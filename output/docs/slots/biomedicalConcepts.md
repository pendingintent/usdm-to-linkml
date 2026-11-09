

# Slot: biomedicalConcepts 



URI: [usdm:slot/biomedicalConcepts](https://www.cdisc.org/usdm/slot/biomedicalConcepts)
Alias: biomedicalConcepts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomedicalConcept](../classes/BiomedicalConcept.md) |
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