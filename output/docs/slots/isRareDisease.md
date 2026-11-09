

# Slot: isRareDisease 



URI: [usdm:slot/isRareDisease](https://www.cdisc.org/usdm/slot/isRareDisease)
Alias: isRareDisease

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Indication](../classes/Indication.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [Indication](../classes/Indication.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Indication](../classes/Indication.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:isRareDisease |
| native | usdm:isRareDisease |




## LinkML Source

<details>
```yaml
name: isRareDisease
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: isRareDisease
owner: Indication
domain_of:
- Indication
range: boolean
required: true

```
</details>