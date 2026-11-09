

# Slot: standardCodeAliases 



URI: [usdm:slot/standardCodeAliases](https://www.cdisc.org/usdm/slot/standardCodeAliases)
Alias: standardCodeAliases

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AliasCode](../classes/AliasCode.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
| Domain Of | [AliasCode](../classes/AliasCode.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AliasCode](../classes/AliasCode.md) |












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