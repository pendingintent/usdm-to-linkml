

# Slot: legalAddress 



URI: [usdm:slot/legalAddress](https://www.cdisc.org/usdm/slot/legalAddress)
Alias: legalAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](../classes/Organization.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Address](../classes/Address.md) |
| Domain Of | [Organization](../classes/Organization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
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
| self | usdm:legalAddress |
| native | usdm:legalAddress |




## LinkML Source

<details>
```yaml
name: legalAddress
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: legalAddress
owner: Organization
domain_of:
- Organization
range: Address
required: false
inlined: true

```
</details>