

# Slot: titles 



URI: [usdm:slot/titles](https://www.cdisc.org/usdm/slot/titles)
Alias: titles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyTitle](../classes/StudyTitle.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](../classes/StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:titles |
| native | usdm:titles |




## LinkML Source

<details>
```yaml
name: titles
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: titles
owner: StudyVersion
domain_of:
- StudyVersion
range: StudyTitle
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>