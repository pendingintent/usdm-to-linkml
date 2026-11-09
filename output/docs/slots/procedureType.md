

# Slot: procedureType 



URI: [usdm:slot/procedureType](https://www.cdisc.org/usdm/slot/procedureType)
Alias: procedureType

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Procedure](../classes/Procedure.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Procedure](../classes/Procedure.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Procedure](../classes/Procedure.md) |












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