

# Slot: isMasked 



URI: [usdm:slot/isMasked](https://www.cdisc.org/usdm/slot/isMasked)
Alias: isMasked

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Masking](../classes/Masking.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [Masking](../classes/Masking.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Masking](../classes/Masking.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:isMasked |
| native | usdm:isMasked |




## LinkML Source

<details>
```yaml
name: isMasked
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: isMasked
owner: Masking
domain_of:
- Masking
range: boolean
required: true

```
</details>