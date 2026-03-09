"""Tests for the USDM to LinkML converter."""

import sys
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from usdm_to_linkml import USDMToLinkMLConverter


@pytest.fixture
def converter():
    """Create a converter instance."""
    return USDMToLinkMLConverter()


@pytest.fixture
def schema(converter):
    """Get the converted schema."""
    return converter.convert()


@pytest.fixture
def schema_view(converter, tmp_path):
    """Get a SchemaView of the converted schema."""
    converter.convert()
    yaml_path = tmp_path / "usdm.yaml"
    converter.save(str(yaml_path))
    return SchemaView(str(yaml_path))


class TestModelDiscovery:
    """Test model discovery from usdm_model package."""

    def test_discovers_core_models(self, converter):
        """Verify core USDM models are discovered."""
        assert "Study" in converter.models
        assert "StudyDesign" in converter.models
        assert "StudyVersion" in converter.models
        assert "Endpoint" in converter.models

    def test_discovers_base_classes(self, converter):
        """Verify base API model classes are included."""
        assert "ApiBaseModel" in converter.models
        assert "ApiBaseModelWithId" in converter.models
        assert "ApiBaseModelWithIdNameLabelAndDesc" in converter.models

    def test_discovers_extension_classes(self, converter):
        """Verify extension classes are included."""
        assert "ExtensionAttribute" in converter.models
        assert "ExtensionClass" in converter.models

    def test_discovers_referenced_classes(self, converter):
        """Verify classes referenced but not in __all__ are included."""
        assert "MedicalDevice" in converter.models
        assert "PersonName" in converter.models
        assert "Substance" in converter.models


class TestSchemaStructure:
    """Test the generated schema structure."""

    def test_schema_has_required_fields(self, schema):
        """Verify schema has all required top-level fields."""
        assert "id" in schema
        assert "name" in schema
        assert "prefixes" in schema
        assert "classes" in schema
        assert "slots" in schema
        assert "imports" in schema

    def test_schema_imports_linkml_types(self, schema):
        """Verify schema imports linkml:types."""
        assert "linkml:types" in schema["imports"]

    def test_schema_has_classes(self, schema):
        """Verify schema has classes defined."""
        assert len(schema["classes"]) > 70  # Should have at least 72 models

    def test_schema_has_slots(self, schema):
        """Verify schema has slots defined."""
        assert len(schema["slots"]) > 100


class TestInheritance:
    """Test inheritance mapping."""

    def test_study_inherits_from_api_base_model(self, schema):
        """Verify Study inherits from ApiBaseModel."""
        assert schema["classes"]["Study"]["is_a"] == "ApiBaseModel"

    def test_study_design_inherits_correctly(self, schema):
        """Verify StudyDesign inherits from ApiBaseModelWithIdNameLabelAndDesc."""
        assert schema["classes"]["StudyDesign"]["is_a"] == "ApiBaseModelWithIdNameLabelAndDesc"

    def test_interventional_study_design_inherits_from_study_design(self, schema):
        """Verify InterventionalStudyDesign inherits from StudyDesign."""
        assert schema["classes"]["InterventionalStudyDesign"]["is_a"] == "StudyDesign"

    def test_base_classes_are_abstract(self, schema):
        """Verify base model classes are marked as abstract."""
        assert schema["classes"]["ApiBaseModel"].get("abstract") is True
        assert schema["classes"]["ApiBaseModelWithId"].get("abstract") is True

    def test_inheritance_chain_resolves(self, schema_view):
        """Verify inheritance chain resolves correctly."""
        ancestors = schema_view.class_ancestors("InterventionalStudyDesign")
        assert "StudyDesign" in ancestors
        assert "ApiBaseModelWithIdNameLabelAndDesc" in ancestors
        assert "ApiBaseModel" in ancestors


class TestInstanceType:
    """Test instanceType handling."""

    def test_instance_type_slot_has_designates_type(self, schema):
        """Verify instanceType slot has designates_type."""
        assert schema["slots"]["instanceType"]["designates_type"] is True

    def test_instance_type_slot_no_equals_string(self, schema):
        """Verify instanceType global slot doesn't have equals_string."""
        assert "equals_string" not in schema["slots"]["instanceType"]

    def test_classes_have_instance_type_slot_usage(self, schema):
        """Verify classes have instanceType in slot_usage."""
        for cls_name in ["Study", "StudyDesign", "Endpoint"]:
            cls_def = schema["classes"][cls_name]
            assert "slot_usage" in cls_def
            assert "instanceType" in cls_def["slot_usage"]
            assert "equals_string" in cls_def["slot_usage"]["instanceType"]

    def test_instance_type_equals_class_name(self, schema):
        """Verify instanceType equals_string matches class name."""
        assert schema["classes"]["Study"]["slot_usage"]["instanceType"]["equals_string"] == "Study"
        assert schema["classes"]["Endpoint"]["slot_usage"]["instanceType"]["equals_string"] == "Endpoint"


class TestIdReferences:
    """Test ID reference slot handling."""

    def test_id_slots_have_inlined_false(self, schema):
        """Verify ID reference slots have inlined: false."""
        assert schema["slots"]["organizationId"]["inlined"] is False
        assert schema["slots"]["biomedicalConceptIds"]["inlined"] is False

    def test_id_slots_infer_range(self, schema):
        """Verify ID reference slots infer correct range when possible."""
        assert schema["slots"]["biomedicalConceptIds"]["range"] == "BiomedicalConcept"
        assert schema["slots"]["organizationId"]["range"] == "Organization"

    def test_list_id_slots_are_multivalued(self, schema):
        """Verify List[str] ID slots are multivalued."""
        assert schema["slots"]["biomedicalConceptIds"]["multivalued"] is True
        assert schema["slots"]["studyInterventionIds"]["multivalued"] is True


class TestTypeMapping:
    """Test Python type to LinkML range mapping."""

    def test_string_fields(self, schema):
        """Verify string fields map to string range."""
        assert schema["slots"]["name"]["range"] == "string"

    def test_list_fields_are_multivalued(self, schema):
        """Verify List fields are multivalued."""
        assert schema["slots"]["extensionAttributes"]["multivalued"] is True

    def test_model_references(self, schema):
        """Verify model references map to class ranges."""
        # Note: This depends on the specific field types in the USDM models
        # The 'country' field should reference Code
        assert schema["slots"]["country"]["range"] == "Code"


class TestSchemaValidation:
    """Test schema validates with LinkML."""

    def test_schema_loads_with_schema_view(self, schema_view):
        """Verify schema loads without errors."""
        # If we got here, the schema loaded successfully
        assert schema_view is not None

    def test_all_classes_resolve(self, schema_view):
        """Verify all class references resolve."""
        for cls_name, cls_def in schema_view.all_classes().items():
            if cls_def.is_a:
                parent = schema_view.get_class(cls_def.is_a)
                assert parent is not None, f"Parent {cls_def.is_a} not found for {cls_name}"

    def test_all_slot_ranges_resolve(self, schema_view):
        """Verify all slot ranges resolve to valid types or classes."""
        # Get all valid ranges (built-in types + classes)
        builtin_types = {"string", "integer", "float", "boolean", "date", "datetime", "uri", "uriorcurie"}
        classes = set(schema_view.all_classes().keys())
        valid_ranges = builtin_types | classes

        for slot_name, slot_def in schema_view.all_slots().items():
            if slot_def.range and slot_def.range not in valid_ranges:
                # Check if it's an any_of pattern
                if not slot_def.any_of:
                    pytest.fail(f"Slot {slot_name} has invalid range: {slot_def.range}")
