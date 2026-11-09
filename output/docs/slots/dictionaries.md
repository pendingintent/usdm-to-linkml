

# Slot: dictionaries 



URI: [usdm:slot/dictionaries](https://www.cdisc.org/usdm/slot/dictionaries)
Alias: dictionaries

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SyntaxTemplateDictionary](../classes/SyntaxTemplateDictionary.md) |
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
| self | usdm:dictionaries |
| native | usdm:dictionaries |




## LinkML Source

<details>
```yaml
name: dictionaries
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: dictionaries
owner: StudyVersion
domain_of:
- StudyVersion
range: SyntaxTemplateDictionary
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>