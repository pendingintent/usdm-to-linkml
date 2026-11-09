

# Slot: ingredients 



URI: [usdm:ingredients](https://www.cdisc.org/usdm/ingredients)
Alias: ingredients

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrableProduct](AdministrableProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Ingredient](Ingredient.md) |
| Domain Of | [AdministrableProduct](AdministrableProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AdministrableProduct](AdministrableProduct.md) |












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