

# Slot: isRequired 



URI: [usdm:slot/isRequired](https://www.cdisc.org/usdm/slot/isRequired)
Alias: isRequired

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Boolean](../types/Boolean.md) |
| Domain Of | [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:isRequired |
| native | usdm:isRequired |




## LinkML Source

<details>
```yaml
name: isRequired
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: isRequired
owner: BiomedicalConceptProperty
domain_of:
- BiomedicalConceptProperty
range: boolean
required: true

```
</details>