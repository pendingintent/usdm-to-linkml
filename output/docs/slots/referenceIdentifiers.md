

# Slot: referenceIdentifiers 



URI: [usdm:slot/referenceIdentifiers](https://www.cdisc.org/usdm/slot/referenceIdentifiers)
Alias: referenceIdentifiers

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ReferenceIdentifier](../classes/ReferenceIdentifier.md) |
| Domain Of | [StudyVersion](../classes/StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](../classes/StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:referenceIdentifiers |
| native | usdm:referenceIdentifiers |




## LinkML Source

<details>
```yaml
name: referenceIdentifiers
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: referenceIdentifiers
owner: StudyVersion
domain_of:
- StudyVersion
range: ReferenceIdentifier
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>