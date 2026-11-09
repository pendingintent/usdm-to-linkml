

# Slot: embeddedProductId 



URI: [usdm:slot/embeddedProductId](https://www.cdisc.org/usdm/slot/embeddedProductId)
Alias: embeddedProductId

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
| self | usdm:embeddedProductId |
| native | usdm:embeddedProductId |




## LinkML Source

<details>
```yaml
name: embeddedProductId
from_schema: https://www.cdisc.org/usdm
rank: 1000
alias: embeddedProductId
owner: MedicalDevice
domain_of:
- MedicalDevice
range: string
required: false

```
</details>