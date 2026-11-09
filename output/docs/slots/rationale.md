

# Slot: rationale 



URI: [usdm:slot/rationale](https://www.cdisc.org/usdm/slot/rationale)
Alias: rationale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionalStudyDesign](../classes/InterventionalStudyDesign.md) |  |  no  |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |
| [StudyChange](../classes/StudyChange.md) |  |  no  |
| [ObservationalStudyDesign](../classes/ObservationalStudyDesign.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [InterventionalStudyDesign](../classes/InterventionalStudyDesign.md), [ObservationalStudyDesign](../classes/ObservationalStudyDesign.md), [StudyChange](../classes/StudyChange.md), [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:rationale |
| native | usdm:rationale |




## LinkML Source

<details>
```yaml
name: rationale
alias: rationale
domain_of:
- InterventionalStudyDesign
- ObservationalStudyDesign
- StudyChange
- StudyVersion
range: string

```
</details>