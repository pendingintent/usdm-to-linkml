

# Slot: summary 



URI: [usdm:slot/summary](https://www.cdisc.org/usdm/slot/summary)
Alias: summary

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyChange](../classes/StudyChange.md) |  |  no  |
| [StudyAmendment](../classes/StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyAmendment](../classes/StudyAmendment.md), [StudyChange](../classes/StudyChange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:summary |
| native | usdm:summary |




## LinkML Source

<details>
```yaml
name: summary
alias: summary
domain_of:
- StudyAmendment
- StudyChange
range: string

```
</details>