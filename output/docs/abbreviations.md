

# Slot: abbreviations 



URI: [usdm:abbreviations](https://www.cdisc.org/usdm/abbreviations)
Alias: abbreviations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Abbreviation](Abbreviation.md) |
| Domain Of | [StudyVersion](StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | usdm:abbreviations |
| native | usdm:abbreviations |




## LinkML Source

<details>
```yaml
name: abbreviations
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: abbreviations
owner: StudyVersion
domain_of:
- StudyVersion
range: Abbreviation
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>