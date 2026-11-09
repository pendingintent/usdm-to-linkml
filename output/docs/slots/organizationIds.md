

# Slot: organizationIds 



URI: [usdm:slot/organizationIds](https://www.cdisc.org/usdm/slot/organizationIds)
Alias: organizationIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyRole](../classes/StudyRole.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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
| self | usdm:organizationIds |
| native | usdm:organizationIds |




## LinkML Source

<details>
```yaml
name: organizationIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: organizationIds
owner: StudyRole
domain_of:
- StudyRole
range: string
required: false
multivalued: true

```
</details>