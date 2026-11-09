

# Slot: reference 



URI: [usdm:reference](https://www.cdisc.org/usdm/reference)
Alias: reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiomedicalConceptSurrogate](BiomedicalConceptSurrogate.md) |  |  no  |
| [BiomedicalConcept](BiomedicalConcept.md) |  |  no  |
| [ParameterMap](ParameterMap.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [BiomedicalConcept](BiomedicalConcept.md), [BiomedicalConceptSurrogate](BiomedicalConceptSurrogate.md), [ParameterMap](ParameterMap.md) |

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