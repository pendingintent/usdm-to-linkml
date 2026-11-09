

# Slot: cohorts 



URI: [usdm:slot/cohorts](https://www.cdisc.org/usdm/slot/cohorts)
Alias: cohorts

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyDesignPopulation](../classes/StudyDesignPopulation.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [StudyCohort](../classes/StudyCohort.md) |
| Domain Of | [StudyDesignPopulation](../classes/StudyDesignPopulation.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyDesignPopulation](../classes/StudyDesignPopulation.md) |












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