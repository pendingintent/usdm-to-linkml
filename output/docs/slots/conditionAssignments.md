

# Slot: conditionAssignments 



URI: [usdm:slot/conditionAssignments](https://www.cdisc.org/usdm/slot/conditionAssignments)
Alias: conditionAssignments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConditionAssignment](../classes/ConditionAssignment.md) |
| Domain Of | [ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduledDecisionInstance](../classes/ScheduledDecisionInstance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:conditionAssignments |
| native | usdm:conditionAssignments |




## LinkML Source

<details>
```yaml
name: conditionAssignments
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: conditionAssignments
owner: ScheduledDecisionInstance
domain_of:
- ScheduledDecisionInstance
range: ConditionAssignment
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>