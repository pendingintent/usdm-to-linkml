

# Slot: lines 



URI: [usdm:slot/lines](https://www.cdisc.org/usdm/slot/lines)
Alias: lines

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
| Multivalued | Yes |
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
| self | usdm:lines |
| native | usdm:lines |




## LinkML Source

<details>
```yaml
name: lines
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: lines
owner: Address
domain_of:
- Address
range: string
required: false
multivalued: true

```
</details>