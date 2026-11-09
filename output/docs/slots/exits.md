

# Slot: exits 



URI: [usdm:slot/exits](https://www.cdisc.org/usdm/slot/exits)
Alias: exits

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](../classes/ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScheduleTimelineExit](../classes/ScheduleTimelineExit.md) |
| Domain Of | [ScheduleTimeline](../classes/ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | usdm:exits |
| native | usdm:exits |




## LinkML Source

<details>
```yaml
name: exits
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: exits
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: ScheduleTimelineExit
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>