

# Slot: numerator 



URI: [usdm:slot/numerator](https://www.cdisc.org/usdm/slot/numerator)
Alias: numerator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Strength](../classes/Strength.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Any](../classes/Any.md)&nbsp;or&nbsp;<br />[Range](../classes/Range.md)&nbsp;or&nbsp;<br />[Quantity](../classes/Quantity.md) |
| Domain Of | [Strength](../classes/Strength.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Strength](../classes/Strength.md) |


<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'Quantity', 'inlined': True})
- AnonymousSlotExpression({'range': 'Range', 'inlined': True})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:numerator |
| native | usdm:numerator |




## LinkML Source

<details>
```yaml
name: numerator
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: numerator
owner: Strength
domain_of:
- Strength
range: Any
required: true
inlined: true
any_of:
- range: Quantity
  inlined: true
- range: Range
  inlined: true

```
</details>