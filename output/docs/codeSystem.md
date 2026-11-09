

# Slot: codeSystem 



URI: [usdm:codeSystem](https://www.cdisc.org/usdm/codeSystem)
Alias: codeSystem

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Code](Code.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Code](Code.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Code](Code.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:codeSystem |
| native | usdm:codeSystem |




## LinkML Source

<details>
```yaml
name: codeSystem
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: codeSystem
owner: Code
domain_of:
- Code
range: string
required: true

```
</details>