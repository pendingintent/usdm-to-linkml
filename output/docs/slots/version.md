

# Slot: version 



URI: [usdm:slot/version](https://www.cdisc.org/usdm/slot/version)
Alias: version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
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