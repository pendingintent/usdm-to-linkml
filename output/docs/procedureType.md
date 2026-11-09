

# Slot: procedureType 



URI: [usdm:procedureType](https://www.cdisc.org/usdm/procedureType)
Alias: procedureType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Procedure](Procedure.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Procedure](Procedure.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Procedure](Procedure.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:procedureType |
| native | usdm:procedureType |




## LinkML Source

<details>
```yaml
name: procedureType
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: procedureType
owner: Procedure
domain_of:
- Procedure
range: string
required: true

```
</details>