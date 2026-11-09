

# Slot: secondaryReasons 



URI: [usdm:secondaryReasons](https://www.cdisc.org/usdm/secondaryReasons)
Alias: secondaryReasons

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendment](StudyAmendment.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyAmendmentReason](StudyAmendmentReason.md) |
| Domain Of | [StudyAmendment](StudyAmendment.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyAmendment](StudyAmendment.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:secondaryReasons |
| native | usdm:secondaryReasons |




## LinkML Source

<details>
```yaml
name: secondaryReasons
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: secondaryReasons
owner: StudyAmendment
domain_of:
- StudyAmendment
range: StudyAmendmentReason
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>