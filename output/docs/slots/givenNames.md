

# Slot: givenNames 



URI: [usdm:slot/givenNames](https://www.cdisc.org/usdm/slot/givenNames)
Alias: givenNames

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
| Multivalued | Yes |
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
| self | usdm:givenNames |
| native | usdm:givenNames |




## LinkML Source

<details>
```yaml
name: givenNames
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: givenNames
owner: PersonName
domain_of:
- PersonName
range: string
required: false
multivalued: true

```
</details>