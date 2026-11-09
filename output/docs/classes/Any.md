

# Class: Any 


_Unconstrained range of union-typed attributes; their any_of narrows it to the allowed classes._





URI: [linkml:Any](https://w3id.org/linkml/Any)





```mermaid
 classDiagram
    class Any
    click Any href "../../classes/Any/"
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [linkml:Any](https://w3id.org/linkml/Any) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Duration](../classes/Duration.md) | [quantity](../slots/quantity.md) | range | [Any](../classes/Any.md) |
| [ScheduleTimeline](../classes/ScheduleTimeline.md) | [instances](../slots/instances.md) | range | [Any](../classes/Any.md) |
| [Strength](../classes/Strength.md) | [numerator](../slots/numerator.md) | range | [Any](../classes/Any.md) |
| [StudyCohort](../classes/StudyCohort.md) | [plannedEnrollmentNumber](../slots/plannedEnrollmentNumber.md) | range | [Any](../classes/Any.md) |
| [StudyCohort](../classes/StudyCohort.md) | [plannedCompletionNumber](../slots/plannedCompletionNumber.md) | range | [Any](../classes/Any.md) |
| [StudyDesignPopulation](../classes/StudyDesignPopulation.md) | [plannedEnrollmentNumber](../slots/plannedEnrollmentNumber.md) | range | [Any](../classes/Any.md) |
| [StudyDesignPopulation](../classes/StudyDesignPopulation.md) | [plannedCompletionNumber](../slots/plannedCompletionNumber.md) | range | [Any](../classes/Any.md) |
| [StudyVersion](../classes/StudyVersion.md) | [studyDesigns](../slots/studyDesigns.md) | range | [Any](../classes/Any.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | linkml:Any |
| native | usdm:Any |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Any
description: Unconstrained range of union-typed attributes; their any_of narrows it
  to the allowed classes.
from_schema: https://www.cdisc.org/usdm
class_uri: linkml:Any

```
</details>

### Induced

<details>
```yaml
name: Any
description: Unconstrained range of union-typed attributes; their any_of narrows it
  to the allowed classes.
from_schema: https://www.cdisc.org/usdm
class_uri: linkml:Any

```
</details>