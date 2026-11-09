

# Slot: responseCodes 



URI: [usdm:slot/responseCodes](https://www.cdisc.org/usdm/slot/responseCodes)
Alias: responseCodes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ResponseCode](../classes/ResponseCode.md) |
| Domain Of | [BiomedicalConceptProperty](../classes/BiomedicalConceptProperty.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
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
| self | usdm:responseCodes |
| native | usdm:responseCodes |




## LinkML Source

<details>
```yaml
name: responseCodes
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: responseCodes
owner: BiomedicalConceptProperty
domain_of:
- BiomedicalConceptProperty
range: ResponseCode
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>