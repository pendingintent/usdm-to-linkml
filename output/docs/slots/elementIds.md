

# Slot: elementIds 



URI: [usdm:slot/elementIds](https://www.cdisc.org/usdm/slot/elementIds)
Alias: elementIds

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
| Multivalued | Yes |
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
| self | usdm:elementIds |
| native | usdm:elementIds |




## LinkML Source

<details>
```yaml
name: elementIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: elementIds
owner: StudyCell
domain_of:
- StudyCell
range: string
required: true
multivalued: true

```
</details>