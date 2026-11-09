

# Slot: narrativeContentItems 



URI: [usdm:slot/narrativeContentItems](https://www.cdisc.org/usdm/slot/narrativeContentItems)
Alias: narrativeContentItems

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NarrativeContentItem](../classes/NarrativeContentItem.md) |
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
| self | usdm:narrativeContentItems |
| native | usdm:narrativeContentItems |




## LinkML Source

<details>
```yaml
name: narrativeContentItems
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: narrativeContentItems
owner: StudyVersion
domain_of:
- StudyVersion
range: NarrativeContentItem
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>