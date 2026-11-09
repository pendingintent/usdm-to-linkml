

# Slot: epochId 



URI: [usdm:slot/epochId](https://www.cdisc.org/usdm/slot/epochId)
Alias: epochId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyCell](../classes/StudyCell.md) |  |  no  |
| [ScheduledActivityInstance](../classes/ScheduledActivityInstance.md) |  |  no  |
| [ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ScheduledActivityInstance](../classes/ScheduledActivityInstance.md), [ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md), [StudyCell](../classes/StudyCell.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:epochId |
| native | usdm:epochId |




## LinkML Source

<details>
```yaml
name: epochId
alias: epochId
domain_of:
- ScheduledActivityInstance
- ScheduledDecisionInstance
- StudyCell
range: string

```
</details>