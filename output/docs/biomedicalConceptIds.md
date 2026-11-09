

# Slot: biomedicalConceptIds 



URI: [usdm:biomedicalConceptIds](https://www.cdisc.org/usdm/biomedicalConceptIds)
Alias: biomedicalConceptIds

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Activity](Activity.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
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
| self | usdm:biomedicalConceptIds |
| native | usdm:biomedicalConceptIds |




## LinkML Source

<details>
```yaml
name: biomedicalConceptIds
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: biomedicalConceptIds
owner: Activity
domain_of:
- Activity
range: string
required: false
multivalued: true

```
</details>