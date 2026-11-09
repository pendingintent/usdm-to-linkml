

# Slot: abbreviations 



URI: [usdm:slot/abbreviations](https://www.cdisc.org/usdm/slot/abbreviations)
Alias: abbreviations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Abbreviation](../classes/Abbreviation.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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