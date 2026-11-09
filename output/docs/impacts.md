

# Slot: impacts 



URI: [usdm:impacts](https://www.cdisc.org/usdm/impacts)
Alias: impacts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendment](StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyAmendmentImpact](StudyAmendmentImpact.md) |
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
| self | usdm:impacts |
| native | usdm:impacts |




## LinkML Source

<details>
```yaml
name: impacts
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: impacts
owner: StudyAmendment
domain_of:
- StudyAmendment
range: StudyAmendmentImpact
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>