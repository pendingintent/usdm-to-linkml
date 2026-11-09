#!/usr/bin/env python
"""Generate LinkML schema from the USDM OpenAPI specification."""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from usdm_to_linkml import USDMToLinkMLConverter


def generate_json_schema(linkml_path: Path) -> str:
    """Serialize the LinkML schema at ``linkml_path`` as JSON Schema."""
    from linkml.generators.jsonschemagen import JsonSchemaGenerator

    return JsonSchemaGenerator(str(linkml_path)).serialize()


def main():
    """Generate the LinkML schema."""
    output_path = Path(__file__).parent.parent / "output" / "usdm.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Converting USDM OpenAPI spec to LinkML schema...")
    converter = USDMToLinkMLConverter()
    converter.convert()
    converter.save(str(output_path))

    print(f"Generated LinkML schema: {output_path}")

    json_schema_path = output_path.with_name("usdm.schema.json")
    json_schema_path.write_text(generate_json_schema(output_path))
    print(f"Generated JSON Schema:   {json_schema_path}")
    print(f"  - {len(converter.schema['classes'])} classes")

    return 0


if __name__ == "__main__":
    sys.exit(main())
