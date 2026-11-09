

# Slot: contextIds 



URI: [usdm:slot/contextIds](https://www.cdisc.org/usdm/slot/contextIds)
Alias: contextIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Condition](../classes/Condition.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Condition](../classes/Condition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Condition](../classes/Condition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:contextIds |
| native | usdm:contextIds |




## LinkML Source

<details>
```yaml
name: contextIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: contextIds
owner: Condition
domain_of:
- Condition
range: string
required: false
multivalued: true

```
</details>