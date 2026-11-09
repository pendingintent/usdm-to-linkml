

# Slot: suffixes 



URI: [usdm:suffixes](https://www.cdisc.org/usdm/suffixes)
Alias: suffixes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonName](PersonName.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [PersonName](PersonName.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonName](PersonName.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:suffixes |
| native | usdm:suffixes |




## LinkML Source

<details>
```yaml
name: suffixes
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: suffixes
owner: PersonName
domain_of:
- PersonName
range: string
required: false
multivalued: true

```
</details>