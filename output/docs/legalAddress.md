

# Slot: legalAddress 



URI: [usdm:legalAddress](https://www.cdisc.org/usdm/legalAddress)
Alias: legalAddress

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Address](Address.md) |
| Domain Of | [Organization](Organization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organization](Organization.md) |












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