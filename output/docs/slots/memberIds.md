

# Slot: memberIds 



URI: [usdm:slot/memberIds](https://www.cdisc.org/usdm/slot/memberIds)
Alias: memberIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:memberIds |
| native | usdm:memberIds |




## LinkML Source

<details>
```yaml
name: memberIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: memberIds
owner: BiomedicalConceptCategory
domain_of:
- BiomedicalConceptCategory
range: string
required: false
multivalued: true

```
</details>