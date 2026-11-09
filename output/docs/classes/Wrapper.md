

# Class: Wrapper 



URI: [usdm:class/Wrapper](https://www.cdisc.org/usdm/class/Wrapper)





```mermaid
 classDiagram
    class Wrapper
    click Wrapper href "../../classes/Wrapper/"
      Wrapper : study
        
          
    
        
        
        Wrapper --> "1" Study : study
        click Study href "../../classes/Study/"
    

        
      Wrapper : systemName
        
      Wrapper : systemVersion
        
      Wrapper : usdmVersion
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [study](../slots/study.md) | 1 <br/> [Study](../classes/Study.md) |  | direct |
| [usdmVersion](../slots/usdmVersion.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [systemName](../slots/systemName.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [systemVersion](../slots/systemVersion.md) | 0..1 <br/> [String](../types/String.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:Wrapper |
| native | usdm:Wrapper |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Wrapper
from_schema: https://www.cdisc.org/usdm
attributes:
  study:
    name: study
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - Wrapper
    range: Study
    required: true
    inlined: true
  usdmVersion:
    name: usdmVersion
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - Wrapper
    range: string
    required: true
  systemName:
    name: systemName
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - Wrapper
    range: string
    required: false
  systemVersion:
    name: systemVersion
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - Wrapper
    range: string
    required: false

```
</details>

### Induced

<details>
```yaml
name: Wrapper
from_schema: https://www.cdisc.org/usdm
attributes:
  study:
    name: study
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: study
    owner: Wrapper
    domain_of:
    - Wrapper
    range: Study
    required: true
    inlined: true
  usdmVersion:
    name: usdmVersion
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: usdmVersion
    owner: Wrapper
    domain_of:
    - Wrapper
    range: string
    required: true
  systemName:
    name: systemName
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: systemName
    owner: Wrapper
    domain_of:
    - Wrapper
    range: string
    required: false
  systemVersion:
    name: systemVersion
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: systemVersion
    owner: Wrapper
    domain_of:
    - Wrapper
    range: string
    required: false

```
</details>