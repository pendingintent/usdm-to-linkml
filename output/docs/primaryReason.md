

# Slot: primaryReason 



URI: [usdm:primaryReason](https://www.cdisc.org/usdm/primaryReason)
Alias: primaryReason

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
| Required | Yes |
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
| self | usdm:primaryReason |
| native | usdm:primaryReason |




## LinkML Source

<details>
```yaml
name: primaryReason
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: primaryReason
owner: StudyAmendment
domain_of:
- StudyAmendment
range: StudyAmendmentReason
required: true
inlined: true

```
</details>