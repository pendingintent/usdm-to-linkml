

# Class: StudyVersion 



URI: [usdm:class/StudyVersion](https://www.cdisc.org/usdm/class/StudyVersion)





```mermaid
 classDiagram
    class StudyVersion
    click StudyVersion href "../../classes/StudyVersion/"
      StudyVersion : abbreviations
        
          
    
        
        
        StudyVersion --> "*" Abbreviation : abbreviations
        click Abbreviation href "../../classes/Abbreviation/"
    

        
      StudyVersion : administrableProducts
        
          
    
        
        
        StudyVersion --> "*" AdministrableProduct : administrableProducts
        click AdministrableProduct href "../../classes/AdministrableProduct/"
    

        
      StudyVersion : amendments
        
          
    
        
        
        StudyVersion --> "*" StudyAmendment : amendments
        click StudyAmendment href "../../classes/StudyAmendment/"
    

        
      StudyVersion : bcCategories
        
          
    
        
        
        StudyVersion --> "*" BiomedicalConceptCategory : bcCategories
        click BiomedicalConceptCategory href "../../classes/BiomedicalConceptCategory/"
    

        
      StudyVersion : bcSurrogates
        
          
    
        
        
        StudyVersion --> "*" BiomedicalConceptSurrogate : bcSurrogates
        click BiomedicalConceptSurrogate href "../../classes/BiomedicalConceptSurrogate/"
    

        
      StudyVersion : biomedicalConcepts
        
          
    
        
        
        StudyVersion --> "*" BiomedicalConcept : biomedicalConcepts
        click BiomedicalConcept href "../../classes/BiomedicalConcept/"
    

        
      StudyVersion : businessTherapeuticAreas
        
          
    
        
        
        StudyVersion --> "*" Code : businessTherapeuticAreas
        click Code href "../../classes/Code/"
    

        
      StudyVersion : conditions
        
          
    
        
        
        StudyVersion --> "*" Condition : conditions
        click Condition href "../../classes/Condition/"
    

        
      StudyVersion : dateValues
        
          
    
        
        
        StudyVersion --> "*" GovernanceDate : dateValues
        click GovernanceDate href "../../classes/GovernanceDate/"
    

        
      StudyVersion : dictionaries
        
          
    
        
        
        StudyVersion --> "*" SyntaxTemplateDictionary : dictionaries
        click SyntaxTemplateDictionary href "../../classes/SyntaxTemplateDictionary/"
    

        
      StudyVersion : documentVersionIds
        
      StudyVersion : eligibilityCriterionItems
        
          
    
        
        
        StudyVersion --> "*" EligibilityCriterionItem : eligibilityCriterionItems
        click EligibilityCriterionItem href "../../classes/EligibilityCriterionItem/"
    

        
      StudyVersion : extensionAttributes
        
          
    
        
        
        StudyVersion --> "*" ExtensionAttribute : extensionAttributes
        click ExtensionAttribute href "../../classes/ExtensionAttribute/"
    

        
      StudyVersion : id
        
      StudyVersion : instanceType
        
      StudyVersion : medicalDevices
        
          
    
        
        
        StudyVersion --> "*" MedicalDevice : medicalDevices
        click MedicalDevice href "../../classes/MedicalDevice/"
    

        
      StudyVersion : narrativeContentItems
        
          
    
        
        
        StudyVersion --> "*" NarrativeContentItem : narrativeContentItems
        click NarrativeContentItem href "../../classes/NarrativeContentItem/"
    

        
      StudyVersion : notes
        
          
    
        
        
        StudyVersion --> "*" CommentAnnotation : notes
        click CommentAnnotation href "../../classes/CommentAnnotation/"
    

        
      StudyVersion : organizations
        
          
    
        
        
        StudyVersion --> "*" Organization : organizations
        click Organization href "../../classes/Organization/"
    

        
      StudyVersion : productOrganizationRoles
        
          
    
        
        
        StudyVersion --> "*" ProductOrganizationRole : productOrganizationRoles
        click ProductOrganizationRole href "../../classes/ProductOrganizationRole/"
    

        
      StudyVersion : rationale
        
      StudyVersion : referenceIdentifiers
        
          
    
        
        
        StudyVersion --> "*" ReferenceIdentifier : referenceIdentifiers
        click ReferenceIdentifier href "../../classes/ReferenceIdentifier/"
    

        
      StudyVersion : roles
        
          
    
        
        
        StudyVersion --> "*" StudyRole : roles
        click StudyRole href "../../classes/StudyRole/"
    

        
      StudyVersion : studyDesigns
        
          
    
        
        
        StudyVersion --> "*" Any : studyDesigns
        click Any href "../../classes/Any/"
    

        
      StudyVersion : studyIdentifiers
        
          
    
        
        
        StudyVersion --> "1..*" StudyIdentifier : studyIdentifiers
        click StudyIdentifier href "../../classes/StudyIdentifier/"
    

        
      StudyVersion : studyInterventions
        
          
    
        
        
        StudyVersion --> "*" StudyIntervention : studyInterventions
        click StudyIntervention href "../../classes/StudyIntervention/"
    

        
      StudyVersion : titles
        
          
    
        
        
        StudyVersion --> "1..*" StudyTitle : titles
        click StudyTitle href "../../classes/StudyTitle/"
    

        
      StudyVersion : versionIdentifier
        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [extensionAttributes](../slots/extensionAttributes.md) | * <br/> [ExtensionAttribute](../classes/ExtensionAttribute.md) |  | direct |
| [versionIdentifier](../slots/versionIdentifier.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [rationale](../slots/rationale.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [documentVersionIds](../slots/documentVersionIds.md) | * <br/> [String](../types/String.md) |  | direct |
| [dateValues](../slots/dateValues.md) | * <br/> [GovernanceDate](../classes/GovernanceDate.md) |  | direct |
| [amendments](../slots/amendments.md) | * <br/> [StudyAmendment](../classes/StudyAmendment.md) |  | direct |
| [businessTherapeuticAreas](../slots/businessTherapeuticAreas.md) | * <br/> [Code](../classes/Code.md) |  | direct |
| [studyIdentifiers](../slots/studyIdentifiers.md) | 1..* <br/> [StudyIdentifier](../classes/StudyIdentifier.md) |  | direct |
| [referenceIdentifiers](../slots/referenceIdentifiers.md) | * <br/> [ReferenceIdentifier](../classes/ReferenceIdentifier.md) |  | direct |
| [studyDesigns](../slots/studyDesigns.md) | * <br/> [InterventionalStudyDesign](../classes/InterventionalStudyDesign.md)&nbsp;or&nbsp;<br />[Any](../classes/Any.md)&nbsp;or&nbsp;<br />[ObservationalStudyDesign](../classes/ObservationalStudyDesign.md) |  | direct |
| [titles](../slots/titles.md) | 1..* <br/> [StudyTitle](../classes/StudyTitle.md) |  | direct |
| [eligibilityCriterionItems](../slots/eligibilityCriterionItems.md) | * <br/> [EligibilityCriterionItem](../classes/EligibilityCriterionItem.md) |  | direct |
| [narrativeContentItems](../slots/narrativeContentItems.md) | * <br/> [NarrativeContentItem](../classes/NarrativeContentItem.md) |  | direct |
| [abbreviations](../slots/abbreviations.md) | * <br/> [Abbreviation](../classes/Abbreviation.md) |  | direct |
| [roles](../slots/roles.md) | * <br/> [StudyRole](../classes/StudyRole.md) |  | direct |
| [organizations](../slots/organizations.md) | * <br/> [Organization](../classes/Organization.md) |  | direct |
| [studyInterventions](../slots/studyInterventions.md) | * <br/> [StudyIntervention](../classes/StudyIntervention.md) |  | direct |
| [administrableProducts](../slots/administrableProducts.md) | * <br/> [AdministrableProduct](../classes/AdministrableProduct.md) |  | direct |
| [medicalDevices](../slots/medicalDevices.md) | * <br/> [MedicalDevice](../classes/MedicalDevice.md) |  | direct |
| [productOrganizationRoles](../slots/productOrganizationRoles.md) | * <br/> [ProductOrganizationRole](../classes/ProductOrganizationRole.md) |  | direct |
| [biomedicalConcepts](../slots/biomedicalConcepts.md) | * <br/> [BiomedicalConcept](../classes/BiomedicalConcept.md) |  | direct |
| [bcCategories](../slots/bcCategories.md) | * <br/> [BiomedicalConceptCategory](../classes/BiomedicalConceptCategory.md) |  | direct |
| [bcSurrogates](../slots/bcSurrogates.md) | * <br/> [BiomedicalConceptSurrogate](../classes/BiomedicalConceptSurrogate.md) |  | direct |
| [dictionaries](../slots/dictionaries.md) | * <br/> [SyntaxTemplateDictionary](../classes/SyntaxTemplateDictionary.md) |  | direct |
| [conditions](../slots/conditions.md) | * <br/> [Condition](../classes/Condition.md) |  | direct |
| [notes](../slots/notes.md) | * <br/> [CommentAnnotation](../classes/CommentAnnotation.md) |  | direct |
| [instanceType](../slots/instanceType.md) | 1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](../classes/Study.md) | [versions](../slots/versions.md) | range | [StudyVersion](../classes/StudyVersion.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:StudyVersion |
| native | usdm:StudyVersion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: StudyVersion
from_schema: https://www.cdisc.org/usdm
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/usdm
    identifier: true
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    pattern: ^[\s\S]+$
  extensionAttributes:
    name: extensionAttributes
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: ExtensionAttribute
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  versionIdentifier:
    name: versionIdentifier
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: string
    required: true
  rationale:
    name: rationale
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyChange
    - StudyVersion
    range: string
    required: true
  documentVersionIds:
    name: documentVersionIds
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyVersion
    range: string
    required: false
    multivalued: true
  dateValues:
    name: dateValues
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - StudyAmendment
    - StudyDefinitionDocumentVersion
    - StudyVersion
    range: GovernanceDate
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  amendments:
    name: amendments
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: StudyAmendment
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  businessTherapeuticAreas:
    name: businessTherapeuticAreas
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyIdentifiers:
    name: studyIdentifiers
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: StudyIdentifier
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  referenceIdentifiers:
    name: referenceIdentifiers
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: ReferenceIdentifier
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyDesigns:
    name: studyDesigns
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: Any
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
    any_of:
    - range: InterventionalStudyDesign
      inlined: true
    - range: ObservationalStudyDesign
      inlined: true
  titles:
    name: titles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: StudyTitle
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  eligibilityCriterionItems:
    name: eligibilityCriterionItems
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: EligibilityCriterionItem
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  narrativeContentItems:
    name: narrativeContentItems
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: NarrativeContentItem
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  abbreviations:
    name: abbreviations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: Abbreviation
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  roles:
    name: roles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: StudyRole
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  organizations:
    name: organizations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: Organization
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyInterventions:
    name: studyInterventions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: StudyIntervention
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  administrableProducts:
    name: administrableProducts
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: AdministrableProduct
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  medicalDevices:
    name: medicalDevices
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: MedicalDevice
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  productOrganizationRoles:
    name: productOrganizationRoles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: ProductOrganizationRole
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  biomedicalConcepts:
    name: biomedicalConcepts
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: BiomedicalConcept
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  bcCategories:
    name: bcCategories
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: BiomedicalConceptCategory
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  bcSurrogates:
    name: bcSurrogates
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: BiomedicalConceptSurrogate
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  dictionaries:
    name: dictionaries
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: SyntaxTemplateDictionary
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  conditions:
    name: conditions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - StudyVersion
    range: Condition
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - Abbreviation
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Procedure
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyArm
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudyVersion
    range: CommentAnnotation
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  instanceType:
    name: instanceType
    from_schema: https://www.cdisc.org/usdm
    designates_type: true
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    equals_string: StudyVersion

```
</details>

### Induced

<details>
```yaml
name: StudyVersion
from_schema: https://www.cdisc.org/usdm
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/usdm
    identifier: true
    alias: id
    owner: StudyVersion
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    pattern: ^[\s\S]+$
  extensionAttributes:
    name: extensionAttributes
    from_schema: https://www.cdisc.org/usdm
    alias: extensionAttributes
    owner: StudyVersion
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: ExtensionAttribute
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  versionIdentifier:
    name: versionIdentifier
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: versionIdentifier
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: string
    required: true
  rationale:
    name: rationale
    from_schema: https://www.cdisc.org/usdm
    alias: rationale
    owner: StudyVersion
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyChange
    - StudyVersion
    range: string
    required: true
  documentVersionIds:
    name: documentVersionIds
    from_schema: https://www.cdisc.org/usdm
    alias: documentVersionIds
    owner: StudyVersion
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyVersion
    range: string
    required: false
    multivalued: true
  dateValues:
    name: dateValues
    from_schema: https://www.cdisc.org/usdm
    alias: dateValues
    owner: StudyVersion
    domain_of:
    - StudyAmendment
    - StudyDefinitionDocumentVersion
    - StudyVersion
    range: GovernanceDate
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  amendments:
    name: amendments
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: amendments
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: StudyAmendment
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  businessTherapeuticAreas:
    name: businessTherapeuticAreas
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: businessTherapeuticAreas
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyIdentifiers:
    name: studyIdentifiers
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyIdentifiers
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: StudyIdentifier
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  referenceIdentifiers:
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
  studyDesigns:
    name: studyDesigns
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyDesigns
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: Any
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
    any_of:
    - range: InterventionalStudyDesign
      inlined: true
    - range: ObservationalStudyDesign
      inlined: true
  titles:
    name: titles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: titles
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: StudyTitle
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  eligibilityCriterionItems:
    name: eligibilityCriterionItems
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: eligibilityCriterionItems
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: EligibilityCriterionItem
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  narrativeContentItems:
    name: narrativeContentItems
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: narrativeContentItems
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: NarrativeContentItem
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  abbreviations:
    name: abbreviations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: abbreviations
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: Abbreviation
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  roles:
    name: roles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: roles
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: StudyRole
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  organizations:
    name: organizations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: organizations
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: Organization
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyInterventions:
    name: studyInterventions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyInterventions
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: StudyIntervention
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  administrableProducts:
    name: administrableProducts
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: administrableProducts
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: AdministrableProduct
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  medicalDevices:
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
  productOrganizationRoles:
    name: productOrganizationRoles
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: productOrganizationRoles
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: ProductOrganizationRole
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  biomedicalConcepts:
    name: biomedicalConcepts
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: biomedicalConcepts
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: BiomedicalConcept
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  bcCategories:
    name: bcCategories
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: bcCategories
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: BiomedicalConceptCategory
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  bcSurrogates:
    name: bcSurrogates
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: bcSurrogates
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: BiomedicalConceptSurrogate
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  dictionaries:
    name: dictionaries
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: dictionaries
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: SyntaxTemplateDictionary
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  conditions:
    name: conditions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: conditions
    owner: StudyVersion
    domain_of:
    - StudyVersion
    range: Condition
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    from_schema: https://www.cdisc.org/usdm
    alias: notes
    owner: StudyVersion
    domain_of:
    - Abbreviation
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Procedure
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyArm
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudyVersion
    range: CommentAnnotation
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  instanceType:
    name: instanceType
    from_schema: https://www.cdisc.org/usdm
    designates_type: true
    alias: instanceType
    owner: StudyVersion
    domain_of:
    - Abbreviation
    - Activity
    - Address
    - AdministrableProduct
    - AdministrableProductIdentifier
    - AdministrableProductProperty
    - Administration
    - AliasCode
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Code
    - CommentAnnotation
    - Condition
    - ConditionAssignment
    - DocumentContentReference
    - Duration
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - ExtensionAttribute
    - ExtensionClass
    - GeographicScope
    - GovernanceDate
    - Indication
    - Ingredient
    - IntercurrentEvent
    - InterventionalStudyDesign
    - Masking
    - MedicalDevice
    - MedicalDeviceIdentifier
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - ParameterMap
    - PersonName
    - Procedure
    - ProductOrganizationRole
    - Quantity
    - Range
    - ReferenceIdentifier
    - ResponseCode
    - ScheduleTimeline
    - ScheduleTimelineExit
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyAmendmentImpact
    - StudyAmendmentReason
    - StudyArm
    - StudyCell
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDefinitionDocumentVersion
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIdentifier
    - StudyIntervention
    - StudyRole
    - StudySite
    - StudyTitle
    - StudyVersion
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    equals_string: StudyVersion

```
</details>