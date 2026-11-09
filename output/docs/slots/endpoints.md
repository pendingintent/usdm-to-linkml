

# Slot: endpoints 



URI: [usdm:slot/endpoints](https://www.cdisc.org/usdm/slot/endpoints)
Alias: endpoints

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Objective](../classes/Objective.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Endpoint](../classes/Endpoint.md) |
| Domain Of | [Objective](../classes/Objective.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Objective](../classes/Objective.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:endpoints |
| native | usdm:endpoints |




## LinkML Source

<details>
```yaml
name: endpoints
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: endpoints
owner: Objective
domain_of:
- Objective
range: Endpoint
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>