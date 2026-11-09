

# Slot: previousId 



URI: [usdm:slot/previousId](https://www.cdisc.org/usdm/slot/previousId)
Alias: previousId

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](../classes/Encounter.md) |  |  no  |
| [NarrativeContent](../classes/NarrativeContent.md) |  |  no  |
| [Activity](../classes/Activity.md) |  |  no  |
| [StudyAmendment](../classes/StudyAmendment.md) |  |  no  |
| [StudyEpoch](../classes/StudyEpoch.md) |  |  no  |
| [EligibilityCriterion](../classes/EligibilityCriterion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Activity](../classes/Activity.md), [EligibilityCriterion](../classes/EligibilityCriterion.md), [Encounter](../classes/Encounter.md), [NarrativeContent](../classes/NarrativeContent.md), [StudyAmendment](../classes/StudyAmendment.md), [StudyEpoch](../classes/StudyEpoch.md) |

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