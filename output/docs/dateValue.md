

# Slot: dateValue 



URI: [usdm:dateValue](https://www.cdisc.org/usdm/dateValue)
Alias: dateValue

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GovernanceDate](GovernanceDate.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Date](Date.md) |
| Domain Of | [GovernanceDate](GovernanceDate.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [GovernanceDate](GovernanceDate.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:dateValue |
| native | usdm:dateValue |




## LinkML Source

<details>
```yaml
name: dateValue
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: dateValue
owner: GovernanceDate
domain_of:
- GovernanceDate
range: date
required: true

```
</details>