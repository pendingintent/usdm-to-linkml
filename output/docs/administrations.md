

# Slot: administrations 



URI: [usdm:administrations](https://www.cdisc.org/usdm/administrations)
Alias: administrations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyIntervention](StudyIntervention.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Administration](Administration.md) |
| Domain Of | [StudyIntervention](StudyIntervention.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyIntervention](StudyIntervention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:administrations |
| native | usdm:administrations |




## LinkML Source

<details>
```yaml
name: administrations
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: administrations
owner: StudyIntervention
domain_of:
- StudyIntervention
range: Administration
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>