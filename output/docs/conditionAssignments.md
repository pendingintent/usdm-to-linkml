

# Slot: conditionAssignments 



URI: [usdm:conditionAssignments](https://www.cdisc.org/usdm/conditionAssignments)
Alias: conditionAssignments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduledDecisionInstance](ScheduledDecisionInstance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ConditionAssignment](ConditionAssignment.md) |
| Domain Of | [ScheduledDecisionInstance](ScheduledDecisionInstance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduledDecisionInstance](ScheduledDecisionInstance.md) |












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