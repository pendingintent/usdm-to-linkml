

# Slot: titles 



URI: [usdm:titles](https://www.cdisc.org/usdm/titles)
Alias: titles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyTitle](StudyTitle.md) |
| Domain Of | [StudyVersion](StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](StudyVersion.md) |












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