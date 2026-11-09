

# Slot: language 



URI: [usdm:language](https://www.cdisc.org/usdm/language)
Alias: language

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDefinitionDocument](StudyDefinitionDocument.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
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
| self | usdm:language |
| native | usdm:language |




## LinkML Source

<details>
```yaml
name: language
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: language
owner: StudyDefinitionDocument
domain_of:
- StudyDefinitionDocument
range: Code
required: true
inlined: true

```
</details>