

# Slot: definedProcedures 



URI: [usdm:definedProcedures](https://www.cdisc.org/usdm/definedProcedures)
Alias: definedProcedures

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Procedure](Procedure.md) |
| Domain Of | [Activity](Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Activity](Activity.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:definedProcedures |
| native | usdm:definedProcedures |




## LinkML Source

<details>
```yaml
name: definedProcedures
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: definedProcedures
owner: Activity
domain_of:
- Activity
range: Procedure
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>