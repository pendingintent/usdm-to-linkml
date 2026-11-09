

# Slot: identifierScheme 



URI: [usdm:identifierScheme](https://www.cdisc.org/usdm/identifierScheme)
Alias: identifierScheme

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Organization](Organization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organization](Organization.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:identifierScheme |
| native | usdm:identifierScheme |




## LinkML Source

<details>
```yaml
name: identifierScheme
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: identifierScheme
owner: Organization
domain_of:
- Organization
range: string
required: true

```
</details>