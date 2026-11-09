

# Slot: pharmacologicClass 



URI: [usdm:slot/pharmacologicClass](https://www.cdisc.org/usdm/slot/pharmacologicClass)
Alias: pharmacologicClass

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
| self | usdm:pharmacologicClass |
| native | usdm:pharmacologicClass |




## LinkML Source

<details>
```yaml
name: pharmacologicClass
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: pharmacologicClass
owner: AdministrableProduct
domain_of:
- AdministrableProduct
range: Code
required: false
inlined: true

```
</details>