

# Slot: reference 



URI: [usdm:slot/reference](https://www.cdisc.org/usdm/slot/reference)
Alias: reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptSurrogate](../classes/BiomedicalConceptSurrogate.md) |  |  no  |
| [BiomedicalConcept](../classes/BiomedicalConcept.md) |  |  no  |
| [ParameterMap](../classes/ParameterMap.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [BiomedicalConcept](../classes/BiomedicalConcept.md), [BiomedicalConceptSurrogate](../classes/BiomedicalConceptSurrogate.md), [ParameterMap](../classes/ParameterMap.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:reference |
| native | usdm:reference |




## LinkML Source

<details>
```yaml
name: reference
alias: reference
domain_of:
- BiomedicalConcept
- BiomedicalConceptSurrogate
- ParameterMap
range: string

```
</details>