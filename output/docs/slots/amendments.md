

# Slot: amendments 



URI: [usdm:slot/amendments](https://www.cdisc.org/usdm/slot/amendments)
Alias: amendments

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyAmendment](../classes/StudyAmendment.md) |
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
| self | usdm:amendments |
| native | usdm:amendments |




## LinkML Source

<details>
```yaml
name: amendments
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: amendments
owner: StudyVersion
domain_of:
- StudyVersion
range: StudyAmendment
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>