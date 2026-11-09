

# Slot: scheduledAtId 



URI: [usdm:scheduledAtId](https://www.cdisc.org/usdm/scheduledAtId)
Alias: scheduledAtId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Encounter](Encounter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Encounter](Encounter.md) |












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