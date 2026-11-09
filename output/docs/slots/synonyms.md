

# Slot: synonyms 



URI: [usdm:slot/synonyms](https://www.cdisc.org/usdm/slot/synonyms)
Alias: synonyms

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [BiomedicalConcept](../classes/BiomedicalConcept.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConcept](../classes/BiomedicalConcept.md) |












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