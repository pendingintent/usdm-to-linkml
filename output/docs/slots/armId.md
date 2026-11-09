

# Slot: armId 



URI: [usdm:slot/armId](https://www.cdisc.org/usdm/slot/armId)
Alias: armId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyCell](../classes/StudyCell.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyCell](../classes/StudyCell.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyCell](../classes/StudyCell.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:armId |
| native | usdm:armId |




## LinkML Source

<details>
```yaml
name: armId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: armId
owner: StudyCell
domain_of:
- StudyCell
range: string
required: true

```
</details>