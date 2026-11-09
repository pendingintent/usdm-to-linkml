"""Convert the USDM OpenAPI specification into a LinkML schema.

The OpenAPI document (``files/USDM_API_v4.0.0.json``) is the source of truth.
Every schema in ``components/schemas`` becomes a LinkML class whose
``attributes`` mirror the OpenAPI properties, so that ranges, cardinality and
required-ness are scoped per class (LinkML's global ``slots`` would otherwise
force same-named attributes such as ``code`` to share one definition).

Mapping rules
-------------
* ``X-Input`` / ``X-Output`` -> class ``X`` (the two variants are verified to
  be structurally identical; a mismatch raises ``ValueError``).
* ``type: array``            -> ``multivalued: true``
* ``required`` list          -> ``required: true``; ``anyOf [.., null]`` and
  properties not listed as required are optional.
* ``$ref``                   -> class range, ``inlined: true`` (+ ``inlined_as_list``)
* ``anyOf [$ref A, $ref B]`` -> ``any_of`` of class ranges
* ``const``/single ``enum``  -> ``equals_string``; ``instanceType`` also gets
  ``designates_type: true``
* ``minLength: 1``           -> ``pattern`` requiring a non-empty string
* ``format: uuid``           -> string with a UUID ``pattern``
* ``format: date``           -> ``date``
* ``id`` (required)          -> ``identifier: true``
"""

import json
import re
from pathlib import Path
from typing import Any

import yaml

DEFAULT_SPEC_PATH = (
    Path(__file__).resolve().parents[2] / "files" / "USDM_API_v4.0.0.json"
)

UUID_PATTERN = (
    "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
)
NON_EMPTY_PATTERN = r"^[\s\S]+$"

_VARIANT_SUFFIX = re.compile(r"-(Input|Output)$")


def class_name(schema_name: str) -> str:
    """Strip the ``-Input`` / ``-Output`` suffix from an OpenAPI schema name."""
    return _VARIANT_SUFFIX.sub("", schema_name)


class USDMToLinkMLConverter:
    """Converts the USDM OpenAPI specification to a LinkML YAML schema."""

    # JSON Schema primitive -> LinkML range
    TYPE_MAP = {
        "string": "string",
        "integer": "integer",
        "number": "float",
        "boolean": "boolean",
    }

    # FastAPI error envelopes, not part of the USDM data model
    EXCLUDED_SCHEMAS = {"HTTPValidationError", "ValidationError"}

    def __init__(self, spec_path: str | Path = DEFAULT_SPEC_PATH):
        self.spec_path = Path(spec_path)
        with open(self.spec_path) as f:
            self.spec: dict[str, Any] = json.load(f)
        self.schemas: dict[str, dict[str, Any]] = self._load_schemas()
        self.schema: dict[str, Any] = {}

    # ------------------------------------------------------------------ input
    def _load_schemas(self) -> dict[str, dict[str, Any]]:
        """Collapse Input/Output variants into one OpenAPI schema per class."""
        raw = self.spec["components"]["schemas"]
        grouped: dict[str, dict[str, dict[str, Any]]] = {}
        for name, body in raw.items():
            cname = class_name(name)
            if cname in self.EXCLUDED_SCHEMAS:
                continue
            grouped.setdefault(cname, {})[name] = body

        schemas: dict[str, dict[str, Any]] = {}
        for cname, variants in grouped.items():
            normalised = {
                n: json.loads(
                    re.sub(r"-(Input|Output)\"", '"', json.dumps(body))
                )
                for n, body in variants.items()
            }
            first = next(iter(normalised.values()))
            if any(v != first for v in normalised.values()):
                raise ValueError(
                    f"Input/Output variants of {cname} differ; "
                    "converter assumes they are identical"
                )
            schemas[cname] = first
        return schemas

    # ------------------------------------------------------------- conversion
    def _range_of(self, node: dict[str, Any]) -> dict[str, Any]:
        """Map a (non-array, non-null) JSON schema node to LinkML slot fields."""
        if "$ref" in node:
            target = class_name(node["$ref"].rsplit("/", 1)[-1])
            return {"range": target, "inlined": True, "inlined_as_list": True}

        result: dict[str, Any] = {}
        jtype = node.get("type", "string")
        fmt = node.get("format")
        if jtype == "string" and fmt == "date":
            result["range"] = "date"
        else:
            result["range"] = self.TYPE_MAP[jtype]
        if fmt == "uuid":
            result["pattern"] = UUID_PATTERN
        if node.get("minLength") == 1:
            result["pattern"] = NON_EMPTY_PATTERN
        elif "minLength" in node:
            raise ValueError(f"Unsupported minLength: {node['minLength']}")

        const = node.get("const")
        if const is None and len(node.get("enum", [])) == 1:
            const = node["enum"][0]
        if const is not None:
            result["equals_string"] = const
        elif "enum" in node:
            raise ValueError(f"Multi-valued enum not supported: {node['enum']}")
        return result

    def _union_of(self, options: list[dict[str, Any]]) -> dict[str, Any]:
        """Map one or more non-null alternatives to LinkML slot fields."""
        if len(options) == 1:
            return self._range_of(options[0])
        parts = [self._range_of(o) for o in options]
        if not all("$ref" in o for o in options):
            raise ValueError(f"Unsupported union of non-class types: {options}")
        return {
            "range": "Any",
            "any_of": [{"range": p["range"]} for p in parts],
            "inlined": True,
            "inlined_as_list": True,
        }

    def _convert_property(
        self, name: str, prop: dict[str, Any], required: bool
    ) -> dict[str, Any]:
        node = prop
        if "anyOf" in node:
            options = [o for o in node["anyOf"] if o.get("type") != "null"]
            node = {"anyOf": options}
        else:
            node = {"anyOf": [node]}

        options = node["anyOf"]
        multivalued = False
        if len(options) == 1 and options[0].get("type") == "array":
            multivalued = True
            items = options[0]["items"]
            options = items["anyOf"] if "anyOf" in items else [items]

        attr = self._union_of(options)
        if multivalued:
            attr["multivalued"] = True
        elif "inlined_as_list" in attr:
            del attr["inlined_as_list"]  # only meaningful for lists

        if name == "id" and required and attr["range"] in ("string",):
            attr["identifier"] = True
        if name == "instanceType":
            attr["designates_type"] = True
        # Keep the attribute definition in a stable, readable key order
        attr["required"] = required
        return attr

    def _convert_class(self, cname: str, body: dict[str, Any]) -> dict[str, Any]:
        required = set(body.get("required", []))
        attributes = {
            pname: self._convert_property(pname, prop, pname in required)
            for pname, prop in body.get("properties", {}).items()
        }
        return {"attributes": attributes}

    def convert(self) -> dict[str, Any]:
        """Build the LinkML schema dictionary."""
        info = self.spec.get("info", {})
        classes = {
            cname: self._convert_class(cname, body)
            for cname, body in sorted(self.schemas.items())
        }

        any_used = any(
            a.get("range") == "Any"
            for c in classes.values()
            for a in c["attributes"].values()
        )
        self.schema = {
            "id": "https://www.cdisc.org/usdm",
            "name": "usdm",
            "title": "Unified Study Definitions Model",
            "description": info.get("description")
            or "Generated from the USDM OpenAPI specification.",
            "version": info.get("version", "4.0.0"),
            "prefixes": {
                "usdm": "https://www.cdisc.org/usdm/",
                "linkml": "https://w3id.org/linkml/",
            },
            "default_prefix": "usdm",
            "default_range": "string",
            "imports": ["linkml:types"],
            "classes": classes,
        }
        if any_used:
            # 'Any' is the range of union-typed slots; any_of narrows it.
            self.schema["classes"] = {
                "Any": {"class_uri": "linkml:Any", "abstract": True},
                **classes,
            }
        return self.schema

    # ----------------------------------------------------------------- output
    def to_yaml(self) -> str:
        """Convert the schema to a YAML string."""
        if not self.schema:
            self.convert()
        return yaml.dump(
            self.schema,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )

    def save(self, path: str | Path) -> None:
        """Save the schema to a YAML file."""
        with open(path, "w") as f:
            f.write(self.to_yaml())


def main():
    """Main entry point for the converter."""
    converter = USDMToLinkMLConverter()
    converter.convert()
    converter.save("output/usdm.yaml")
    print(f"Generated LinkML schema with {len(converter.schema['classes'])} classes")


if __name__ == "__main__":
    main()
