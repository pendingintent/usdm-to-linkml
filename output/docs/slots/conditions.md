

# Slot: conditions 



URI: [usdm:slot/conditions](https://www.cdisc.org/usdm/slot/conditions)
Alias: conditions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Condition](../classes/Condition.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](../classes/StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:conditions |
| native | usdm:conditions |




## LinkML Source

<details>
```yaml
name: conditions
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: conditions
owner: StudyVersion
domain_of:
- StudyVersion
range: Condition
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>