

# Slot: administrableDoseForm 



URI: [usdm:slot/administrableDoseForm](https://www.cdisc.org/usdm/slot/administrableDoseForm)
Alias: administrableDoseForm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrableProduct](../classes/AdministrableProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AliasCode](../classes/AliasCode.md) |
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
| self | usdm:administrableDoseForm |
| native | usdm:administrableDoseForm |




## LinkML Source

<details>
```yaml
name: administrableDoseForm
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: administrableDoseForm
owner: AdministrableProduct
domain_of:
- AdministrableProduct
range: AliasCode
required: true
inlined: true

```
</details>