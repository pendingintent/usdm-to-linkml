

# Slot: populationSummary 



URI: [usdm:slot/populationSummary](https://www.cdisc.org/usdm/slot/populationSummary)
Alias: populationSummary

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Estimand](../classes/Estimand.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Estimand](../classes/Estimand.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Estimand](../classes/Estimand.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:populationSummary |
| native | usdm:populationSummary |




## LinkML Source

<details>
```yaml
name: populationSummary
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: populationSummary
owner: Estimand
domain_of:
- Estimand
range: string
required: true

```
</details>