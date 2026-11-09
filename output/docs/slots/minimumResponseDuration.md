

# Slot: minimumResponseDuration 



URI: [usdm:slot/minimumResponseDuration](https://www.cdisc.org/usdm/slot/minimumResponseDuration)
Alias: minimumResponseDuration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyIntervention](../classes/StudyIntervention.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Quantity](../classes/Quantity.md) |
| Domain Of | [StudyIntervention](../classes/StudyIntervention.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyIntervention](../classes/StudyIntervention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:minimumResponseDuration |
| native | usdm:minimumResponseDuration |




## LinkML Source

<details>
```yaml
name: minimumResponseDuration
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: minimumResponseDuration
owner: StudyIntervention
domain_of:
- StudyIntervention
range: Quantity
required: false
inlined: true

```
</details>