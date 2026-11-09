

# Slot: intentTypes 



URI: [usdm:intentTypes](https://www.cdisc.org/usdm/intentTypes)
Alias: intentTypes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [InterventionalStudyDesign](InterventionalStudyDesign.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
| Domain Of | [InterventionalStudyDesign](InterventionalStudyDesign.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [InterventionalStudyDesign](InterventionalStudyDesign.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:intentTypes |
| native | usdm:intentTypes |




## LinkML Source

<details>
```yaml
name: intentTypes
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: intentTypes
owner: InterventionalStudyDesign
domain_of:
- InterventionalStudyDesign
range: Code
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>