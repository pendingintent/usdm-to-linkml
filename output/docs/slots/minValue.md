

# Slot: minValue 



URI: [usdm:slot/minValue](https://www.cdisc.org/usdm/slot/minValue)
Alias: minValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Range](../classes/Range.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Quantity](../classes/Quantity.md) |
| Domain Of | [Range](../classes/Range.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Range](../classes/Range.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:minValue |
| native | usdm:minValue |




## LinkML Source

<details>
```yaml
name: minValue
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: minValue
owner: Range
domain_of:
- Range
range: Quantity
required: true
inlined: true

```
</details>