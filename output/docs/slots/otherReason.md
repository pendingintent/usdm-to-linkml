

# Slot: otherReason 



URI: [usdm:slot/otherReason](https://www.cdisc.org/usdm/slot/otherReason)
Alias: otherReason

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyAmendmentReason](../classes/StudyAmendmentReason.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [StudyAmendmentReason](../classes/StudyAmendmentReason.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyAmendmentReason](../classes/StudyAmendmentReason.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:otherReason |
| native | usdm:otherReason |




## LinkML Source

<details>
```yaml
name: otherReason
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: otherReason
owner: StudyAmendmentReason
domain_of:
- StudyAmendmentReason
range: string
required: false

```
</details>