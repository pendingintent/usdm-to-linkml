

# Slot: roles 



URI: [usdm:roles](https://www.cdisc.org/usdm/roles)
Alias: roles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyRole](StudyRole.md) |
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
| self | usdm:roles |
| native | usdm:roles |




## LinkML Source

<details>
```yaml
name: roles
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: roles
owner: StudyVersion
domain_of:
- StudyVersion
range: StudyRole
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>