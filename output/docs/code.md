

# Slot: code 



URI: [usdm:code](https://www.cdisc.org/usdm/code)
Alias: code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyRole](StudyRole.md) |  |  no  |
| [ProductOrganizationRole](ProductOrganizationRole.md) |  |  no  |
| [Code](Code.md) |  |  no  |
| [BiomedicalConcept](BiomedicalConcept.md) |  |  no  |
| [Procedure](Procedure.md) |  |  no  |
| [StudyAmendmentReason](StudyAmendmentReason.md) |  |  no  |
| [ResponseCode](ResponseCode.md) |  |  no  |
| [BiomedicalConceptProperty](BiomedicalConceptProperty.md) |  |  no  |
| [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |  |  no  |
| [GeographicScope](GeographicScope.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiomedicalConcept](BiomedicalConcept.md), [BiomedicalConceptCategory](BiomedicalConceptCategory.md), [BiomedicalConceptProperty](BiomedicalConceptProperty.md), [Code](Code.md), [GeographicScope](GeographicScope.md), [Procedure](Procedure.md), [ProductOrganizationRole](ProductOrganizationRole.md), [ResponseCode](ResponseCode.md), [StudyAmendmentReason](StudyAmendmentReason.md), [StudyRole](StudyRole.md) |

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