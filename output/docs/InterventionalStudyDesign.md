

# Class: InterventionalStudyDesign 



URI: [usdm:InterventionalStudyDesign](https://www.cdisc.org/usdm/InterventionalStudyDesign)





```mermaid
 classDiagram
    class InterventionalStudyDesign
    click InterventionalStudyDesign href "../InterventionalStudyDesign/"
      InterventionalStudyDesign : activities
        
          
    
        
        
        InterventionalStudyDesign --> "*" Activity : activities
        click Activity href "../Activity/"
    

        
      InterventionalStudyDesign : analysisPopulations
        
          
    
        
        
        InterventionalStudyDesign --> "*" AnalysisPopulation : analysisPopulations
        click AnalysisPopulation href "../AnalysisPopulation/"
    

        
      InterventionalStudyDesign : arms
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyArm : arms
        click StudyArm href "../StudyArm/"
    

        
      InterventionalStudyDesign : biospecimenRetentions
        
          
    
        
        
        InterventionalStudyDesign --> "*" BiospecimenRetention : biospecimenRetentions
        click BiospecimenRetention href "../BiospecimenRetention/"
    

        
      InterventionalStudyDesign : blindingSchema
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" AliasCode : blindingSchema
        click AliasCode href "../AliasCode/"
    

        
      InterventionalStudyDesign : characteristics
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : characteristics
        click Code href "../Code/"
    

        
      InterventionalStudyDesign : description
        
      InterventionalStudyDesign : documentVersionIds
        
      InterventionalStudyDesign : elements
        
          
    
        
        
        InterventionalStudyDesign --> "*" StudyElement : elements
        click StudyElement href "../StudyElement/"
    

        
      InterventionalStudyDesign : eligibilityCriteria
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" EligibilityCriterion : eligibilityCriteria
        click EligibilityCriterion href "../EligibilityCriterion/"
    

        
      InterventionalStudyDesign : encounters
        
          
    
        
        
        InterventionalStudyDesign --> "*" Encounter : encounters
        click Encounter href "../Encounter/"
    

        
      InterventionalStudyDesign : epochs
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyEpoch : epochs
        click StudyEpoch href "../StudyEpoch/"
    

        
      InterventionalStudyDesign : estimands
        
          
    
        
        
        InterventionalStudyDesign --> "*" Estimand : estimands
        click Estimand href "../Estimand/"
    

        
      InterventionalStudyDesign : extensionAttributes
        
          
    
        
        
        InterventionalStudyDesign --> "*" ExtensionAttribute : extensionAttributes
        click ExtensionAttribute href "../ExtensionAttribute/"
    

        
      InterventionalStudyDesign : id
        
      InterventionalStudyDesign : indications
        
          
    
        
        
        InterventionalStudyDesign --> "*" Indication : indications
        click Indication href "../Indication/"
    

        
      InterventionalStudyDesign : instanceType
        
      InterventionalStudyDesign : intentTypes
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : intentTypes
        click Code href "../Code/"
    

        
      InterventionalStudyDesign : label
        
      InterventionalStudyDesign : model
        
          
    
        
        
        InterventionalStudyDesign --> "1" Code : model
        click Code href "../Code/"
    

        
      InterventionalStudyDesign : name
        
      InterventionalStudyDesign : notes
        
          
    
        
        
        InterventionalStudyDesign --> "*" CommentAnnotation : notes
        click CommentAnnotation href "../CommentAnnotation/"
    

        
      InterventionalStudyDesign : objectives
        
          
    
        
        
        InterventionalStudyDesign --> "*" Objective : objectives
        click Objective href "../Objective/"
    

        
      InterventionalStudyDesign : population
        
          
    
        
        
        InterventionalStudyDesign --> "1" StudyDesignPopulation : population
        click StudyDesignPopulation href "../StudyDesignPopulation/"
    

        
      InterventionalStudyDesign : rationale
        
      InterventionalStudyDesign : scheduleTimelines
        
          
    
        
        
        InterventionalStudyDesign --> "*" ScheduleTimeline : scheduleTimelines
        click ScheduleTimeline href "../ScheduleTimeline/"
    

        
      InterventionalStudyDesign : studyCells
        
          
    
        
        
        InterventionalStudyDesign --> "1..*" StudyCell : studyCells
        click StudyCell href "../StudyCell/"
    

        
      InterventionalStudyDesign : studyInterventionIds
        
      InterventionalStudyDesign : studyPhase
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" AliasCode : studyPhase
        click AliasCode href "../AliasCode/"
    

        
      InterventionalStudyDesign : studyType
        
          
    
        
        
        InterventionalStudyDesign --> "0..1" Code : studyType
        click Code href "../Code/"
    

        
      InterventionalStudyDesign : subTypes
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : subTypes
        click Code href "../Code/"
    

        
      InterventionalStudyDesign : therapeuticAreas
        
          
    
        
        
        InterventionalStudyDesign --> "*" Code : therapeuticAreas
        click Code href "../Code/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) |  | direct |
| [extensionAttributes](extensionAttributes.md) | * <br/> [ExtensionAttribute](ExtensionAttribute.md) |  | direct |
| [name](name.md) | 1 <br/> [String](String.md) |  | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) |  | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) |  | direct |
| [studyType](studyType.md) | 0..1 <br/> [Code](Code.md) |  | direct |
| [studyPhase](studyPhase.md) | 0..1 <br/> [AliasCode](AliasCode.md) |  | direct |
| [therapeuticAreas](therapeuticAreas.md) | * <br/> [Code](Code.md) |  | direct |
| [characteristics](characteristics.md) | * <br/> [Code](Code.md) |  | direct |
| [encounters](encounters.md) | * <br/> [Encounter](Encounter.md) |  | direct |
| [activities](activities.md) | * <br/> [Activity](Activity.md) |  | direct |
| [arms](arms.md) | 1..* <br/> [StudyArm](StudyArm.md) |  | direct |
| [studyCells](studyCells.md) | 1..* <br/> [StudyCell](StudyCell.md) |  | direct |
| [rationale](rationale.md) | 1 <br/> [String](String.md) |  | direct |
| [epochs](epochs.md) | 1..* <br/> [StudyEpoch](StudyEpoch.md) |  | direct |
| [elements](elements.md) | * <br/> [StudyElement](StudyElement.md) |  | direct |
| [estimands](estimands.md) | * <br/> [Estimand](Estimand.md) |  | direct |
| [indications](indications.md) | * <br/> [Indication](Indication.md) |  | direct |
| [studyInterventionIds](studyInterventionIds.md) | * <br/> [String](String.md) |  | direct |
| [objectives](objectives.md) | * <br/> [Objective](Objective.md) |  | direct |
| [population](population.md) | 1 <br/> [StudyDesignPopulation](StudyDesignPopulation.md) |  | direct |
| [scheduleTimelines](scheduleTimelines.md) | * <br/> [ScheduleTimeline](ScheduleTimeline.md) |  | direct |
| [biospecimenRetentions](biospecimenRetentions.md) | * <br/> [BiospecimenRetention](BiospecimenRetention.md) |  | direct |
| [documentVersionIds](documentVersionIds.md) | * <br/> [String](String.md) |  | direct |
| [eligibilityCriteria](eligibilityCriteria.md) | 1..* <br/> [EligibilityCriterion](EligibilityCriterion.md) |  | direct |
| [analysisPopulations](analysisPopulations.md) | * <br/> [AnalysisPopulation](AnalysisPopulation.md) |  | direct |
| [notes](notes.md) | * <br/> [CommentAnnotation](CommentAnnotation.md) |  | direct |
| [subTypes](subTypes.md) | * <br/> [Code](Code.md) |  | direct |
| [model](model.md) | 1 <br/> [Code](Code.md) |  | direct |
| [intentTypes](intentTypes.md) | * <br/> [Code](Code.md) |  | direct |
| [blindingSchema](blindingSchema.md) | 0..1 <br/> [AliasCode](AliasCode.md) |  | direct |
| [instanceType](instanceType.md) | 1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyVersion](StudyVersion.md) | [studyDesigns](studyDesigns.md) | any_of[range] | [InterventionalStudyDesign](InterventionalStudyDesign.md) |












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