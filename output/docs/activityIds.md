

# Slot: activityIds 



URI: [usdm:activityIds](https://www.cdisc.org/usdm/activityIds)
Alias: activityIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ScheduledActivityInstance](ScheduledActivityInstance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [ScheduledActivityInstance](ScheduledActivityInstance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [ScheduledActivityInstance](ScheduledActivityInstance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:activityIds |
| native | usdm:activityIds |




## LinkML Source

<details>
```yaml
name: activityIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: activityIds
owner: ScheduledActivityInstance
domain_of:
- ScheduledActivityInstance
range: string
required: false
multivalued: true

```
</details>