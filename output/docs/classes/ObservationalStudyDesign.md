

# Class: ObservationalStudyDesign 



URI: [usdm:class/ObservationalStudyDesign](https://www.cdisc.org/usdm/class/ObservationalStudyDesign)





```mermaid
 classDiagram
    class ObservationalStudyDesign
    click ObservationalStudyDesign href "../../classes/ObservationalStudyDesign/"
      ObservationalStudyDesign : activities
        
          
    
        
        
        ObservationalStudyDesign --> "*" Activity : activities
        click Activity href "../../classes/Activity/"
    

        
      ObservationalStudyDesign : analysisPopulations
        
          
    
        
        
        ObservationalStudyDesign --> "*" AnalysisPopulation : analysisPopulations
        click AnalysisPopulation href "../../classes/AnalysisPopulation/"
    

        
      ObservationalStudyDesign : arms
        
          
    
        
        
        ObservationalStudyDesign --> "1..*" StudyArm : arms
        click StudyArm href "../../classes/StudyArm/"
    

        
      ObservationalStudyDesign : biospecimenRetentions
        
          
    
        
        
        ObservationalStudyDesign --> "*" BiospecimenRetention : biospecimenRetentions
        click BiospecimenRetention href "../../classes/BiospecimenRetention/"
    

        
      ObservationalStudyDesign : characteristics
        
          
    
        
        
        ObservationalStudyDesign --> "*" Code : characteristics
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : description
        
      ObservationalStudyDesign : documentVersionIds
        
      ObservationalStudyDesign : elements
        
          
    
        
        
        ObservationalStudyDesign --> "*" StudyElement : elements
        click StudyElement href "../../classes/StudyElement/"
    

        
      ObservationalStudyDesign : eligibilityCriteria
        
          
    
        
        
        ObservationalStudyDesign --> "1..*" EligibilityCriterion : eligibilityCriteria
        click EligibilityCriterion href "../../classes/EligibilityCriterion/"
    

        
      ObservationalStudyDesign : encounters
        
          
    
        
        
        ObservationalStudyDesign --> "*" Encounter : encounters
        click Encounter href "../../classes/Encounter/"
    

        
      ObservationalStudyDesign : epochs
        
          
    
        
        
        ObservationalStudyDesign --> "1..*" StudyEpoch : epochs
        click StudyEpoch href "../../classes/StudyEpoch/"
    

        
      ObservationalStudyDesign : estimands
        
          
    
        
        
        ObservationalStudyDesign --> "*" Estimand : estimands
        click Estimand href "../../classes/Estimand/"
    

        
      ObservationalStudyDesign : extensionAttributes
        
          
    
        
        
        ObservationalStudyDesign --> "*" ExtensionAttribute : extensionAttributes
        click ExtensionAttribute href "../../classes/ExtensionAttribute/"
    

        
      ObservationalStudyDesign : id
        
      ObservationalStudyDesign : indications
        
          
    
        
        
        ObservationalStudyDesign --> "*" Indication : indications
        click Indication href "../../classes/Indication/"
    

        
      ObservationalStudyDesign : instanceType
        
      ObservationalStudyDesign : label
        
      ObservationalStudyDesign : model
        
          
    
        
        
        ObservationalStudyDesign --> "1" Code : model
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : name
        
      ObservationalStudyDesign : notes
        
          
    
        
        
        ObservationalStudyDesign --> "*" CommentAnnotation : notes
        click CommentAnnotation href "../../classes/CommentAnnotation/"
    

        
      ObservationalStudyDesign : objectives
        
          
    
        
        
        ObservationalStudyDesign --> "*" Objective : objectives
        click Objective href "../../classes/Objective/"
    

        
      ObservationalStudyDesign : population
        
          
    
        
        
        ObservationalStudyDesign --> "1" StudyDesignPopulation : population
        click StudyDesignPopulation href "../../classes/StudyDesignPopulation/"
    

        
      ObservationalStudyDesign : rationale
        
      ObservationalStudyDesign : samplingMethod
        
          
    
        
        
        ObservationalStudyDesign --> "0..1" Code : samplingMethod
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : scheduleTimelines
        
          
    
        
        
        ObservationalStudyDesign --> "*" ScheduleTimeline : scheduleTimelines
        click ScheduleTimeline href "../../classes/ScheduleTimeline/"
    

        
      ObservationalStudyDesign : studyCells
        
          
    
        
        
        ObservationalStudyDesign --> "1..*" StudyCell : studyCells
        click StudyCell href "../../classes/StudyCell/"
    

        
      ObservationalStudyDesign : studyInterventionIds
        
      ObservationalStudyDesign : studyPhase
        
          
    
        
        
        ObservationalStudyDesign --> "0..1" AliasCode : studyPhase
        click AliasCode href "../../classes/AliasCode/"
    

        
      ObservationalStudyDesign : studyType
        
          
    
        
        
        ObservationalStudyDesign --> "0..1" Code : studyType
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : subTypes
        
          
    
        
        
        ObservationalStudyDesign --> "*" Code : subTypes
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : therapeuticAreas
        
          
    
        
        
        ObservationalStudyDesign --> "*" Code : therapeuticAreas
        click Code href "../../classes/Code/"
    

        
      ObservationalStudyDesign : timePerspective
        
          
    
        
        
        ObservationalStudyDesign --> "1" Code : timePerspective
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
| [timePerspective](../slots/timePerspective.md) | 1 <br/> [Code](../classes/Code.md) |  | direct |
| [samplingMethod](../slots/samplingMethod.md) | 0..1 <br/> [Code](../classes/Code.md) |  | direct |
| [instanceType](../slots/instanceType.md) | 1 <br/> [String](../types/String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyVersion](../classes/StudyVersion.md) | [studyDesigns](../slots/studyDesigns.md) | any_of[range] | [ObservationalStudyDesign](../classes/ObservationalStudyDesign.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://www.cdisc.org/usdm




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | usdm:ObservationalStudyDesign |
| native | usdm:ObservationalStudyDesign |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ObservationalStudyDesign
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
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    inlined: true
  studyPhase:
    name: studyPhase
    from_schema: https://www.cdisc.org/usdm
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AliasCode
    required: false
    inlined: true
  therapeuticAreas:
    name: therapeuticAreas
    from_schema: https://www.cdisc.org/usdm
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
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyDesignPopulation
    required: true
    inlined: true
  scheduleTimelines:
    name: scheduleTimelines
    from_schema: https://www.cdisc.org/usdm
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
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  timePerspective:
    name: timePerspective
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  samplingMethod:
    name: samplingMethod
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    domain_of:
    - ObservationalStudyDesign
    range: Code
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
    equals_string: ObservationalStudyDesign

```
</details>

### Induced

<details>
```yaml
name: ObservationalStudyDesign
from_schema: https://www.cdisc.org/usdm
attributes:
  id:
    name: id
    from_schema: https://www.cdisc.org/usdm
    identifier: true
    alias: id
    owner: ObservationalStudyDesign
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
    owner: ObservationalStudyDesign
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
    owner: ObservationalStudyDesign
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
    owner: ObservationalStudyDesign
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
    owner: ObservationalStudyDesign
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
    alias: studyType
    owner: ObservationalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: false
    inlined: true
  studyPhase:
    name: studyPhase
    from_schema: https://www.cdisc.org/usdm
    alias: studyPhase
    owner: ObservationalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: AliasCode
    required: false
    inlined: true
  therapeuticAreas:
    name: therapeuticAreas
    from_schema: https://www.cdisc.org/usdm
    alias: therapeuticAreas
    owner: ObservationalStudyDesign
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
    alias: characteristics
    owner: ObservationalStudyDesign
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
    alias: encounters
    owner: ObservationalStudyDesign
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
    alias: activities
    owner: ObservationalStudyDesign
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
    alias: arms
    owner: ObservationalStudyDesign
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
    alias: studyCells
    owner: ObservationalStudyDesign
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
    alias: rationale
    owner: ObservationalStudyDesign
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
    alias: epochs
    owner: ObservationalStudyDesign
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
    alias: elements
    owner: ObservationalStudyDesign
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
    alias: estimands
    owner: ObservationalStudyDesign
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
    alias: indications
    owner: ObservationalStudyDesign
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
    alias: studyInterventionIds
    owner: ObservationalStudyDesign
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
    alias: objectives
    owner: ObservationalStudyDesign
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
    alias: population
    owner: ObservationalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: StudyDesignPopulation
    required: true
    inlined: true
  scheduleTimelines:
    name: scheduleTimelines
    from_schema: https://www.cdisc.org/usdm
    alias: scheduleTimelines
    owner: ObservationalStudyDesign
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
    alias: biospecimenRetentions
    owner: ObservationalStudyDesign
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
    alias: documentVersionIds
    owner: ObservationalStudyDesign
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
    alias: eligibilityCriteria
    owner: ObservationalStudyDesign
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
    alias: analysisPopulations
    owner: ObservationalStudyDesign
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
    owner: ObservationalStudyDesign
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
    alias: subTypes
    owner: ObservationalStudyDesign
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
    alias: model
    owner: ObservationalStudyDesign
    domain_of:
    - InterventionalStudyDesign
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  timePerspective:
    name: timePerspective
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: timePerspective
    owner: ObservationalStudyDesign
    domain_of:
    - ObservationalStudyDesign
    range: Code
    required: true
    inlined: true
  samplingMethod:
    name: samplingMethod
    from_schema: https://www.cdisc.org/usdm
    rank: 1000
    alias: samplingMethod
    owner: ObservationalStudyDesign
    domain_of:
    - ObservationalStudyDesign
    range: Code
    required: false
    inlined: true
  instanceType:
    name: instanceType
    from_schema: https://www.cdisc.org/usdm
    designates_type: true
    alias: instanceType
    owner: ObservationalStudyDesign
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
    equals_string: ObservationalStudyDesign

```
</details>