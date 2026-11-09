

# Slot: postalCode 



URI: [usdm:slot/postalCode](https://www.cdisc.org/usdm/slot/postalCode)
Alias: postalCode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](../classes/Address.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Address](../classes/Address.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Address](../classes/Address.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:postalCode |
| native | usdm:postalCode |




## LinkML Source

<details>
```yaml
name: postalCode
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: postalCode
owner: Address
domain_of:
- Address
range: string
required: false

```
</details>