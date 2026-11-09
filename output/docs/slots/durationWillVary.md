

# Slot: durationWillVary 



URI: [usdm:slot/durationWillVary](https://www.cdisc.org/usdm/slot/durationWillVary)
Alias: durationWillVary

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Duration](../classes/Duration.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [Duration](../classes/Duration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Duration](../classes/Duration.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:durationWillVary |
| native | usdm:durationWillVary |




## LinkML Source

<details>
```yaml
name: durationWillVary
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: durationWillVary
owner: Duration
domain_of:
- Duration
range: boolean
required: true

```
</details>