

# Slot: assignedPersons 



URI: [usdm:slot/assignedPersons](https://www.cdisc.org/usdm/slot/assignedPersons)
Alias: assignedPersons

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyRole](../classes/StudyRole.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AssignedPerson](../classes/AssignedPerson.md) |
| Domain Of | [StudyRole](../classes/StudyRole.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyRole](../classes/StudyRole.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:assignedPersons |
| native | usdm:assignedPersons |




## LinkML Source

<details>
```yaml
name: assignedPersons
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: assignedPersons
owner: StudyRole
domain_of:
- StudyRole
range: AssignedPerson
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>