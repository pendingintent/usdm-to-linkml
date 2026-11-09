

# Slot: subsetOfIds 



URI: [usdm:slot/subsetOfIds](https://www.cdisc.org/usdm/slot/subsetOfIds)
Alias: subsetOfIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisPopulation](../classes/AnalysisPopulation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [AnalysisPopulation](../classes/AnalysisPopulation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [AnalysisPopulation](../classes/AnalysisPopulation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:subsetOfIds |
| native | usdm:subsetOfIds |




## LinkML Source

<details>
```yaml
name: subsetOfIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: subsetOfIds
owner: AnalysisPopulation
domain_of:
- AnalysisPopulation
range: string
required: false
multivalued: true

```
</details>