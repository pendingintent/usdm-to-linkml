

# Slot: biomedicalConcepts 



URI: [usdm:biomedicalConcepts](https://www.cdisc.org/usdm/biomedicalConcepts)
Alias: biomedicalConcepts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomedicalConcept](BiomedicalConcept.md) |
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
| self | usdm:biomedicalConcepts |
| native | usdm:biomedicalConcepts |




## LinkML Source

<details>
```yaml
name: biomedicalConcepts
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: biomedicalConcepts
owner: StudyVersion
domain_of:
- StudyVersion
range: BiomedicalConcept
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>