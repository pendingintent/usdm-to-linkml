# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

This project converts the **Unified Study Data Model (USDM) API specification** into **LinkML** schemas. USDM is a TransCelerate Digital Data Flow standard for clinical trial study definitions. LinkML enables generation of multiple output formats (JSON Schema, Python, RDF/OWL, SQL, etc.) from a single schema definition.

## Tech Stack

- **Python 3.14** with virtual environment in `.venv/`
- **LinkML 1.10.0** - modeling framework and code generators
- **usdm_model 0.66.0** - Pydantic models for 75+ USDM entities
- **Pydantic 2.x** - data validation
- **pytest 9.0.2** - testing

## Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run single test
pytest path/to/test.py::test_function_name -v
```

## Input Data

`files/USDM_API_v4.0.0.json` - OpenAPI 3.1.0 specification containing:
- 4 REST endpoints for study management
- 164 schema definitions for clinical trial entities (Study, StudyDesign, Arm, Epoch, Intervention, Endpoint, etc.)

## Architecture

**Transformation Pipeline:**
1. Parse USDM OpenAPI specification (JSON)
2. Map USDM Pydantic models to LinkML schema constructs
3. Generate LinkML YAML schemas
4. Use LinkML generators to produce target formats

**Key LinkML Concepts:**
- `classes` - map to USDM entity types
- `slots` - map to entity attributes
- `enums` - map to USDM code lists
- `types` - primitive data types
- `prefixes` - namespace declarations for semantic web URIs

**USDM Domain Model:**
- Core: Study, StudyVersion, StudyDefinition, StudyDesign
- Structural: Arm, Cell, Element, Epoch
- Clinical: Intervention, Population, EligibilityCriterion, Endpoint, Estimand
- Administrative: Organization, Person, Site
- Products: Substance, Ingredient, MedicalDevice
