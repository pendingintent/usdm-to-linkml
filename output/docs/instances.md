

# Slot: instances 



URI: [usdm:instances](https://www.cdisc.org/usdm/instances)
Alias: instances

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](Any.md)&nbsp;or&nbsp;<br />[ScheduledActivityInstance](ScheduledActivityInstance.md)&nbsp;or&nbsp;<br />[ScheduledDecisionInstance](ScheduledDecisionInstance.md) |
| Domain Of | [ScheduleTimeline](ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduleTimeline](ScheduleTimeline.md) |


<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'ScheduledActivityInstance', 'inlined': True})
- AnonymousSlotExpression({'range': 'ScheduledDecisionInstance', 'inlined': True})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:instances |
| native | usdm:instances |




## LinkML Source

<details>
```yaml
name: instances
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: instances
owner: ScheduleTimeline
domain_of:
- ScheduleTimeline
range: Any
required: false
multivalued: true
inlined: true
inlined_as_list: true
any_of:
- range: ScheduledActivityInstance
  inlined: true
- range: ScheduledDecisionInstance
  inlined: true

```
</details>