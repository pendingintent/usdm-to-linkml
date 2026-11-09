

# Slot: unit 



URI: [usdm:unit](https://www.cdisc.org/usdm/unit)
Alias: unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Quantity](Quantity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AliasCode](AliasCode.md) |
| Domain Of | [Quantity](Quantity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Quantity](Quantity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:unit |
| native | usdm:unit |




## LinkML Source

<details>
```yaml
name: unit
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: unit
owner: Quantity
domain_of:
- Quantity
range: AliasCode
required: false
inlined: true

```
</details>