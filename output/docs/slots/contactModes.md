

# Slot: contactModes 



URI: [usdm:slot/contactModes](https://www.cdisc.org/usdm/slot/contactModes)
Alias: contactModes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](../classes/Encounter.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](../classes/Code.md) |
| Domain Of | [Encounter](../classes/Encounter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Encounter](../classes/Encounter.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:contactModes |
| native | usdm:contactModes |




## LinkML Source

<details>
```yaml
name: contactModes
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: contactModes
owner: Encounter
domain_of:
- Encounter
range: Code
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>