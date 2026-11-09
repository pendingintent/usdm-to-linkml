

# Slot: scheduledAtId 



URI: [usdm:slot/scheduledAtId](https://www.cdisc.org/usdm/slot/scheduledAtId)
Alias: scheduledAtId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](../classes/Encounter.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Encounter](../classes/Encounter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Encounter](../classes/Encounter.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:scheduledAtId |
| native | usdm:scheduledAtId |




## LinkML Source

<details>
```yaml
name: scheduledAtId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: scheduledAtId
owner: Encounter
domain_of:
- Encounter
range: string
required: false

```
</details>