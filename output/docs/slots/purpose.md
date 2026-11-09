

# Slot: purpose 



URI: [usdm:slot/purpose](https://www.cdisc.org/usdm/slot/purpose)
Alias: purpose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Endpoint](../classes/Endpoint.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Endpoint](../classes/Endpoint.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Endpoint](../classes/Endpoint.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:purpose |
| native | usdm:purpose |




## LinkML Source

<details>
```yaml
name: purpose
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: purpose
owner: Endpoint
domain_of:
- Endpoint
range: string
required: true

```
</details>