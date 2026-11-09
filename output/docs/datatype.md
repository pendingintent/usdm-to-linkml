

# Slot: datatype 



URI: [usdm:datatype](https://www.cdisc.org/usdm/datatype)
Alias: datatype

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptProperty](BiomedicalConceptProperty.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiomedicalConceptProperty](BiomedicalConceptProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [BiomedicalConceptProperty](BiomedicalConceptProperty.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:datatype |
| native | usdm:datatype |




## LinkML Source

<details>
```yaml
name: datatype
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: datatype
owner: BiomedicalConceptProperty
domain_of:
- BiomedicalConceptProperty
range: string
required: true

```
</details>