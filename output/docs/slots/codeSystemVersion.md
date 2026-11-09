

# Slot: codeSystemVersion 



URI: [usdm:slot/codeSystemVersion](https://www.cdisc.org/usdm/slot/codeSystemVersion)
Alias: codeSystemVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Code](../classes/Code.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [Code](../classes/Code.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Code](../classes/Code.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:codeSystemVersion |
| native | usdm:codeSystemVersion |




## LinkML Source

<details>
```yaml
name: codeSystemVersion
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: codeSystemVersion
owner: Code
domain_of:
- Code
range: string
required: true

```
</details>