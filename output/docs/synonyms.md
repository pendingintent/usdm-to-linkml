

# Slot: synonyms 



URI: [usdm:synonyms](https://www.cdisc.org/usdm/synonyms)
Alias: synonyms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConcept](BiomedicalConcept.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiomedicalConcept](BiomedicalConcept.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConcept](BiomedicalConcept.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:synonyms |
| native | usdm:synonyms |




## LinkML Source

<details>
```yaml
name: synonyms
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: synonyms
owner: BiomedicalConcept
domain_of:
- BiomedicalConcept
range: string
required: false
multivalued: true

```
</details>