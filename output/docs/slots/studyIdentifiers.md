

# Slot: studyIdentifiers 



URI: [usdm:slot/studyIdentifiers](https://www.cdisc.org/usdm/slot/studyIdentifiers)
Alias: studyIdentifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyIdentifier](../classes/StudyIdentifier.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | usdm:studyIdentifiers |
| native | usdm:studyIdentifiers |




## LinkML Source

<details>
```yaml
name: studyIdentifiers
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: studyIdentifiers
owner: StudyVersion
domain_of:
- StudyVersion
range: StudyIdentifier
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>