

# Slot: administrableDoseForm 



URI: [usdm:administrableDoseForm](https://www.cdisc.org/usdm/administrableDoseForm)
Alias: administrableDoseForm

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AdministrableProduct](AdministrableProduct.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AliasCode](AliasCode.md) |
| Domain Of | [AdministrableProduct](AdministrableProduct.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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