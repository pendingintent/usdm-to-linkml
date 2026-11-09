

# Slot: relativeToFrom 



URI: [usdm:slot/relativeToFrom](https://www.cdisc.org/usdm/slot/relativeToFrom)
Alias: relativeToFrom

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Timing](../classes/Timing.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
| Domain Of | [Timing](../classes/Timing.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Timing](../classes/Timing.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:relativeToFrom |
| native | usdm:relativeToFrom |




## LinkML Source

<details>
```yaml
name: relativeToFrom
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: relativeToFrom
owner: Timing
domain_of:
- Timing
range: Code
required: true
inlined: true

```
</details>