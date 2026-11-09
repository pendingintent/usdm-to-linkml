

# Slot: substance 



URI: [usdm:slot/substance](https://www.cdisc.org/usdm/slot/substance)
Alias: substance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Ingredient](../classes/Ingredient.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Substance](../classes/Substance.md) |
| Domain Of | [Ingredient](../classes/Ingredient.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Ingredient](../classes/Ingredient.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:substance |
| native | usdm:substance |




## LinkML Source

<details>
```yaml
name: substance
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: substance
owner: Ingredient
domain_of:
- Ingredient
range: Substance
required: true
inlined: true

```
</details>