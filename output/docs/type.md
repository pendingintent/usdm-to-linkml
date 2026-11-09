

# Slot: type 



URI: [usdm:type](https://www.cdisc.org/usdm/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyArm](StudyArm.md) |  |  no  |
| [StudyIntervention](StudyIntervention.md) |  |  no  |
| [GovernanceDate](GovernanceDate.md) |  |  no  |
| [StudyTitle](StudyTitle.md) |  |  no  |
| [Encounter](Encounter.md) |  |  no  |
| [Organization](Organization.md) |  |  no  |
| [ReferenceIdentifier](ReferenceIdentifier.md) |  |  no  |
| [StudyEpoch](StudyEpoch.md) |  |  no  |
| [Timing](Timing.md) |  |  no  |
| [MedicalDeviceIdentifier](MedicalDeviceIdentifier.md) |  |  no  |
| [StudyDefinitionDocument](StudyDefinitionDocument.md) |  |  no  |
| [GeographicScope](GeographicScope.md) |  |  no  |
| [AdministrableProductProperty](AdministrableProductProperty.md) |  |  no  |
| [StudyAmendmentImpact](StudyAmendmentImpact.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [AdministrableProductProperty](AdministrableProductProperty.md), [Encounter](Encounter.md), [GeographicScope](GeographicScope.md), [GovernanceDate](GovernanceDate.md), [MedicalDeviceIdentifier](MedicalDeviceIdentifier.md), [Organization](Organization.md), [ReferenceIdentifier](ReferenceIdentifier.md), [StudyAmendmentImpact](StudyAmendmentImpact.md), [StudyArm](StudyArm.md), [StudyDefinitionDocument](StudyDefinitionDocument.md), [StudyEpoch](StudyEpoch.md), [StudyIntervention](StudyIntervention.md), [StudyTitle](StudyTitle.md), [Timing](Timing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:type |
| native | usdm:type |




## LinkML Source

<details>
```yaml
name: type
alias: type
domain_of:
- AdministrableProductProperty
- Encounter
- GeographicScope
- GovernanceDate
- MedicalDeviceIdentifier
- Organization
- ReferenceIdentifier
- StudyAmendmentImpact
- StudyArm
- StudyDefinitionDocument
- StudyEpoch
- StudyIntervention
- StudyTitle
- Timing
range: string

```
</details>