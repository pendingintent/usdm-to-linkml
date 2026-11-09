

# Slot: cohorts 



URI: [usdm:cohorts](https://www.cdisc.org/usdm/cohorts)
Alias: cohorts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDesignPopulation](StudyDesignPopulation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyCohort](StudyCohort.md) |
| Domain Of | [StudyDesignPopulation](StudyDesignPopulation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDesignPopulation](StudyDesignPopulation.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:cohorts |
| native | usdm:cohorts |




## LinkML Source

<details>
```yaml
name: cohorts
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: cohorts
owner: StudyDesignPopulation
domain_of:
- StudyDesignPopulation
range: StudyCohort
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>