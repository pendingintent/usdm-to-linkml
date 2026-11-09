

# Slot: medicalDevices 



URI: [usdm:slot/medicalDevices](https://www.cdisc.org/usdm/slot/medicalDevices)
Alias: medicalDevices

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [MedicalDevice](../classes/MedicalDevice.md) |
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
| self | usdm:medicalDevices |
| native | usdm:medicalDevices |




## LinkML Source

<details>
```yaml
name: medicalDevices
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: medicalDevices
owner: StudyVersion
domain_of:
- StudyVersion
range: MedicalDevice
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>