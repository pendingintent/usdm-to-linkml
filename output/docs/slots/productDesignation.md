

# Slot: productDesignation 



URI: [usdm:slot/productDesignation](https://www.cdisc.org/usdm/slot/productDesignation)
Alias: productDesignation

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrableProduct](../classes/AdministrableProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
| Domain Of | [AdministrableProduct](../classes/AdministrableProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | usdm:productDesignation |
| native | usdm:productDesignation |




## LinkML Source

<details>
```yaml
name: productDesignation
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: productDesignation
owner: AdministrableProduct
domain_of:
- AdministrableProduct
range: Code
required: true
inlined: true

```
</details>