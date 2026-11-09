

# Slot: codeSystemVersion 



URI: [usdm:codeSystemVersion](https://www.cdisc.org/usdm/codeSystemVersion)
Alias: codeSystemVersion

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