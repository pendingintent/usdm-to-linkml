

# Slot: studyInterventions 



URI: [usdm:slot/studyInterventions](https://www.cdisc.org/usdm/slot/studyInterventions)
Alias: studyInterventions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyIntervention](../classes/StudyIntervention.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](../classes/StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:studyInterventions |
| native | usdm:studyInterventions |




## LinkML Source

<details>
```yaml
name: studyInterventions
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: studyInterventions
owner: StudyVersion
domain_of:
- StudyVersion
range: StudyIntervention
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>