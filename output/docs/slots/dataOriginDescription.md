

# Slot: dataOriginDescription 



URI: [usdm:slot/dataOriginDescription](https://www.cdisc.org/usdm/slot/dataOriginDescription)
Alias: dataOriginDescription

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
| Required | Yes |
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
| self | usdm:dataOriginDescription |
| native | usdm:dataOriginDescription |




## LinkML Source

<details>
```yaml
name: dataOriginDescription
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: dataOriginDescription
owner: StudyArm
domain_of:
- StudyArm
range: string
required: true

```
</details>