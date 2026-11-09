

# Slot: duration 



URI: [usdm:slot/duration](https://www.cdisc.org/usdm/slot/duration)
Alias: duration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Administration](../classes/Administration.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Duration](../classes/Duration.md) |
| Domain Of | [Administration](../classes/Administration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Administration](../classes/Administration.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:duration |
| native | usdm:duration |




## LinkML Source

<details>
```yaml
name: duration
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: duration
owner: Administration
domain_of:
- Administration
range: Duration
required: true
inlined: true

```
</details>