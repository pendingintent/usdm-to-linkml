

# Slot: businessTherapeuticAreas 



URI: [usdm:slot/businessTherapeuticAreas](https://www.cdisc.org/usdm/slot/businessTherapeuticAreas)
Alias: businessTherapeuticAreas

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
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