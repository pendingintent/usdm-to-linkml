

# Slot: templateName 



URI: [usdm:slot/templateName](https://www.cdisc.org/usdm/slot/templateName)
Alias: templateName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:templateName |
| native | usdm:templateName |




## LinkML Source

<details>
```yaml
name: templateName
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: templateName
owner: StudyDefinitionDocument
domain_of:
- StudyDefinitionDocument
range: string
required: true

```
</details>