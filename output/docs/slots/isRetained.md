

# Slot: isRetained 



URI: [usdm:slot/isRetained](https://www.cdisc.org/usdm/slot/isRetained)
Alias: isRetained

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenRetention](../classes/BiospecimenRetention.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [BiospecimenRetention](../classes/BiospecimenRetention.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiospecimenRetention](../classes/BiospecimenRetention.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:isRetained |
| native | usdm:isRetained |




## LinkML Source

<details>
```yaml
name: isRetained
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: isRetained
owner: BiospecimenRetention
domain_of:
- BiospecimenRetention
range: boolean
required: true

```
</details>