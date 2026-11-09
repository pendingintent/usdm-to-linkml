

# Slot: ingredients 



URI: [usdm:slot/ingredients](https://www.cdisc.org/usdm/slot/ingredients)
Alias: ingredients

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrableProduct](../classes/AdministrableProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ingredient](../classes/Ingredient.md) |
| Domain Of | [AdministrableProduct](../classes/AdministrableProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrableProduct](../classes/AdministrableProduct.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:ingredients |
| native | usdm:ingredients |




## LinkML Source

<details>
```yaml
name: ingredients
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: ingredients
owner: AdministrableProduct
domain_of:
- AdministrableProduct
range: Ingredient
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>