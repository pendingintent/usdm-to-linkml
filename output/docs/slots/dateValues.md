

# Slot: dateValues 



URI: [usdm:slot/dateValues](https://www.cdisc.org/usdm/slot/dateValues)
Alias: dateValues

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |  |  no  |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |
| [StudyAmendment](../classes/StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyAmendment](../classes/StudyAmendment.md), [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md), [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:dateValues |
| native | usdm:dateValues |




## LinkML Source

<details>
```yaml
name: dateValues
alias: dateValues
domain_of:
- StudyAmendment
- StudyDefinitionDocumentVersion
- StudyVersion
range: string

```
</details>