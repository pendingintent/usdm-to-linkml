

# Slot: documentedBy 



URI: [usdm:slot/documentedBy](https://www.cdisc.org/usdm/slot/documentedBy)
Alias: documentedBy

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](../classes/Study.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyDefinitionDocument](../classes/StudyDefinitionDocument.md) |
| Domain Of | [Study](../classes/Study.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Study](../classes/Study.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:documentedBy |
| native | usdm:documentedBy |




## LinkML Source

<details>
```yaml
name: documentedBy
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: documentedBy
owner: Study
domain_of:
- Study
range: StudyDefinitionDocument
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>