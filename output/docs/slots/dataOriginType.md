

# Slot: dataOriginType 



URI: [usdm:slot/dataOriginType](https://www.cdisc.org/usdm/slot/dataOriginType)
Alias: dataOriginType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyArm](../classes/StudyArm.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
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
| self | usdm:dataOriginType |
| native | usdm:dataOriginType |




## LinkML Source

<details>
```yaml
name: dataOriginType
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: dataOriginType
owner: StudyArm
domain_of:
- StudyArm
range: Code
required: true
inlined: true

```
</details>