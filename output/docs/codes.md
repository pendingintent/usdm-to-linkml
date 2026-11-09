

# Slot: codes 



URI: [usdm:codes](https://www.cdisc.org/usdm/codes)
Alias: codes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommentAnnotation](CommentAnnotation.md) |  |  no  |
| [Substance](Substance.md) |  |  no  |
| [StudyIntervention](StudyIntervention.md) |  |  no  |
| [Indication](Indication.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [CommentAnnotation](CommentAnnotation.md), [Indication](Indication.md), [StudyIntervention](StudyIntervention.md), [Substance](Substance.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information






## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:codes |
| native | usdm:codes |




## LinkML Source

<details>
```yaml
name: codes
alias: codes
domain_of:
- CommentAnnotation
- Indication
- StudyIntervention
- Substance
range: string

```
</details>