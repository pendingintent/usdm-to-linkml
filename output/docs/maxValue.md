

# Slot: maxValue 



URI: [usdm:maxValue](https://www.cdisc.org/usdm/maxValue)
Alias: maxValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Range](Range.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Quantity](Quantity.md) |
| Domain Of | [Range](Range.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Range](Range.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:maxValue |
| native | usdm:maxValue |




## LinkML Source

<details>
```yaml
name: maxValue
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: maxValue
owner: Range
domain_of:
- Range
range: Quantity
required: true
inlined: true

```
</details>