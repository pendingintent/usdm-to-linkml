

# Slot: study 



URI: [usdm:slot/study](https://www.cdisc.org/usdm/slot/study)
Alias: study

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Wrapper](../classes/Wrapper.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Study](../classes/Study.md) |
| Domain Of | [Wrapper](../classes/Wrapper.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Wrapper](../classes/Wrapper.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:study |
| native | usdm:study |




## LinkML Source

<details>
```yaml
name: study
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: study
owner: Wrapper
domain_of:
- Wrapper
range: Study
required: true
inlined: true

```
</details>