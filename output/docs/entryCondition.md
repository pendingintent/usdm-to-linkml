

# Slot: entryCondition 



URI: [usdm:entryCondition](https://www.cdisc.org/usdm/entryCondition)
Alias: entryCondition

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ScheduleTimeline](ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduleTimeline](ScheduleTimeline.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:entryCondition |
| native | usdm:entryCondition |




## LinkML Source

<details>
```yaml
name: entryCondition
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: entryCondition
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: string
required: true

```
</details>