

# Slot: enrollments 



URI: [usdm:enrollments](https://www.cdisc.org/usdm/enrollments)
Alias: enrollments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendment](StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SubjectEnrollment](SubjectEnrollment.md) |
| Domain Of | [StudyAmendment](StudyAmendment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyAmendment](StudyAmendment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:enrollments |
| native | usdm:enrollments |




## LinkML Source

<details>
```yaml
name: enrollments
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: enrollments
owner: StudyAmendment
domain_of:
- StudyAmendment
range: SubjectEnrollment
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>