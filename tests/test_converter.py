"""Tests for the USDM OpenAPI -> LinkML converter.

``TestSpecConformance`` is the regression suite: it re-derives the expected
shape of every class straight from ``files/USDM_API_v4.0.0.json`` (independently
of the converter's own code) and compares it with what LinkML's SchemaView sees
in both a freshly generated schema and the committed ``output/usdm.yaml``.
"""

import json
import re
import sys
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))

from usdm_to_linkml import USDMToLinkMLConverter  # noqa: E402

SPEC = ROOT / "files" / "USDM_API_v4.0.0.json"
COMMITTED = ROOT / "output" / "usdm.yaml"
EXCLUDED = {"HTTPValidationError", "ValidationError"}
PRIMITIVES = {
    "string": "string",
    "integer": "integer",
    "number": "float",
    "boolean": "boolean",
}


def strip(name: str) -> str:
    return re.sub(r"-(Input|Output)$", "", name)


# ---------------------------------------------------------------- expectations
def _expected_range(node):
    """-> (range or frozenset of class names, multivalued)"""
    if "anyOf" in node:
        options = [o for o in node["anyOf"] if o.get("type") != "null"]
        if len(options) == 1:
            node = options[0]
        else:
            return frozenset(strip(o["$ref"].split("/")[-1]) for o in options), False
    if node.get("type") == "array":
        inner, _ = _expected_range(node["items"])
        return inner, True
    if "$ref" in node:
        return strip(node["$ref"].split("/")[-1]), False
    if node.get("format") == "date":
        return "date", False
    return PRIMITIVES[node["type"]], False


def _spec_classes():
    spec = json.loads(SPEC.read_text())
    out = {}
    for name, body in spec["components"]["schemas"].items():
        cname = strip(name)
        if cname in EXCLUDED:
            continue
        required = set(body.get("required", []))
        attrs = {}
        for pname, prop in body["properties"].items():
            rng, multi = _expected_range(prop)
            attrs[pname] = (rng, multi, pname in required)
        out.setdefault(cname, []).append((name, attrs, body))
    return out


SPEC_CLASSES = _spec_classes()


@pytest.fixture(scope="module")
def converter():
    return USDMToLinkMLConverter()


@pytest.fixture(scope="module")
def schema(converter):
    return converter.convert()


@pytest.fixture(scope="module")
def fresh_view(converter, tmp_path_factory):
    converter.convert()
    path = tmp_path_factory.mktemp("schema") / "usdm.yaml"
    converter.save(path)
    return SchemaView(str(path))


@pytest.fixture(scope="module")
def committed_view():
    return SchemaView(str(COMMITTED))


def _induced(view, cname):
    return {s.name: s for s in view.class_induced_slots(cname)}


def _actual_range(slot):
    if slot.any_of:
        return frozenset(a.range for a in slot.any_of)
    return slot.range


# ------------------------------------------------------------------ conformance
@pytest.fixture(params=["fresh_view", "committed_view"])
def view(request):
    return request.getfixturevalue(request.param)


class TestSpecConformance:
    def test_spec_input_and_output_variants_are_identical(self):
        """The converter collapses X-Input/X-Output; guard that assumption."""
        for cname, variants in SPEC_CLASSES.items():
            assert all(v[1] == variants[0][1] for v in variants), cname

    def test_class_set_matches_spec(self, view):
        classes = set(view.all_classes())
        assert set(SPEC_CLASSES) <= classes
        # only the linkml:Any helper may be extra
        assert classes - set(SPEC_CLASSES) <= {"Any"}

    def test_version_matches_spec(self, view):
        spec = json.loads(SPEC.read_text())
        assert view.schema.version == spec["info"]["version"]

    @pytest.mark.parametrize("cname", sorted(SPEC_CLASSES))
    def test_class_attributes_match_spec(self, view, cname):
        expected = SPEC_CLASSES[cname][0][1]
        actual = _induced(view, cname)
        assert set(actual) == set(expected), f"{cname} attribute set differs"
        problems = []
        for aname, (rng, multi, required) in expected.items():
            slot = actual[aname]
            if _actual_range(slot) != rng:
                problems.append(f"{aname}: range {_actual_range(slot)!r} != {rng!r}")
            if bool(slot.multivalued) != multi:
                problems.append(f"{aname}: multivalued {slot.multivalued} != {multi}")
            if bool(slot.required) != required:
                problems.append(f"{aname}: required {slot.required} != {required}")
        assert not problems, f"{cname}: " + "; ".join(problems)

    @pytest.mark.parametrize("cname", sorted(SPEC_CLASSES))
    def test_instance_type_constant(self, view, cname):
        body = SPEC_CLASSES[cname][0][2]
        if "instanceType" not in body["properties"]:
            pytest.skip(f"{cname} has no instanceType in the spec")
        const = body["properties"]["instanceType"]["const"]
        slot = _induced(view, cname)["instanceType"]
        assert const == cname
        assert slot.equals_string == const
        assert slot.designates_type

    def test_non_empty_string_constraint_preserved(self, view):
        """Every spec ``minLength: 1`` must be a non-empty pattern in LinkML."""
        checked = 0
        for cname, variants in SPEC_CLASSES.items():
            body = variants[0][2]
            slots = _induced(view, cname)
            for pname, prop in body["properties"].items():
                nodes = prop.get("anyOf", [prop])
                if any(n.get("minLength") == 1 for n in nodes):
                    assert slots[pname].pattern, f"{cname}.{pname}"
                    checked += 1
        assert checked == 133  # unique class attributes (Input/Output pairs collapsed)

    def test_formats_preserved(self, view):
        assert _induced(view, "GovernanceDate")["dateValue"].range == "date"
        assert "0-9a-fA-F" in _induced(view, "Study")["id"].pattern


class TestSpecificRegressions:
    """Cases that the previous Pydantic-derived schema got wrong."""

    @pytest.mark.parametrize(
        "cname,aname,rng",
        [
            ("Procedure", "code", "Code"),
            ("StudyRole", "code", "Code"),
            ("BiomedicalConcept", "code", "AliasCode"),
            ("GeographicScope", "code", "AliasCode"),
            ("BiomedicalConcept", "properties", "BiomedicalConceptProperty"),
            ("MedicalDevice", "identifiers", "MedicalDeviceIdentifier"),
            ("StudyCohort", "characteristics", "Characteristic"),
            ("StudyDefinitionDocument", "versions", "StudyDefinitionDocumentVersion"),
            ("ExtensionAttribute", "valueCode", "Code"),
            ("Quantity", "unit", "AliasCode"),
            ("Range", "minValue", "Quantity"),
            ("Timing", "value", "string"),
        ],
    )
    def test_ranges(self, view, cname, aname, rng):
        assert _induced(view, cname)[aname].range == rng

    @pytest.mark.parametrize(
        "cname,aname,members",
        [
            ("Duration", "quantity", {"Quantity", "Range"}),
            ("Strength", "numerator", {"Quantity", "Range"}),
            ("StudyVersion", "studyDesigns",
             {"InterventionalStudyDesign", "ObservationalStudyDesign"}),
            ("ScheduleTimeline", "instances",
             {"ScheduledActivityInstance", "ScheduledDecisionInstance"}),
        ],
    )
    def test_unions(self, view, cname, aname, members):
        assert _actual_range(_induced(view, cname)[aname]) == frozenset(members)

    def test_required_attributes_preserved(self, view):
        activity = _induced(view, "Activity")
        assert {n for n, s in activity.items() if s.required} == {
            "id", "name", "instanceType"
        }

    def test_study_has_extension_attributes(self, view):
        assert "extensionAttributes" in _induced(view, "Study")


class TestCommittedOutput:
    def test_committed_yaml_is_up_to_date(self, converter):
        """output/usdm.yaml must equal a fresh conversion (run generate_schema.py)."""
        assert COMMITTED.read_text() == converter.to_yaml()


class TestSchemaValidity:
    def test_all_slot_ranges_resolve(self, fresh_view):
        known = set(fresh_view.all_classes()) | set(fresh_view.all_types())
        for cname in fresh_view.all_classes():
            for slot in fresh_view.class_induced_slots(cname):
                assert slot.range in known, f"{cname}.{slot.name}: {slot.range}"
                for alt in slot.any_of or []:
                    assert alt.range in known

    def test_generates_json_schema(self, tmp_path):
        from linkml.generators.jsonschemagen import JsonSchemaGenerator

        out = json.loads(JsonSchemaGenerator(str(COMMITTED)).serialize())
        assert "Study" in out["$defs"]
        assert set(out["$defs"]["Activity"]["required"]) >= {"id", "name", "instanceType"}
