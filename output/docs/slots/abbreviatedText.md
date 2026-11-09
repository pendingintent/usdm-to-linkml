

# Slot: abbreviatedText 



URI: [usdm:slot/abbreviatedText](https://www.cdisc.org/usdm/slot/abbreviatedText)
Alias: abbreviatedText

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
| self | usdm:abbreviatedText |
| native | usdm:abbreviatedText |




## LinkML Source

<details>
```yaml
name: abbreviatedText
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: abbreviatedText
owner: Abbreviation
domain_of:
- Abbreviation
range: string
required: true
pattern: ^[\s\S]+$

```
</details>