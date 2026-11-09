

# Slot: previousId 



URI: [usdm:previousId](https://www.cdisc.org/usdm/previousId)
Alias: previousId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) |  |  no  |
| [NarrativeContent](NarrativeContent.md) |  |  no  |
| [Activity](Activity.md) |  |  no  |
| [StudyAmendment](StudyAmendment.md) |  |  no  |
| [StudyEpoch](StudyEpoch.md) |  |  no  |
| [EligibilityCriterion](EligibilityCriterion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Activity](Activity.md), [EligibilityCriterion](EligibilityCriterion.md), [Encounter](Encounter.md), [NarrativeContent](NarrativeContent.md), [StudyAmendment](StudyAmendment.md), [StudyEpoch](StudyEpoch.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:previousId |
| native | usdm:previousId |




## LinkML Source

<details>
```yaml
name: previousId
alias: previousId
domain_of:
- Activity
- EligibilityCriterion
- Encounter
- NarrativeContent
- StudyAmendment
- StudyEpoch
range: string

```
</details>