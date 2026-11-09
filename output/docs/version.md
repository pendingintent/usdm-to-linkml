

# Slot: version 



URI: [usdm:version](https://www.cdisc.org/usdm/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](StudyDefinitionDocumentVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyDefinitionDocumentVersion](StudyDefinitionDocumentVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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
| self | usdm:version |
| native | usdm:version |




## LinkML Source

<details>
```yaml
name: version
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: version
owner: StudyDefinitionDocumentVersion
domain_of:
- StudyDefinitionDocumentVersion
range: string
required: true

```
</details>