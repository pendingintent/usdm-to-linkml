

# Slot: changedSections 



URI: [usdm:changedSections](https://www.cdisc.org/usdm/changedSections)
Alias: changedSections

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyChange](StudyChange.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DocumentContentReference](DocumentContentReference.md) |
| Domain Of | [StudyChange](StudyChange.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyChange](StudyChange.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:changedSections |
| native | usdm:changedSections |




## LinkML Source

<details>
```yaml
name: changedSections
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: changedSections
owner: StudyChange
domain_of:
- StudyChange
range: DocumentContentReference
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>