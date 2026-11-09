

# Slot: condition 



URI: [usdm:condition](https://www.cdisc.org/usdm/condition)
Alias: condition

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
| self | usdm:condition |
| native | usdm:condition |




## LinkML Source

<details>
```yaml
name: condition
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: condition
owner: ConditionAssignment
domain_of:
- ConditionAssignment
range: string
required: true

```
</details>