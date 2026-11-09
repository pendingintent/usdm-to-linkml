

# Slot: number 



URI: [usdm:number](https://www.cdisc.org/usdm/number)
Alias: number

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendment](StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyAmendment](StudyAmendment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyAmendment](StudyAmendment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:number |
| native | usdm:number |




## LinkML Source

<details>
```yaml
name: number
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: number
owner: StudyAmendment
domain_of:
- StudyAmendment
range: string
required: true

```
</details>