

# Slot: timings 



URI: [usdm:timings](https://www.cdisc.org/usdm/timings)
Alias: timings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Timing](Timing.md) |
| Domain Of | [ScheduleTimeline](ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | usdm:timings |
| native | usdm:timings |




## LinkML Source

<details>
```yaml
name: timings
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: timings
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: Timing
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>