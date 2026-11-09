

# Slot: isRetained 



URI: [usdm:isRetained](https://www.cdisc.org/usdm/isRetained)
Alias: isRetained

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenRetention](BiospecimenRetention.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](Boolean.md) |
| Domain Of | [BiospecimenRetention](BiospecimenRetention.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiospecimenRetention](BiospecimenRetention.md) |












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