

# Slot: category 



URI: [usdm:category](https://www.cdisc.org/usdm/category)
Alias: category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EligibilityCriterion](EligibilityCriterion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
| Domain Of | [EligibilityCriterion](EligibilityCriterion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EligibilityCriterion](EligibilityCriterion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:category |
| native | usdm:category |




## LinkML Source

<details>
```yaml
name: category
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: category
owner: EligibilityCriterion
domain_of:
- EligibilityCriterion
range: Code
required: true
inlined: true

```
</details>