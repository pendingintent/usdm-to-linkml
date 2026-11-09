

# Slot: state 



URI: [usdm:slot/state](https://www.cdisc.org/usdm/slot/state)
Alias: state

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
| self | usdm:state |
| native | usdm:state |




## LinkML Source

<details>
```yaml
name: state
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: state
owner: Address
domain_of:
- Address
range: string
required: false

```
</details>