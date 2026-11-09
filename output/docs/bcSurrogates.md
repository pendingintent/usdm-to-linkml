

# Slot: bcSurrogates 



URI: [usdm:bcSurrogates](https://www.cdisc.org/usdm/bcSurrogates)
Alias: bcSurrogates

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomedicalConceptSurrogate](BiomedicalConceptSurrogate.md) |
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
| self | usdm:bcSurrogates |
| native | usdm:bcSurrogates |




## LinkML Source

<details>
```yaml
name: bcSurrogates
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: bcSurrogates
owner: StudyVersion
domain_of:
- StudyVersion
range: BiomedicalConceptSurrogate
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>