

# Slot: city 



URI: [usdm:city](https://www.cdisc.org/usdm/city)
Alias: city

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Address](Address.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Address](Address.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Address](Address.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:city |
| native | usdm:city |




## LinkML Source

<details>
```yaml
name: city
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: city
owner: Address
domain_of:
- Address
range: string
required: false

```
</details>