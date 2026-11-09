

# Slot: mainTimeline 



URI: [usdm:slot/mainTimeline](https://www.cdisc.org/usdm/slot/mainTimeline)
Alias: mainTimeline

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](../classes/ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
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
| self | usdm:mainTimeline |
| native | usdm:mainTimeline |




## LinkML Source

<details>
```yaml
name: mainTimeline
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: mainTimeline
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: boolean
required: true

```
</details>