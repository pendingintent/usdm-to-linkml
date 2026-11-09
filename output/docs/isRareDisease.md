

# Slot: isRareDisease 



URI: [usdm:isRareDisease](https://www.cdisc.org/usdm/isRareDisease)
Alias: isRareDisease

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Indication](Indication.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [Indication](Indication.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Indication](Indication.md) |












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