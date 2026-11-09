

# Slot: contents 



URI: [usdm:slot/contents](https://www.cdisc.org/usdm/slot/contents)
Alias: contents

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [NarrativeContent](../classes/NarrativeContent.md) |
| Domain Of | [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |












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