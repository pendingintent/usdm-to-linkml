

# Slot: standardCodeAliases 



URI: [usdm:standardCodeAliases](https://www.cdisc.org/usdm/standardCodeAliases)
Alias: standardCodeAliases

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
| Multivalued | Yes |
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
| self | usdm:standardCodeAliases |
| native | usdm:standardCodeAliases |




## LinkML Source

<details>
```yaml
name: standardCodeAliases
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: standardCodeAliases
owner: AliasCode
domain_of:
- AliasCode
range: Code
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>