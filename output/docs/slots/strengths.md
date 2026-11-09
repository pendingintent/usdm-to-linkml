

# Slot: strengths 



URI: [usdm:slot/strengths](https://www.cdisc.org/usdm/slot/strengths)
Alias: strengths

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Substance](../classes/Substance.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Strength](../classes/Strength.md) |
| Domain Of | [Substance](../classes/Substance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Substance](../classes/Substance.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:strengths |
| native | usdm:strengths |




## LinkML Source

<details>
```yaml
name: strengths
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: strengths
owner: Substance
domain_of:
- Substance
range: Strength
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>