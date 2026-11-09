

# Slot: eligibilityCriterionItems 



URI: [usdm:slot/eligibilityCriterionItems](https://www.cdisc.org/usdm/slot/eligibilityCriterionItems)
Alias: eligibilityCriterionItems

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EligibilityCriterionItem](../classes/EligibilityCriterionItem.md) |
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
| self | usdm:eligibilityCriterionItems |
| native | usdm:eligibilityCriterionItems |




## LinkML Source

<details>
```yaml
name: eligibilityCriterionItems
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: eligibilityCriterionItems
owner: StudyVersion
domain_of:
- StudyVersion
range: EligibilityCriterionItem
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>