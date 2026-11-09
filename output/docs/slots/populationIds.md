

# Slot: populationIds 



URI: [usdm:slot/populationIds](https://www.cdisc.org/usdm/slot/populationIds)
Alias: populationIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyArm](../classes/StudyArm.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyArm](../classes/StudyArm.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyArm](../classes/StudyArm.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:populationIds |
| native | usdm:populationIds |




## LinkML Source

<details>
```yaml
name: populationIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: populationIds
owner: StudyArm
domain_of:
- StudyArm
range: string
required: false
multivalued: true

```
</details>