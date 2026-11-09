

# Slot: changes 



URI: [usdm:slot/changes](https://www.cdisc.org/usdm/slot/changes)
Alias: changes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendment](../classes/StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyChange](../classes/StudyChange.md) |
| Domain Of | [StudyAmendment](../classes/StudyAmendment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyAmendment](../classes/StudyAmendment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:changes |
| native | usdm:changes |




## LinkML Source

<details>
```yaml
name: changes
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: changes
owner: StudyAmendment
domain_of:
- StudyAmendment
range: StudyChange
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>