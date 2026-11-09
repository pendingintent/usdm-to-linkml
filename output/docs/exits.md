

# Slot: exits 



URI: [usdm:exits](https://www.cdisc.org/usdm/exits)
Alias: exits

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ScheduleTimelineExit](ScheduleTimelineExit.md) |
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