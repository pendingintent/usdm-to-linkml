

# Slot: childIds 



URI: [usdm:childIds](https://www.cdisc.org/usdm/childIds)
Alias: childIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocument](StudyDefinitionDocument.md) |  |  no  |
| [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |  |  no  |
| [Activity](Activity.md) |  |  no  |
| [NarrativeContent](NarrativeContent.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Activity](Activity.md), [BiomedicalConceptCategory](BiomedicalConceptCategory.md), [NarrativeContent](NarrativeContent.md), [StudyDefinitionDocument](StudyDefinitionDocument.md) |

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