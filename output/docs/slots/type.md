

# Slot: type 



URI: [usdm:slot/type](https://www.cdisc.org/usdm/slot/type)
Alias: type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyArm](../classes/StudyArm.md) |  |  no  |
| [StudyIntervention](../classes/StudyIntervention.md) |  |  no  |
| [GovernanceDate](../classes/GovernanceDate.md) |  |  no  |
| [StudyTitle](../classes/StudyTitle.md) |  |  no  |
| [Encounter](../classes/Encounter.md) |  |  no  |
| [Organization](../classes/Organization.md) |  |  no  |
| [ReferenceIdentifier](../classes/ReferenceIdentifier.md) |  |  no  |
| [StudyEpoch](../classes/StudyEpoch.md) |  |  no  |
| [Timing](../classes/Timing.md) |  |  no  |
| [MedicalDeviceIdentifier](../classes/MedicalDeviceIdentifier.md) |  |  no  |
| [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |  |  no  |
| [GeographicScope](../classes/GeographicScope.md) |  |  no  |
| [AdministrableProductProperty](../classes/AdministrableProductProperty.md) |  |  no  |
| [StudyAmendmentImpact](../classes/StudyAmendmentImpact.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AdministrableProductProperty](../classes/AdministrableProductProperty.md), [Encounter](../classes/Encounter.md), [GeographicScope](../classes/GeographicScope.md), [GovernanceDate](../classes/GovernanceDate.md), [MedicalDeviceIdentifier](../classes/MedicalDeviceIdentifier.md), [Organization](../classes/Organization.md), [ReferenceIdentifier](../classes/ReferenceIdentifier.md), [StudyAmendmentImpact](../classes/StudyAmendmentImpact.md), [StudyArm](../classes/StudyArm.md), [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md), [StudyEpoch](../classes/StudyEpoch.md), [StudyIntervention](../classes/StudyIntervention.md), [StudyTitle](../classes/StudyTitle.md), [Timing](../classes/Timing.md) |

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