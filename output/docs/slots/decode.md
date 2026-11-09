

# Slot: decode 



URI: [usdm:slot/decode](https://www.cdisc.org/usdm/slot/decode)
Alias: decode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Code](../classes/Code.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Code](../classes/Code.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Code](../classes/Code.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:decode |
| native | usdm:decode |




## LinkML Source

<details>
```yaml
name: decode
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: decode
owner: Code
domain_of:
- Code
range: string
required: true

```
</details>