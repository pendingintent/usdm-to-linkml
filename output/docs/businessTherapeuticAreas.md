

# Slot: businessTherapeuticAreas 



URI: [usdm:businessTherapeuticAreas](https://www.cdisc.org/usdm/businessTherapeuticAreas)
Alias: businessTherapeuticAreas

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
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
| self | usdm:businessTherapeuticAreas |
| native | usdm:businessTherapeuticAreas |




## LinkML Source

<details>
```yaml
name: businessTherapeuticAreas
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: businessTherapeuticAreas
owner: StudyVersion
domain_of:
- StudyVersion
range: Code
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>