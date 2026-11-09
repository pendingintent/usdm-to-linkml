

# Slot: codes 



URI: [usdm:slot/codes](https://www.cdisc.org/usdm/slot/codes)
Alias: codes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CommentAnnotation](../classes/CommentAnnotation.md) |  |  no  |
| [Substance](../classes/Substance.md) |  |  no  |
| [StudyIntervention](../classes/StudyIntervention.md) |  |  no  |
| [Indication](../classes/Indication.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [CommentAnnotation](../classes/CommentAnnotation.md), [Indication](../classes/Indication.md), [StudyIntervention](../classes/StudyIntervention.md), [Substance](../classes/Substance.md) |

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