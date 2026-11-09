

# Slot: bcCategories 



URI: [usdm:bcCategories](https://www.cdisc.org/usdm/bcCategories)
Alias: bcCategories

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |
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
| self | usdm:bcCategories |
| native | usdm:bcCategories |




## LinkML Source

<details>
```yaml
name: bcCategories
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: bcCategories
owner: StudyVersion
domain_of:
- StudyVersion
range: BiomedicalConceptCategory
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>