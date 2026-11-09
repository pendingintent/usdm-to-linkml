

# Slot: appliesToId 



URI: [usdm:slot/appliesToId](https://www.cdisc.org/usdm/slot/appliesToId)
Alias: appliesToId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentContentReference](../classes/DocumentContentReference.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [DocumentContentReference](../classes/DocumentContentReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DocumentContentReference](../classes/DocumentContentReference.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:appliesToId |
| native | usdm:appliesToId |




## LinkML Source

<details>
```yaml
name: appliesToId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: appliesToId
owner: DocumentContentReference
domain_of:
- DocumentContentReference
range: string
required: true

```
</details>