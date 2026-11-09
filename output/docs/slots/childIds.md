

# Slot: childIds 



URI: [usdm:slot/childIds](https://www.cdisc.org/usdm/slot/childIds)
Alias: childIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |  |  no  |
| [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |  |  no  |
| [Activity](../classes/Activity.md) |  |  no  |
| [NarrativeContent](../classes/NarrativeContent.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Activity](../classes/Activity.md), [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md), [NarrativeContent](../classes/NarrativeContent.md), [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:childIds |
| native | usdm:childIds |




## LinkML Source

<details>
```yaml
name: childIds
alias: childIds
domain_of:
- Activity
- BiomedicalConceptCategory
- NarrativeContent
- StudyDefinitionDocument
range: string

```
</details>