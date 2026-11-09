

# Slot: jobTitle 



URI: [usdm:slot/jobTitle](https://www.cdisc.org/usdm/slot/jobTitle)
Alias: jobTitle

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssignedPerson](../classes/AssignedPerson.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AssignedPerson](../classes/AssignedPerson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AssignedPerson](../classes/AssignedPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:jobTitle |
| native | usdm:jobTitle |




## LinkML Source

<details>
```yaml
name: jobTitle
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: jobTitle
owner: AssignedPerson
domain_of:
- AssignedPerson
range: string
required: true

```
</details>