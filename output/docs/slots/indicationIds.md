

# Slot: indicationIds 



URI: [usdm:slot/indicationIds](https://www.cdisc.org/usdm/slot/indicationIds)
Alias: indicationIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyCohort](../classes/StudyCohort.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyCohort](../classes/StudyCohort.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyCohort](../classes/StudyCohort.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:indicationIds |
| native | usdm:indicationIds |




## LinkML Source

<details>
```yaml
name: indicationIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: indicationIds
owner: StudyCohort
domain_of:
- StudyCohort
range: string
required: false
multivalued: true

```
</details>