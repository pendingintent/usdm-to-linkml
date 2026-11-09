

# Slot: expandedText 



URI: [usdm:slot/expandedText](https://www.cdisc.org/usdm/slot/expandedText)
Alias: expandedText

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Abbreviation](../classes/Abbreviation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Abbreviation](../classes/Abbreviation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Abbreviation](../classes/Abbreviation.md) |


### Value Constraints

| Property | Value |
| --- | --- |
| Regex Pattern | `^[\s\S]+$` |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:expandedText |
| native | usdm:expandedText |




## LinkML Source

<details>
```yaml
name: expandedText
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: expandedText
owner: Abbreviation
domain_of:
- Abbreviation
range: string
required: true
pattern: ^[\s\S]+$

```
</details>