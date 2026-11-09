

# Slot: text 



URI: [usdm:slot/text](https://www.cdisc.org/usdm/slot/text)
Alias: text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Endpoint](../classes/Endpoint.md) |  |  no  |
| [EligibilityCriterionItem](../classes/EligibilityCriterionItem.md) |  |  no  |
| [AdministrableProductIdentifier](../classes/AdministrableProductIdentifier.md) |  |  no  |
| [NarrativeContentItem](../classes/NarrativeContentItem.md) |  |  no  |
| [Condition](../classes/Condition.md) |  |  no  |
| [StudyTitle](../classes/StudyTitle.md) |  |  no  |
| [CommentAnnotation](../classes/CommentAnnotation.md) |  |  no  |
| [Objective](../classes/Objective.md) |  |  no  |
| [TransitionRule](../classes/TransitionRule.md) |  |  no  |
| [AnalysisPopulation](../classes/AnalysisPopulation.md) |  |  no  |
| [Masking](../classes/Masking.md) |  |  no  |
| [StudyAmendmentImpact](../classes/StudyAmendmentImpact.md) |  |  no  |
| [Duration](../classes/Duration.md) |  |  no  |
| [Address](../classes/Address.md) |  |  no  |
| [MedicalDeviceIdentifier](../classes/MedicalDeviceIdentifier.md) |  |  no  |
| [StudyIdentifier](../classes/StudyIdentifier.md) |  |  no  |
| [AdministrableProductProperty](../classes/AdministrableProductProperty.md) |  |  no  |
| [ReferenceIdentifier](../classes/ReferenceIdentifier.md) |  |  no  |
| [IntercurrentEvent](../classes/IntercurrentEvent.md) |  |  no  |
| [Characteristic](../classes/Characteristic.md) |  |  no  |
| [PersonName](../classes/PersonName.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Address](../classes/Address.md), [AdministrableProductIdentifier](../classes/AdministrableProductIdentifier.md), [AdministrableProductProperty](../classes/AdministrableProductProperty.md), [AnalysisPopulation](../classes/AnalysisPopulation.md), [Characteristic](../classes/Characteristic.md), [CommentAnnotation](../classes/CommentAnnotation.md), [Condition](../classes/Condition.md), [Duration](../classes/Duration.md), [EligibilityCriterionItem](../classes/EligibilityCriterionItem.md), [Endpoint](../classes/Endpoint.md), [IntercurrentEvent](../classes/IntercurrentEvent.md), [Masking](../classes/Masking.md), [MedicalDeviceIdentifier](../classes/MedicalDeviceIdentifier.md), [NarrativeContentItem](../classes/NarrativeContentItem.md), [Objective](../classes/Objective.md), [PersonName](../classes/PersonName.md), [ReferenceIdentifier](../classes/ReferenceIdentifier.md), [StudyAmendmentImpact](../classes/StudyAmendmentImpact.md), [StudyIdentifier](../classes/StudyIdentifier.md), [StudyTitle](../classes/StudyTitle.md), [TransitionRule](../classes/TransitionRule.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:text |
| native | usdm:text |




## LinkML Source

<details>
```yaml
name: text
alias: text
domain_of:
- Address
- AdministrableProductIdentifier
- AdministrableProductProperty
- AnalysisPopulation
- Characteristic
- CommentAnnotation
- Condition
- Duration
- EligibilityCriterionItem
- Endpoint
- IntercurrentEvent
- Masking
- MedicalDeviceIdentifier
- NarrativeContentItem
- Objective
- PersonName
- ReferenceIdentifier
- StudyAmendmentImpact
- StudyIdentifier
- StudyTitle
- TransitionRule
range: string

```
</details>