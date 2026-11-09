

# Slot: elementIds 



URI: [usdm:elementIds](https://www.cdisc.org/usdm/elementIds)
Alias: elementIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyCell](StudyCell.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyCell](StudyCell.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyCell](StudyCell.md) |












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