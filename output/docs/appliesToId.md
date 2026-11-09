

# Slot: appliesToId 



URI: [usdm:appliesToId](https://www.cdisc.org/usdm/appliesToId)
Alias: appliesToId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentContentReference](DocumentContentReference.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DocumentContentReference](DocumentContentReference.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [DocumentContentReference](DocumentContentReference.md) |












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