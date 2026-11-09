

# Slot: standardCode 



URI: [usdm:standardCode](https://www.cdisc.org/usdm/standardCode)
Alias: standardCode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AliasCode](AliasCode.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
| Domain Of | [AliasCode](AliasCode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AliasCode](AliasCode.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:standardCode |
| native | usdm:standardCode |




## LinkML Source

<details>
```yaml
name: standardCode
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: standardCode
owner: AliasCode
domain_of:
- AliasCode
range: Code
required: true
inlined: true

```
</details>