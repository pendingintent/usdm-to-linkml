

# Slot: contents 



URI: [usdm:contents](https://www.cdisc.org/usdm/contents)
Alias: contents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](StudyDefinitionDocumentVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NarrativeContent](NarrativeContent.md) |
| Domain Of | [StudyDefinitionDocumentVersion](StudyDefinitionDocumentVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDefinitionDocumentVersion](StudyDefinitionDocumentVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:contents |
| native | usdm:contents |




## LinkML Source

<details>
```yaml
name: contents
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: contents
owner: StudyDefinitionDocumentVersion
domain_of:
- StudyDefinitionDocumentVersion
range: NarrativeContent
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>