

# Slot: nextId 



URI: [usdm:nextId](https://www.cdisc.org/usdm/nextId)
Alias: nextId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) |  |  no  |
| [NarrativeContent](NarrativeContent.md) |  |  no  |
| [Activity](Activity.md) |  |  no  |
| [StudyEpoch](StudyEpoch.md) |  |  no  |
| [EligibilityCriterion](EligibilityCriterion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Activity](Activity.md), [EligibilityCriterion](EligibilityCriterion.md), [Encounter](Encounter.md), [NarrativeContent](NarrativeContent.md), [StudyEpoch](StudyEpoch.md) |

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