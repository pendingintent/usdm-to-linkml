

# Slot: intercurrentEvents 



URI: [usdm:intercurrentEvents](https://www.cdisc.org/usdm/intercurrentEvents)
Alias: intercurrentEvents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Estimand](Estimand.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [IntercurrentEvent](IntercurrentEvent.md) |
| Domain Of | [Estimand](Estimand.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Estimand](Estimand.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:intercurrentEvents |
| native | usdm:intercurrentEvents |




## LinkML Source

<details>
```yaml
name: intercurrentEvents
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: intercurrentEvents
owner: Estimand
domain_of:
- Estimand
range: IntercurrentEvent
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>