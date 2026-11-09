

# Slot: conditionTargetId 



URI: [usdm:conditionTargetId](https://www.cdisc.org/usdm/conditionTargetId)
Alias: conditionTargetId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ConditionAssignment](ConditionAssignment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ConditionAssignment](ConditionAssignment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ConditionAssignment](ConditionAssignment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:conditionTargetId |
| native | usdm:conditionTargetId |




## LinkML Source

<details>
```yaml
name: conditionTargetId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: conditionTargetId
owner: ConditionAssignment
domain_of:
- ConditionAssignment
range: string
required: true

```
</details>