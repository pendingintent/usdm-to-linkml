

# Slot: productOrganizationRoles 



URI: [usdm:slot/productOrganizationRoles](https://www.cdisc.org/usdm/slot/productOrganizationRoles)
Alias: productOrganizationRoles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ProductOrganizationRole](../classes/ProductOrganizationRole.md) |
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
| self | usdm:productOrganizationRoles |
| native | usdm:productOrganizationRoles |




## LinkML Source

<details>
```yaml
name: productOrganizationRoles
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: productOrganizationRoles
owner: StudyVersion
domain_of:
- StudyVersion
range: ProductOrganizationRole
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>