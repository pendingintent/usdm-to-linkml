

# Slot: administrableProducts 



URI: [usdm:administrableProducts](https://www.cdisc.org/usdm/administrableProducts)
Alias: administrableProducts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AdministrableProduct](AdministrableProduct.md) |
| Domain Of | [StudyVersion](StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:administrableProducts |
| native | usdm:administrableProducts |




## LinkML Source

<details>
```yaml
name: administrableProducts
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: administrableProducts
owner: StudyVersion
domain_of:
- StudyVersion
range: AdministrableProduct
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>