

# Slot: versionIdentifier 



URI: [usdm:versionIdentifier](https://www.cdisc.org/usdm/versionIdentifier)
Alias: versionIdentifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [StudyVersion](StudyVersion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyVersion](StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:versionIdentifier |
| native | usdm:versionIdentifier |




## LinkML Source

<details>
```yaml
name: versionIdentifier
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: versionIdentifier
owner: StudyVersion
domain_of:
- StudyVersion
range: string
required: true

```
</details>