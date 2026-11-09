

# Slot: templateName 



URI: [usdm:templateName](https://www.cdisc.org/usdm/templateName)
Alias: templateName

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocument](StudyDefinitionDocument.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyDefinitionDocument](StudyDefinitionDocument.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDefinitionDocument](StudyDefinitionDocument.md) |












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