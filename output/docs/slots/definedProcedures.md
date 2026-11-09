

# Slot: definedProcedures 



URI: [usdm:slot/definedProcedures](https://www.cdisc.org/usdm/slot/definedProcedures)
Alias: definedProcedures

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](../classes/Activity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Procedure](../classes/Procedure.md) |
| Domain Of | [Activity](../classes/Activity.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Activity](../classes/Activity.md) |












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