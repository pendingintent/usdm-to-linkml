

# Slot: memberIds 



URI: [usdm:memberIds](https://www.cdisc.org/usdm/memberIds)
Alias: memberIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConceptCategory](BiomedicalConceptCategory.md) |












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