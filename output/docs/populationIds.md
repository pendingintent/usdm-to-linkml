

# Slot: populationIds 



URI: [usdm:populationIds](https://www.cdisc.org/usdm/populationIds)
Alias: populationIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyArm](StudyArm.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyArm](StudyArm.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyArm](StudyArm.md) |












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