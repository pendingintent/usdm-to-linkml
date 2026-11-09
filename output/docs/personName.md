

# Slot: personName 



URI: [usdm:personName](https://www.cdisc.org/usdm/personName)
Alias: personName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AssignedPerson](AssignedPerson.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PersonName](PersonName.md) |
| Domain Of | [AssignedPerson](AssignedPerson.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AssignedPerson](AssignedPerson.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:personName |
| native | usdm:personName |




## LinkML Source

<details>
```yaml
name: personName
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: personName
owner: AssignedPerson
domain_of:
- AssignedPerson
range: PersonName
required: true
inlined: true

```
</details>