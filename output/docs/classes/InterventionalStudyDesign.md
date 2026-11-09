

# Class: InterventionalStudyDesign 



URI: [usdm:class/InterventionalStudyDesign](https://www.cdisc.org/usdm/class/InterventionalStudyDesign)





```mermaid
 classDiagram
    class InterventionalStudyDesign
    click InterventionalStudyDesign href "../../classes/InterventionalStudyDesign/"
      InterventionalStudyDesign : activities
        
          
    
        
        
        InterventionalStudyDesign --> "*" Activity : activities
        click Activity href "../../classes/Activity/"
    

        
      InterventionalStudyDesign : analysisPopulations
        
          
    
        
        
        InterventionalStudyDesign --> "*" AnalysisPopulation : analysisPopulations
        click AnalysisPopulation href "../../classes/AnalysisPopulation/"
    

        
      InterventionalStudyDesign : arms
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyArm : arms
        click StudyArm href "../../classes/StudyArm/"
    

        
      InterventionalStudyDesign : biospecimenRetentions
        
          
    
        
        
        InterventionalStudyDesign --> "*" BiospecimenRetention : biospecimenRetentions
        click BiospecimenRetention href "../../classes/BiospecimenRetention/"
    

        
      InterventionalStudyDesign : blindingSchema
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" AliasCode : blindingSchema
        click AliasCode href "../../classes/AliasCode/"
    

        
      InterventionalStudyDesign : characteristics
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : characteristics
        click Code href "../../classes/Code/"
    

        
      InterventionalStudyDesign : description
        
      InterventionalStudyDesign : documentVersionIds
        
      InterventionalStudyDesign : elements
        
          
    
        
        
        InterventionalStudyDesign --> "*" StudyElement : elements
        click StudyElement href "../../classes/StudyElement/"
    

        
      InterventionalStudyDesign : eligibilityCriteria
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" EligibilityCriterion : eligibilityCriteria
        click EligibilityCriterion href "../../classes/EligibilityCriterion/"
    

        
      InterventionalStudyDesign : encounters
        
          
    
        
        
        InterventionalStudyDesign --> "*" Encounter : encounters
        click Encounter href "../../classes/Encounter/"
    

        
      InterventionalStudyDesign : epochs
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyEpoch : epochs
        click StudyEpoch href "../../classes/StudyEpoch/"
    

        
      InterventionalStudyDesign : estimands
        
          
    
        
        
        InterventionalStudyDesign --> "*" Estimand : estimands
        click Estimand href "../../classes/Estimand/"
    

        
      InterventionalStudyDesign : extensionAttributes
        
          
    
        
        
        InterventionalStudyDesign --> "*" ExtensionAttribute : extensionAttributes
        click ExtensionAttribute href "../../classes/ExtensionAttribute/"
    

        
      InterventionalStudyDesign : id
        
      InterventionalStudyDesign : indications
        
          
    
        
        
        InterventionalStudyDesign --> "*" Indication : indications
        click Indication href "../../classes/Indication/"
    

        
      InterventionalStudyDesign : instanceType
        
      InterventionalStudyDesign : intentTypes
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : intentTypes
        click Code href "../../classes/Code/"
    

        
      InterventionalStudyDesign : label
        
      InterventionalStudyDesign : model
        
          
    
        
        
        InterventionalStudyDesign --> "1" Code : model
        click Code href "../../classes/Code/"
    

        
      InterventionalStudyDesign : name
        
      InterventionalStudyDesign : notes
        
          
    
        
        
        InterventionalStudyDesign --> "*" CommentAnnotation : notes
        click CommentAnnotation href "../../classes/CommentAnnotation/"
    

        
      InterventionalStudyDesign : objectives
        
          
    
        
        
        InterventionalStudyDesign --> "*" Objective : objectives
        click Objective href "../../classes/Objective/"
    

        
      InterventionalStudyDesign : population
        
          
    
        
        
        InterventionalStudyDesign --> "1" StudyDesignPopulation : population
        click StudyDesignPopulation href "../../classes/StudyDesignPopulation/"
    

        
      InterventionalStudyDesign : rationale
        
      InterventionalStudyDesign : scheduleTimelines
        
          
    
        
        
        InterventionalStudyDesign --> "*" ScheduleTimeline : scheduleTimelines
        click ScheduleTimeline href "../../classes/ScheduleTimeline/"
    

        
      InterventionalStudyDesign : studyCells
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyCell : studyCells
        click StudyCell href "../../classes/StudyCell/"
    

        
      InterventionalStudyDesign : studyInterventionIds
        
      InterventionalStudyDesign : studyPhase
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" AliasCode : studyPhase
        click AliasCode href "../../classes/AliasCode/"
    

        
      InterventionalStudyDesign : studyType
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" Code : studyType
        click Code href "../../classes/Code/"
    

        
      InterventionalStudyDesign : subTypes
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : subTypes
        click Code href "../../classes/Code/"
    

        
      InterventionalStudyDesign : therapeuticAreas
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : therapeuticAreas
        click Code href "../../classes/Code/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](../slots/id.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [extensionAttributes](../slots/extensionAttributes.md) | * <br/> [ExtensionAttribute](../classes/ExtensionAttribute.md) |  | direct |
| [name](../slots/name.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [label](../slots/label.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [description](../slots/description.md) | 0..1 <br/> [String](../types/String.md) |  | direct |
| [studyType](../slots/studyType.md) | 0..1 <br/> [Code](../classes/Code.md) |  | direct |
| [studyPhase](../slots/studyPhase.md) | 0..1 <br/> [AliasCode](../classes/AliasCode.md) |  | direct |
| [therapeuticAreas](../slots/therapeuticAreas.md) | * <br/> [Code](../classes/Code.md) |  | direct |
| [characteristics](../slots/characteristics.md) | * <br/> [Code](../classes/Code.md) |  | direct |
| [encounters](../slots/encounters.md) | * <br/> [Encounter](../classes/Encounter.md) |  | direct |
| [activities](../slots/activities.md) | * <br/> [Activity](../classes/Activity.md) |  | direct |
| [arms](../slots/arms.md) | 1..* <br/> [StudyArm](../classes/StudyArm.md) |  | direct |
| [studyCells](../slots/studyCells.md) | 1..* <br/> [StudyCell](../classes/StudyCell.md) |  | direct |
| [rationale](../slots/rationale.md) | 1 <br/> [String](../types/String.md) |  | direct |
| [epochs](../slots/epochs.md) | 1..* <br/> [StudyEpoch](../classes/StudyEpoch.md) |  | direct |
| [elements](../slots/elements.md) | * <br/> [StudyElement](../classes/StudyElement.md) |  | direct |
| [estimands](../slots/estimands.md) | * <br/> [Estimand](../classes/Estimand.md) |  | direct |
| [indications](../slots/indications.md) | * <br/> [Indication](../classes/Indication.md) |  | direct |
| [studyInterventionIds](../slots/studyInterventionIds.md) | * <br/> [String](../types/String.md) |  | direct |
| [objectives](../slots/objectives.md) | * <br/> [Objective](../classes/Objective.md) |  | direct |
| [population](../slots/population.md) | 1 <br/> [StudyDesignPopulation](../classes/StudyDesignPopulation.md) |  | direct |
| [scheduleTimelines](../slots/scheduleTimelines.md) | * <br/> [ScheduleTimeline](../classes/ScheduleTimeline.md) |  | direct |
| [biospecimenRetentions](../slots/biospecimenRetentions.md) | * <br/> [BiospecimenRetention](../classes/BiospecimenRetention.md) |  | direct |
| [documentVersionIds](../slots/documentVersionIds.md) | * <br/> [String](../types/String.md) |  | direct |
| [eligibilityCriteria](../slots/eligibilityCriteria.md) | 1..* <br/> [EligibilityCriterion](../classes/EligibilityCriterion.md) |  | direct |
| [analysisPopulations](../slots/analysisPopulations.md) | * <br/> [AnalysisPopulation](../classes/AnalysisPopulation.md) |  | direct |
| [notes](../slots/notes.md) | * <br/> [CommentAnnotation](../classes/CommentAnnotation.md) |  | direct |
| [subTypes](../slots/subTypes.md) | * <br/> [Code](../classes/Code.md) |  | direct |
| [model](../slots/model.md) | 1 <br/> [Code](../classes/Code.md) |  | direct |
| [intentTypes](../slots/intentTypes.md) | * <br/> [Code](../classes/Code.md) |  | direct |
| [blindingSchema](../slots/blindingSchema.md) | 0..1 <br/> [AliasCode](../classes/AliasCode.md) |  | direct |
| [instanceType](../slots/instanceType.md) | 1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) | [studyDesigns](../slots/studyDesigns.md) | any_of[range] | [InterventionalStudyDesign](../classes/InterventionalStudyDesign.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:InterventionalStudyDesign |
| native | usdm:InterventionalStudyDesign |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InterventionalStudyDesign
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
  name:
    name: name
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - Activity
    - AdministrableProduct
    - AdministrableProductProperty
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - Procedure
    - ProductOrganizationRole
    - ResponseCode
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    pattern: ^[\s\S]+$
  label:
    name: label
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Organization
    - Procedure
    - ProductOrganizationRole
    - ResponseCode
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: false
  description:
    name: description
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConceptCategory
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Procedure
    - ProductOrganizationRole
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: false
  studyType:
    name: studyType
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    inlined: true
  studyPhase:
    name: studyPhase
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AliasCode
    required: false
    inlined: true
  therapeuticAreas:
    name: therapeuticAreas
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  characteristics:
    name: characteristics
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyCohort
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  encounters:
    name: encounters
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Encounter
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  activities:
    name: activities
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Activity
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  arms:
    name: arms
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyArm
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyCells:
    name: studyCells
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyCell
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  rationale:
    name: rationale
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyChange
    - StudyVersion
    range: string
    required: true
  epochs:
    name: epochs
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyEpoch
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  elements:
    name: elements
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyElement
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  estimands:
    name: estimands
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Estimand
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  indications:
    name: indications
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Indication
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyInterventionIds:
    name: studyInterventionIds
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyElement
    range: string
    required: false
    multivalued: true
  objectives:
    name: objectives
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Objective
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  population:
    name: population
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyDesignPopulation
    required: true
    inlined: true
  scheduleTimelines:
    name: scheduleTimelines
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: ScheduleTimeline
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  biospecimenRetentions:
    name: biospecimenRetentions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: BiospecimenRetention
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  documentVersionIds:
    name: documentVersionIds
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyVersion
    range: string
    required: false
    multivalued: true
  eligibilityCriteria:
    name: eligibilityCriteria
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: EligibilityCriterion
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  analysisPopulations:
    name: analysisPopulations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AnalysisPopulation
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
  subTypes:
    name: subTypes
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  model:
    name: model
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  intentTypes:
    name: intentTypes
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  blindingSchema:
    name: blindingSchema
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - InterventionalStudyDesign
    range: AliasCode
    required: false
    inlined: true
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
    equals_string: InterventionalStudyDesign

```
</details>

### Induced

<details>
```yaml
name: InterventionalStudyDesign
from_schema: https://www.cdisc.org/usdm
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/usdm
    identifier: true
    alias: id
    owner: InterventionalStudyDesign
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
    owner: InterventionalStudyDesign
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
  name:
    name: name
    from_schema: https://www.cdisc.org/usdm
    alias: name
    owner: InterventionalStudyDesign
    domain_of:
    - Activity
    - AdministrableProduct
    - AdministrableProductProperty
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - NarrativeContent
    - NarrativeContentItem
    - Objective
    - ObservationalStudyDesign
    - Organization
    - Procedure
    - ProductOrganizationRole
    - ResponseCode
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: true
    pattern: ^[\s\S]+$
  label:
    name: label
    from_schema: https://www.cdisc.org/usdm
    alias: label
    owner: InterventionalStudyDesign
    domain_of:
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConcept
    - BiomedicalConceptCategory
    - BiomedicalConceptProperty
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Organization
    - Procedure
    - ProductOrganizationRole
    - ResponseCode
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: false
  description:
    name: description
    from_schema: https://www.cdisc.org/usdm
    alias: description
    owner: InterventionalStudyDesign
    domain_of:
    - Activity
    - AdministrableProduct
    - Administration
    - AnalysisPopulation
    - AssignedPerson
    - BiomedicalConceptCategory
    - BiomedicalConceptSurrogate
    - BiospecimenRetention
    - Characteristic
    - Condition
    - EligibilityCriterion
    - EligibilityCriterionItem
    - Encounter
    - Endpoint
    - Estimand
    - GovernanceDate
    - Indication
    - IntercurrentEvent
    - InterventionalStudyDesign
    - MedicalDevice
    - Objective
    - ObservationalStudyDesign
    - Procedure
    - ProductOrganizationRole
    - ScheduleTimeline
    - ScheduledActivityInstance
    - ScheduledDecisionInstance
    - Strength
    - Study
    - StudyAmendment
    - StudyArm
    - StudyChange
    - StudyCohort
    - StudyDefinitionDocument
    - StudyDesignPopulation
    - StudyElement
    - StudyEpoch
    - StudyIntervention
    - StudyRole
    - StudySite
    - SubjectEnrollment
    - Substance
    - SyntaxTemplateDictionary
    - Timing
    - TransitionRule
    range: string
    required: false
  studyType:
    name: studyType
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyType
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    inlined: true
  studyPhase:
    name: studyPhase
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyPhase
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AliasCode
    required: false
    inlined: true
  therapeuticAreas:
    name: therapeuticAreas
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: therapeuticAreas
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  characteristics:
    name: characteristics
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: characteristics
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyCohort
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  encounters:
    name: encounters
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: encounters
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Encounter
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  activities:
    name: activities
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: activities
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Activity
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  arms:
    name: arms
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: arms
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyArm
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyCells:
    name: studyCells
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyCells
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyCell
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  rationale:
    name: rationale
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: rationale
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyChange
    - StudyVersion
    range: string
    required: true
  epochs:
    name: epochs
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: epochs
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyEpoch
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  elements:
    name: elements
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: elements
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyElement
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  estimands:
    name: estimands
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: estimands
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Estimand
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  indications:
    name: indications
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: indications
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Indication
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  studyInterventionIds:
    name: studyInterventionIds
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: studyInterventionIds
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyElement
    range: string
    required: false
    multivalued: true
  objectives:
    name: objectives
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: objectives
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Objective
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  population:
    name: population
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: population
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyDesignPopulation
    required: true
    inlined: true
  scheduleTimelines:
    name: scheduleTimelines
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: scheduleTimelines
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: ScheduleTimeline
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  biospecimenRetentions:
    name: biospecimenRetentions
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: biospecimenRetentions
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: BiospecimenRetention
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  documentVersionIds:
    name: documentVersionIds
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: documentVersionIds
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    - StudyVersion
    range: string
    required: false
    multivalued: true
  eligibilityCriteria:
    name: eligibilityCriteria
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: eligibilityCriteria
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: EligibilityCriterion
    required: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  analysisPopulations:
    name: analysisPopulations
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: analysisPopulations
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AnalysisPopulation
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    from_schema: https://www.cdisc.org/usdm
    alias: notes
    owner: InterventionalStudyDesign
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
  subTypes:
    name: subTypes
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: subTypes
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  model:
    name: model
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: model
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  intentTypes:
    name: intentTypes
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: intentTypes
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    range: Code
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  blindingSchema:
    name: blindingSchema
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: blindingSchema
    owner: InterventionalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    range: AliasCode
    required: false
    inlined: true
  instanceType:
    name: instanceType
    from_schema: https://www.cdisc.org/usdm
    designates_type: true
    alias: instanceType
    owner: InterventionalStudyDesign
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
    equals_string: InterventionalStudyDesign

```
</details>