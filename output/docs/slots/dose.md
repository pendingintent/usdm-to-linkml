

# Slot: dose 



URI: [usdm:slot/dose](https://www.cdisc.org/usdm/slot/dose)
Alias: dose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Administration](../classes/Administration.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Quantity](../classes/Quantity.md) |
| Domain Of | [Administration](../classes/Administration.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Administration](../classes/Administration.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:dose |
| native | usdm:dose |




## LinkML Source

<details>
```yaml
name: dose
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: dose
owner: Administration
domain_of:
- Administration
range: Quantity
required: false
inlined: true

```
</details>