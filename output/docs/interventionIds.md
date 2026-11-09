

# Slot: interventionIds 



URI: [usdm:interventionIds](https://www.cdisc.org/usdm/interventionIds)
Alias: interventionIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Estimand](Estimand.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Estimand](Estimand.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Estimand](Estimand.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:interventionIds |
| native | usdm:interventionIds |




## LinkML Source

<details>
```yaml
name: interventionIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: interventionIds
owner: Estimand
domain_of:
- Estimand
range: string
required: true
multivalued: true

```
</details>