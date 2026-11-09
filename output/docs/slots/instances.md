

# Slot: instances 



URI: [usdm:slot/instances](https://www.cdisc.org/usdm/slot/instances)
Alias: instances

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduleTimeline](../classes/ScheduleTimeline.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[ScheduledActivityInstance](../classes/ScheduledActivityInstance.md)&nbsp;or&nbsp;<br />[ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md) |
| Domain Of | [ScheduleTimeline](../classes/ScheduleTimeline.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduleTimeline](../classes/ScheduleTimeline.md) |


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