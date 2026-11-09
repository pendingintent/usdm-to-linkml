

# Slot: code 



URI: [usdm:slot/code](https://www.cdisc.org/usdm/slot/code)
Alias: code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyRole](../classes/StudyRole.md) |  |  no  |
| [ProductOrganizationRole](../classes/ProductOrganizationRole.md) |  |  no  |
| [Code](../classes/Code.md) |  |  no  |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  no  |
| [Procedure](../classes/Procedure.md) |  |  no  |
| [StudyAmendmentReason](../classes/StudyAmendmentReason.md) |  |  no  |
| [ResponseCode](../classes/ResponseCode.md) |  |  no  |
| [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |  |  no  |
| [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |  |  no  |
| [GeographicScope](../classes/GeographicScope.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [BiomedicalConcept](../classes/BiomedicalConcept.md), [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md), [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md), [Code](../classes/Code.md), [GeographicScope](../classes/GeographicScope.md), [Procedure](../classes/Procedure.md), [ProductOrganizationRole](../classes/ProductOrganizationRole.md), [ResponseCode](../classes/ResponseCode.md), [StudyAmendmentReason](../classes/StudyAmendmentReason.md), [StudyRole](../classes/StudyRole.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:code |
| native | usdm:code |




## LinkML Source

<details>
```yaml
name: code
alias: code
domain_of:
- BiomedicalConcept
- BiomedicalConceptCategory
- BiomedicalConceptProperty
- Code
- GeographicScope
- Procedure
- ProductOrganizationRole
- ResponseCode
- StudyAmendmentReason
- StudyRole
range: string

```
</details>