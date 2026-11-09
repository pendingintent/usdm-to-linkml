

# Slot: encounterId 



URI: [usdm:slot/encounterId](https://www.cdisc.org/usdm/slot/encounterId)
Alias: encounterId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduledActivityInstance](../classes/ScheduledActivityInstance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [ScheduledActivityInstance](../classes/ScheduledActivityInstance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduledActivityInstance](../classes/ScheduledActivityInstance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:encounterId |
| native | usdm:encounterId |




## LinkML Source

<details>
```yaml
name: encounterId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: encounterId
owner: ScheduledActivityInstance
domain_of:
- ScheduledActivityInstance
range: string
required: false

```
</details>