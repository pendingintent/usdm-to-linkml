

# Slot: environmentalSettings 



URI: [usdm:environmentalSettings](https://www.cdisc.org/usdm/environmentalSettings)
Alias: environmentalSettings

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Code](Code.md) |
| Domain Of | [Encounter](Encounter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Encounter](Encounter.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:environmentalSettings |
| native | usdm:environmentalSettings |




## LinkML Source

<details>
```yaml
name: environmentalSettings
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: environmentalSettings
owner: Encounter
domain_of:
- Encounter
range: Code
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>