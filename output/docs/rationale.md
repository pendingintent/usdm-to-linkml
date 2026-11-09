

# Slot: rationale 



URI: [usdm:rationale](https://www.cdisc.org/usdm/rationale)
Alias: rationale

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionalStudyDesign](InterventionalStudyDesign.md) |  |  no  |
| [StudyVersion](StudyVersion.md) |  |  no  |
| [StudyChange](StudyChange.md) |  |  no  |
| [ObservationalStudyDesign](ObservationalStudyDesign.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [InterventionalStudyDesign](InterventionalStudyDesign.md), [ObservationalStudyDesign](ObservationalStudyDesign.md), [StudyChange](StudyChange.md), [StudyVersion](StudyVersion.md) |

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