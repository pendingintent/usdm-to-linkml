

# Slot: entryId 



URI: [usdm:slot/entryId](https://www.cdisc.org/usdm/slot/entryId)
Alias: entryId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](../classes/ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ScheduleTimeline](../classes/ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduleTimeline](../classes/ScheduleTimeline.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:entryId |
| native | usdm:entryId |




## LinkML Source

<details>
```yaml
name: entryId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: entryId
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: string
required: true

```
</details>