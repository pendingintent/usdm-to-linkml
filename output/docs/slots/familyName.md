

# Slot: familyName 



URI: [usdm:slot/familyName](https://www.cdisc.org/usdm/slot/familyName)
Alias: familyName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonName](../classes/PersonName.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [PersonName](../classes/PersonName.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonName](../classes/PersonName.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:familyName |
| native | usdm:familyName |




## LinkML Source

<details>
```yaml
name: familyName
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: familyName
owner: PersonName
domain_of:
- PersonName
range: string
required: false

```
</details>