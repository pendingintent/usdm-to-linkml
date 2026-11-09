

# Slot: text 



URI: [usdm:text](https://www.cdisc.org/usdm/text)
Alias: text

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Endpoint](Endpoint.md) |  |  no  |
| [EligibilityCriterionItem](EligibilityCriterionItem.md) |  |  no  |
| [AdministrableProductIdentifier](AdministrableProductIdentifier.md) |  |  no  |
| [NarrativeContentItem](NarrativeContentItem.md) |  |  no  |
| [Condition](Condition.md) |  |  no  |
| [StudyTitle](StudyTitle.md) |  |  no  |
| [CommentAnnotation](CommentAnnotation.md) |  |  no  |
| [Objective](Objective.md) |  |  no  |
| [TransitionRule](TransitionRule.md) |  |  no  |
| [AnalysisPopulation](AnalysisPopulation.md) |  |  no  |
| [Masking](Masking.md) |  |  no  |
| [StudyAmendmentImpact](StudyAmendmentImpact.md) |  |  no  |
| [Duration](Duration.md) |  |  no  |
| [Address](Address.md) |  |  no  |
| [MedicalDeviceIdentifier](MedicalDeviceIdentifier.md) |  |  no  |
| [StudyIdentifier](StudyIdentifier.md) |  |  no  |
| [AdministrableProductProperty](AdministrableProductProperty.md) |  |  no  |
| [ReferenceIdentifier](ReferenceIdentifier.md) |  |  no  |
| [IntercurrentEvent](IntercurrentEvent.md) |  |  no  |
| [Characteristic](Characteristic.md) |  |  no  |
| [PersonName](PersonName.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Address](Address.md), [AdministrableProductIdentifier](AdministrableProductIdentifier.md), [AdministrableProductProperty](AdministrableProductProperty.md), [AnalysisPopulation](AnalysisPopulation.md), [Characteristic](Characteristic.md), [CommentAnnotation](CommentAnnotation.md), [Condition](Condition.md), [Duration](Duration.md), [EligibilityCriterionItem](EligibilityCriterionItem.md), [Endpoint](Endpoint.md), [IntercurrentEvent](IntercurrentEvent.md), [Masking](Masking.md), [MedicalDeviceIdentifier](MedicalDeviceIdentifier.md), [NarrativeContentItem](NarrativeContentItem.md), [Objective](Objective.md), [PersonName](PersonName.md), [ReferenceIdentifier](ReferenceIdentifier.md), [StudyAmendmentImpact](StudyAmendmentImpact.md), [StudyIdentifier](StudyIdentifier.md), [StudyTitle](StudyTitle.md), [TransitionRule](TransitionRule.md) |

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