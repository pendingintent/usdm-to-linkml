"""Convert USDM Pydantic models to LinkML schema."""

import re
from typing import Any, Union, get_args, get_origin
from uuid import UUID

import yaml
from pydantic import BaseModel

import usdm_model
from usdm_model.api_base_model import (
    ApiBaseModel,
    ApiBaseModelWithId,
    ApiBaseModelWithIdAndDesc,
    ApiBaseModelWithIdAndName,
    ApiBaseModelWithIdNameAndLabel,
    ApiBaseModelWithIdNameLabelAndDesc,
    ApiBaseModelWithIdNameAndDesc,
    ApiBaseModelWithIdOnly,
)
from usdm_model.extension import (
    Extension,
    ExtensionAttribute,
    ExtensionClass,
    BaseCode,
    BaseAliasCode,
    BaseQuantity,
    BaseRange,
)


class USDMToLinkMLConverter:
    """Converts USDM Pydantic models to LinkML YAML schema."""

    # Python types to LinkML ranges
    TYPE_MAP = {
        str: "string",
        int: "integer",
        float: "float",
        bool: "boolean",
        UUID: "string",  # UUIDs are serialized as strings
    }

    # Base model classes in inheritance order (most specific first)
    BASE_CLASSES = [
        ApiBaseModelWithIdNameLabelAndDesc,
        ApiBaseModelWithIdNameAndLabel,
        ApiBaseModelWithIdNameAndDesc,
        ApiBaseModelWithIdAndDesc,
        ApiBaseModelWithIdAndName,
        ApiBaseModelWithId,
        ApiBaseModelWithIdOnly,
        ApiBaseModel,
    ]

    # Additional base classes from extension.py
    EXTENSION_BASE_CLASSES = [
        Extension,
        ExtensionAttribute,
        ExtensionClass,
        BaseCode,
        BaseAliasCode,
        BaseQuantity,
        BaseRange,
    ]

    def __init__(self):
        """Initialize the converter."""
        self.models: dict[str, type[BaseModel]] = {}
        self.schema: dict[str, Any] = {}
        self._discover_models()

    def _discover_models(self) -> None:
        """Discover all USDM model classes from the usdm_model package."""
        # Get all models from __all__
        for name in usdm_model.__all__:
            cls = getattr(usdm_model, name, None)
            if cls is not None and isinstance(cls, type) and issubclass(cls, BaseModel):
                self.models[name] = cls

        # Also add ConditionAssignment which is not in __all__ but is used
        from usdm_model.scheduled_instance import ConditionAssignment
        self.models["ConditionAssignment"] = ConditionAssignment

        # Add base model classes
        for cls in self.BASE_CLASSES:
            self.models[cls.__name__] = cls

        # Add extension base classes
        for cls in self.EXTENSION_BASE_CLASSES:
            self.models[cls.__name__] = cls

        # Add classes not in __all__ but referenced by other models
        additional_classes = [
            ("usdm_model.biospecimen_retention", "BiospecimenRetention"),
            ("usdm_model.comment_annotation", "CommentAnnotation"),
            ("usdm_model.assigned_person", "PersonName"),
            ("usdm_model.ingredient", "Substance"),
            ("usdm_model.study_amendment", "StudyChange"),
            ("usdm_model.study_amendment", "StudyAmendmentImpact"),
            ("usdm_model.medical_device", "MedicalDevice"),
            ("usdm_model.product_organization_role", "ProductOrganizationRole"),
        ]

        for module_name, class_name in additional_classes:
            try:
                import importlib
                module = importlib.import_module(module_name)
                cls = getattr(module, class_name, None)
                if cls is not None:
                    self.models[class_name] = cls
            except (ImportError, AttributeError):
                pass

    def _get_parent_class(self, cls: type) -> str | None:
        """Get the LinkML parent class name for a Pydantic model."""
        if cls is BaseModel:
            return None

        # Check direct bases
        for base in cls.__bases__:
            if base is BaseModel:
                return None
            if base.__name__ in self.models:
                return base.__name__

        return None

    def _is_abstract_class(self, cls: type) -> bool:
        """Determine if a class should be marked as abstract in LinkML."""
        # Base API model classes are abstract
        if cls in self.BASE_CLASSES:
            return True
        if cls in [Extension]:
            return True
        # Classes with subclasses that override instanceType are abstract
        cls_name = cls.__name__
        for model_cls in self.models.values():
            if model_cls is not cls:
                parent = self._get_parent_class(model_cls)
                if parent == cls_name:
                    # Check if the subclass has its own instanceType
                    if "instanceType" in model_cls.model_fields:
                        return True
        return False

    def _parse_type(self, field_type: Any) -> dict[str, Any]:
        """Parse a Python type annotation into LinkML slot properties."""
        result: dict[str, Any] = {}

        origin = get_origin(field_type)
        args = get_args(field_type)

        # Handle Literal types (e.g., Literal["Study"])
        if origin is type(None):
            result["range"] = "string"
            return result

        # Handle Literal
        try:
            from typing import Literal
            if origin is Literal:
                result["range"] = "string"
                if args:
                    result["equals_string"] = args[0]
                return result
        except ImportError:
            pass

        # Handle Union types
        if origin is Union:
            non_none_args = [a for a in args if a is not type(None)]
            if len(non_none_args) == 0:
                result["range"] = "string"
            elif len(non_none_args) == 1:
                # Optional[X] -> X with required: false
                inner_result = self._parse_type(non_none_args[0])
                result.update(inner_result)
                result["required"] = False
            else:
                # Union of multiple non-None types
                any_of = []
                for arg in non_none_args:
                    inner = self._parse_type(arg)
                    any_of.append({"range": inner.get("range", "string")})
                result["any_of"] = any_of
            return result

        # Handle List types
        if origin is list:
            result["multivalued"] = True
            if args:
                inner_result = self._parse_type(args[0])
                result.update(inner_result)
                # Keep multivalued even if inner type sets something
                result["multivalued"] = True
            else:
                result["range"] = "string"
            return result

        # Handle primitive types
        if field_type in self.TYPE_MAP:
            result["range"] = self.TYPE_MAP[field_type]
            return result

        # Handle USDM model references
        if isinstance(field_type, type):
            if field_type.__name__ in self.models:
                result["range"] = field_type.__name__
                return result
            if issubclass(field_type, BaseModel):
                result["range"] = field_type.__name__
                return result

        # Default to string
        result["range"] = "string"
        return result

    def _is_id_reference(self, field_name: str) -> tuple[bool, str | None]:
        """Check if a field name indicates an ID reference and infer the target class."""
        if field_name.endswith("Ids"):
            # pluralIds -> infer singular class name
            base = field_name[:-3]  # Remove "Ids"
            # Convert camelCase to class name possibilities
            candidates = self._infer_class_names(base)
            for candidate in candidates:
                if candidate in self.models:
                    return True, candidate
            return True, None
        elif field_name.endswith("Id") and field_name != "id":
            # singularId -> infer class name
            base = field_name[:-2]  # Remove "Id"
            candidates = self._infer_class_names(base)
            for candidate in candidates:
                if candidate in self.models:
                    return True, candidate
            return True, None
        return False, None

    def _infer_class_names(self, base: str) -> list[str]:
        """Infer possible class names from a base field name."""
        candidates = []
        # Direct match with first letter capitalized
        candidates.append(base[0].upper() + base[1:] if base else base)
        # Try adding common prefixes
        for prefix in ["Study", "Schedule", "Administrable"]:
            if base.lower().startswith(prefix.lower()):
                continue
            candidates.append(prefix + base[0].upper() + base[1:])
        return candidates

    def _convert_class(self, name: str, cls: type) -> dict[str, Any]:
        """Convert a single Pydantic model to a LinkML class definition."""
        class_def: dict[str, Any] = {}

        # Set parent class
        parent = self._get_parent_class(cls)
        if parent:
            class_def["is_a"] = parent

        # Check if abstract
        if self._is_abstract_class(cls):
            class_def["abstract"] = True

        # Get slots from model_fields
        slots = []
        slot_usage = {}

        for field_name, field_info in cls.model_fields.items():
            # Check if field is inherited from parent
            is_inherited = False
            if parent and parent in self.models:
                parent_cls = self.models[parent]
                if field_name in parent_cls.model_fields:
                    is_inherited = True

            # Handle instanceType specially - add to slot_usage with equals_string
            if field_name == "instanceType":
                slot_props = self._parse_type(field_info.annotation)
                if "equals_string" in slot_props:
                    slot_usage["instanceType"] = {
                        "equals_string": slot_props["equals_string"]
                    }
                # Only add to slots list if not inherited
                if not is_inherited:
                    slots.append(field_name)
                continue

            # Skip other inherited fields
            if is_inherited:
                continue

            slots.append(field_name)

        if slots:
            class_def["slots"] = slots

        if slot_usage:
            class_def["slot_usage"] = slot_usage

        return class_def

    def _convert_slot(self, field_name: str, field_info: Any, owner_class: str) -> dict[str, Any]:
        """Convert a Pydantic field to a LinkML slot definition."""
        slot_def: dict[str, Any] = {}

        # Parse the type
        type_info = self._parse_type(field_info.annotation)
        slot_def.update(type_info)

        # Check for ID references
        is_ref, target_class = self._is_id_reference(field_name)
        if is_ref:
            slot_def["inlined"] = False
            if target_class:
                slot_def["range"] = target_class

        # Handle special fields
        if field_name == "id":
            slot_def["identifier"] = True
            slot_def["range"] = "string"
        elif field_name == "instanceType":
            slot_def["designates_type"] = True
            # Remove equals_string from global slot - it belongs in slot_usage per class
            slot_def.pop("equals_string", None)
            slot_def["range"] = "string"

        # Check if required (has no default or default is not None)
        if field_info.default is None and field_info.default_factory is None:
            if "required" not in slot_def:
                slot_def["required"] = True
        elif field_info.default is not None or field_info.default_factory is not None:
            # Has a default value, so not strictly required
            if "required" not in slot_def:
                slot_def["required"] = False

        return slot_def

    def convert(self) -> dict[str, Any]:
        """Convert all USDM models to a LinkML schema."""
        self.schema = {
            "id": "https://www.cdisc.org/usdm",
            "name": "usdm",
            "title": "Unified Study Definitions Model",
            "version": "4.0.0",
            "prefixes": {
                "usdm": "https://www.cdisc.org/usdm/",
                "linkml": "https://w3id.org/linkml/",
            },
            "default_prefix": "usdm",
            "default_range": "string",
            "imports": ["linkml:types"],
            "classes": {},
            "slots": {},
        }

        # First pass: collect all slots from all classes
        all_slots: dict[str, dict[str, Any]] = {}

        for name, cls in sorted(self.models.items()):
            for field_name, field_info in cls.model_fields.items():
                if field_name not in all_slots:
                    all_slots[field_name] = self._convert_slot(field_name, field_info, name)

        # Add global slots
        self.schema["slots"] = all_slots

        # Second pass: convert classes
        for name, cls in sorted(self.models.items()):
            class_def = self._convert_class(name, cls)
            if class_def:  # Only add non-empty class definitions
                self.schema["classes"][name] = class_def

        return self.schema

    def to_yaml(self) -> str:
        """Convert the schema to YAML string."""
        if not self.schema:
            self.convert()

        # Custom representer for cleaner YAML output
        def str_representer(dumper, data):
            if '\n' in data:
                return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
            return dumper.represent_scalar('tag:yaml.org,2002:str', data)

        yaml.add_representer(str, str_representer)

        return yaml.dump(
            self.schema,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            width=120,
        )

    def save(self, path: str) -> None:
        """Save the schema to a YAML file."""
        yaml_content = self.to_yaml()
        with open(path, "w") as f:
            f.write(yaml_content)


def main():
    """Main entry point for the converter."""
    converter = USDMToLinkMLConverter()
    converter.convert()
    converter.save("output/usdm.yaml")
    print(f"Generated LinkML schema with {len(converter.schema['classes'])} classes")
    print(f"and {len(converter.schema['slots'])} slots")


if __name__ == "__main__":
    main()
