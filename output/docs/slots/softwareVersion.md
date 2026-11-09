

# Slot: softwareVersion 



URI: [usdm:slot/softwareVersion](https://www.cdisc.org/usdm/slot/softwareVersion)
Alias: softwareVersion

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MedicalDevice](../classes/MedicalDevice.md) |  |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](../types/String.md) |
| Domain Of | [MedicalDevice](../classes/MedicalDevice.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [MedicalDevice](../classes/MedicalDevice.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:softwareVersion |
| native | usdm:softwareVersion |




## LinkML Source

<details>
```yaml
name: softwareVersion
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: softwareVersion
owner: MedicalDevice
domain_of:
- MedicalDevice
range: string
required: false

```
</details>