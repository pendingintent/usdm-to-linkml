

# Slot: organizations 



URI: [usdm:organizations](https://www.cdisc.org/usdm/organizations)
Alias: organizations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Organization](Organization.md) |
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
| self | usdm:organizations |
| native | usdm:organizations |




## LinkML Source

<details>
```yaml
name: organizations
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: organizations
owner: StudyVersion
domain_of:
- StudyVersion
range: Organization
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>