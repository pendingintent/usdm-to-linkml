

# Slot: nextId 



URI: [usdm:slot/nextId](https://www.cdisc.org/usdm/slot/nextId)
Alias: nextId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](../classes/Encounter.md) |  |  no  |
| [NarrativeContent](../classes/NarrativeContent.md) |  |  no  |
| [Activity](../classes/Activity.md) |  |  no  |
| [StudyEpoch](../classes/StudyEpoch.md) |  |  no  |
| [EligibilityCriterion](../classes/EligibilityCriterion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Activity](../classes/Activity.md), [EligibilityCriterion](../classes/EligibilityCriterion.md), [Encounter](../classes/Encounter.md), [NarrativeContent](../classes/NarrativeContent.md), [StudyEpoch](../classes/StudyEpoch.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:nextId |
| native | usdm:nextId |




## LinkML Source

<details>
```yaml
name: nextId
alias: nextId
domain_of:
- Activity
- EligibilityCriterion
- Encounter
- NarrativeContent
- StudyEpoch
range: string

```
</details>