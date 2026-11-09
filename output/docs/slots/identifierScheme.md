

# Slot: identifierScheme 



URI: [usdm:slot/identifierScheme](https://www.cdisc.org/usdm/slot/identifierScheme)
Alias: identifierScheme

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](../classes/Organization.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Organization](../classes/Organization.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Organization](../classes/Organization.md) |












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