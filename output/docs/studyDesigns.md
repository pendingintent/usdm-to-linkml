

# Slot: studyDesigns 



URI: [usdm:studyDesigns](https://www.cdisc.org/usdm/studyDesigns)
Alias: studyDesigns

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [InterventionalStudyDesign](InterventionalStudyDesign.md)&nbsp;or&nbsp;<br />[Any](Any.md)&nbsp;or&nbsp;<br />[ObservationalStudyDesign](ObservationalStudyDesign.md) |
| Domain Of | [StudyVersion](StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](StudyVersion.md) |


<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'InterventionalStudyDesign', 'inlined': True})
- AnonymousSlotExpression({'range': 'ObservationalStudyDesign', 'inlined': True})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:studyDesigns |
| native | usdm:studyDesigns |




## LinkML Source

<details>
```yaml
name: studyDesigns
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: studyDesigns
owner: StudyVersion
domain_of:
- StudyVersion
range: Any
required: false
multivalued: true
inlined: true
inlined_as_list: true
any_of:
- range: InterventionalStudyDesign
  inlined: true
- range: ObservationalStudyDesign
  inlined: true

```
</details>