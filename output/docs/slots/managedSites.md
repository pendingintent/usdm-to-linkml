

# Slot: managedSites 



URI: [usdm:slot/managedSites](https://www.cdisc.org/usdm/slot/managedSites)
Alias: managedSites

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](../classes/Organization.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudySite](../classes/StudySite.md) |
| Domain Of | [Organization](../classes/Organization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organization](../classes/Organization.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:managedSites |
| native | usdm:managedSites |




## LinkML Source

<details>
```yaml
name: managedSites
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: managedSites
owner: Organization
domain_of:
- Organization
range: StudySite
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>