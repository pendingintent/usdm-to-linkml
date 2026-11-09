

# Slot: parameterMaps 



URI: [usdm:parameterMaps](https://www.cdisc.org/usdm/parameterMaps)
Alias: parameterMaps

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SyntaxTemplateDictionary](SyntaxTemplateDictionary.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ParameterMap](ParameterMap.md) |
| Domain Of | [SyntaxTemplateDictionary](SyntaxTemplateDictionary.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [SyntaxTemplateDictionary](SyntaxTemplateDictionary.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:parameterMaps |
| native | usdm:parameterMaps |




## LinkML Source

<details>
```yaml
name: parameterMaps
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: parameterMaps
owner: SyntaxTemplateDictionary
domain_of:
- SyntaxTemplateDictionary
range: ParameterMap
required: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>