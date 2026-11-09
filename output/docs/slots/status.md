

# Slot: status 



URI: [usdm:slot/status](https://www.cdisc.org/usdm/slot/status)
Alias: status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocumentVersion](../classes/StudyDefinitionDocumentVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
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
| self | usdm:status |
| native | usdm:status |




## LinkML Source

<details>
```yaml
name: status
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: status
owner: StudyDefinitionDocumentVersion
domain_of:
- StudyDefinitionDocumentVersion
range: Code
required: true
inlined: true

```
</details>