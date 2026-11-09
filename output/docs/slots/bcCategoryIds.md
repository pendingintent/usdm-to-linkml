

# Slot: bcCategoryIds 



URI: [usdm:slot/bcCategoryIds](https://www.cdisc.org/usdm/slot/bcCategoryIds)
Alias: bcCategoryIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](../classes/Activity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
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
| self | usdm:bcCategoryIds |
| native | usdm:bcCategoryIds |




## LinkML Source

<details>
```yaml
name: bcCategoryIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: bcCategoryIds
owner: Activity
domain_of:
- Activity
range: string
required: false
multivalued: true

```
</details>