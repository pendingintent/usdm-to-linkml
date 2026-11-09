# USDM to LinkML

Converts the [USDM](https://www.cdisc.org/ddf) (Unified Study Definitions Model) **v4.0.0 OpenAPI specification** into a [LinkML](https://linkml.io) schema, so you can generate JSON Schema, Python, OWL and other formats from one source.

- **Input:** `files/USDM_API_v4.0.0.json` (the source of truth)
- **Output:** `output/usdm.yaml` (LinkML, 82 classes) and `output/usdm.schema.json` (JSON Schema)

## Quick start

```bash
# 1. Set up (Python 3.14)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Generate the LinkML schema and JSON Schema
python scripts/generate_schema.py

# 3. Run the tests
pytest
```

## Generate other formats

`output/usdm.schema.json` is produced by step 2. For other formats, run these from the project root:

```bash
gen-pydantic    output/usdm.yaml > output/usdm_models.py
gen-python      output/usdm.yaml > output/usdm_dataclasses.py
gen-owl         output/usdm.yaml > output/usdm.owl.ttl
```

## How the conversion works

Each OpenAPI schema becomes one LinkML class with its own `attributes`:

| OpenAPI | LinkML |
|---|---|
| `X-Input` / `X-Output` | one class `X` (the converter fails if they ever differ) |
| `required` list | `required: true` |
| `type: array` | `multivalued: true` |
| `$ref` | class range (inlined) |
| `anyOf` of classes (e.g. `Quantity` or `Range`) | `any_of` |
| `instanceType` constant | `equals_string` + `designates_type` |
| `minLength: 1` | non-empty `pattern` |
| `format: uuid` / `date` | UUID `pattern` / `date` range |

Notes:
- The API model is flat, so there is no class inheritance in the output.
- `*Id` / `*Ids` attributes are plain strings, as in the spec.
- `HTTPValidationError` and `ValidationError` (FastAPI error types) are excluded.
- `linkml-lint output/usdm.yaml` reports no errors; its warnings are about missing descriptions and the spec's camelCase names.

## Tests

`pytest` checks:
- every class in the generated schema against the raw OpenAPI file (attributes, types, unions, cardinality, required fields, `instanceType`, constraints)
- the example USDM files in `examples/` validate against the OpenAPI spec, the generated JSON Schema and LinkML's validator, and deliberately broken data is rejected
- `output/usdm.yaml` and `output/usdm.schema.json` are up to date. After changing the converter or the spec, re-run `python scripts/generate_schema.py` and commit the result.

To validate your own USDM file:

```bash
linkml-validate -s output/usdm.yaml -C Wrapper path/to/study.json
```

Note: the `linkml-validate` command treats an empty list (`[]`) in a required list attribute as missing, whereas the USDM spec allows it. The JSON Schema (`output/usdm.schema.json`) follows the spec, so use it if you see such errors on valid files.

## Project layout

```
files/USDM_API_v4.0.0.json        input spec
src/usdm_to_linkml/converter.py   converter
scripts/generate_schema.py        command-line entry point
output/                           generated schemas
examples/                         sample USDM v4.0.0 files used in tests
tests/test_converter.py           conformance and regression tests
```
