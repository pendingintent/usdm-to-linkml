```mermaid
erDiagram
Abbreviation {
    string id  
    string abbreviatedText  
    string expandedText  
    string instanceType  
}
Activity {
    string id  
    string name  
    string description  
    stringList bcCategoryIds  
    stringList bcSurrogateIds  
    stringList biomedicalConceptIds  
    stringList childIds  
    string instanceType  
    string label  
    string nextId  
    string previousId  
    string timelineId  
}
Address {
    string id  
    string city  
    string district  
    string instanceType  
    stringList lines  
    string postalCode  
    string state  
    string text  
}
AdministrableProduct {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
AdministrableProductIdentifier {
    string id  
    string instanceType  
    string scopeId  
    string text  
}
AdministrableProductProperty {
    string id  
    string name  
    string instanceType  
    string text  
}
Administration {
    string id  
    string name  
    string description  
    string administrableProductId  
    string instanceType  
    string label  
    string medicalDeviceId  
}
AliasCode {
    string id  
    string instanceType  
}
AnalysisPopulation {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    stringList subsetOfIds  
    string text  
}
Any {

}
AssignedPerson {
    string id  
    string name  
    string description  
    string instanceType  
    string jobTitle  
    string label  
    string organizationId  
}
BiomedicalConcept {
    string id  
    string name  
    string instanceType  
    string label  
    string reference  
    stringList synonyms  
}
BiomedicalConceptCategory {
    string id  
    string name  
    string description  
    stringList childIds  
    string instanceType  
    string label  
    stringList memberIds  
}
BiomedicalConceptProperty {
    string id  
    string name  
    string datatype  
    string instanceType  
    boolean isEnabled  
    boolean isRequired  
    string label  
}
BiomedicalConceptSurrogate {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string reference  
}
BiospecimenRetention {
    string id  
    string name  
    string description  
    boolean includesDNA  
    string instanceType  
    boolean isRetained  
    string label  
}
Characteristic {
    string id  
    string name  
    string description  
    string dictionaryId  
    string instanceType  
    string label  
    string text  
}
Code {
    string id  
    string code  
    string codeSystem  
    string codeSystemVersion  
    string decode  
    string instanceType  
}
CommentAnnotation {
    string id  
    string instanceType  
    string text  
}
Condition {
    string id  
    string name  
    string description  
    stringList appliesToIds  
    stringList contextIds  
    string dictionaryId  
    string instanceType  
    string label  
    string text  
}
ConditionAssignment {
    string id  
    string condition  
    string conditionTargetId  
    string instanceType  
}
DocumentContentReference {
    string id  
    string appliesToId  
    string instanceType  
    string sectionNumber  
    string sectionTitle  
}
Duration {
    string id  
    boolean durationWillVary  
    string instanceType  
    string reasonDurationWillVary  
    string text  
}
EligibilityCriterion {
    string id  
    string name  
    string description  
    string criterionItemId  
    string identifier  
    string instanceType  
    string label  
    string nextId  
    string previousId  
}
EligibilityCriterionItem {
    string id  
    string name  
    string description  
    string dictionaryId  
    string instanceType  
    string label  
    string text  
}
Encounter {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string nextId  
    string previousId  
    string scheduledAtId  
}
Endpoint {
    string id  
    string name  
    string description  
    string dictionaryId  
    string instanceType  
    string label  
    string purpose  
    string text  
}
Estimand {
    string id  
    string name  
    string description  
    string analysisPopulationId  
    string instanceType  
    stringList interventionIds  
    string label  
    string populationSummary  
    string variableOfInterestId  
}
ExtensionAttribute {
    string id  
    string instanceType  
    string url  
    boolean valueBoolean  
    string valueId  
    integer valueInteger  
    string valueString  
}
ExtensionClass {
    string id  
    string instanceType  
    string url  
}
GeographicScope {
    string id  
    string instanceType  
}
GovernanceDate {
    string id  
    string name  
    string description  
    date dateValue  
    string instanceType  
    string label  
}
Indication {
    string id  
    string name  
    string description  
    string instanceType  
    boolean isRareDisease  
    string label  
}
Ingredient {
    string id  
    string instanceType  
}
IntercurrentEvent {
    string id  
    string name  
    string description  
    string dictionaryId  
    string instanceType  
    string label  
    string strategy  
    string text  
}
InterventionalStudyDesign {
    string id  
    string name  
    string description  
    stringList documentVersionIds  
    string instanceType  
    string label  
    string rationale  
    stringList studyInterventionIds  
}
Masking {
    string id  
    string instanceType  
    boolean isMasked  
    string text  
}
MedicalDevice {
    string id  
    string name  
    string description  
    string embeddedProductId  
    string hardwareVersion  
    string instanceType  
    string label  
    string softwareVersion  
}
MedicalDeviceIdentifier {
    string id  
    string instanceType  
    string scopeId  
    string text  
}
NarrativeContent {
    string id  
    string name  
    stringList childIds  
    string contentItemId  
    boolean displaySectionNumber  
    boolean displaySectionTitle  
    string instanceType  
    string nextId  
    string previousId  
    string sectionNumber  
    string sectionTitle  
}
NarrativeContentItem {
    string id  
    string name  
    string instanceType  
    string text  
}
Objective {
    string id  
    string name  
    string description  
    string dictionaryId  
    string instanceType  
    string label  
    string text  
}
ObservationalStudyDesign {
    string id  
    string name  
    string description  
    stringList documentVersionIds  
    string instanceType  
    string label  
    string rationale  
    stringList studyInterventionIds  
}
Organization {
    string id  
    string name  
    string identifier  
    string identifierScheme  
    string instanceType  
    string label  
}
ParameterMap {
    string id  
    string instanceType  
    string reference  
    string tag  
}
PersonName {
    string id  
    string familyName  
    stringList givenNames  
    string instanceType  
    stringList prefixes  
    stringList suffixes  
    string text  
}
Procedure {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string procedureType  
    string studyInterventionId  
}
ProductOrganizationRole {
    string id  
    string name  
    string description  
    stringList appliesToIds  
    string instanceType  
    string label  
    string organizationId  
}
Quantity {
    string id  
    string instanceType  
    float value  
}
Range {
    string id  
    string instanceType  
    boolean isApproximate  
}
ReferenceIdentifier {
    string id  
    string instanceType  
    string scopeId  
    string text  
}
ResponseCode {
    string id  
    string name  
    string instanceType  
    boolean isEnabled  
    string label  
}
ScheduleTimeline {
    string id  
    string name  
    string description  
    string entryCondition  
    string entryId  
    string instanceType  
    string label  
    boolean mainTimeline  
}
ScheduleTimelineExit {
    string id  
    string instanceType  
}
ScheduledActivityInstance {
    string id  
    string name  
    string description  
    stringList activityIds  
    string defaultConditionId  
    string encounterId  
    string epochId  
    string instanceType  
    string label  
    string timelineExitId  
    string timelineId  
}
ScheduledDecisionInstance {
    string id  
    string name  
    string description  
    string defaultConditionId  
    string epochId  
    string instanceType  
    string label  
}
Strength {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
Study {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
StudyAmendment {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string number  
    string previousId  
    string summary  
}
StudyAmendmentImpact {
    string id  
    string instanceType  
    boolean isSubstantial  
    string text  
}
StudyAmendmentReason {
    string id  
    string instanceType  
    string otherReason  
}
StudyArm {
    string id  
    string name  
    string description  
    string dataOriginDescription  
    string instanceType  
    string label  
    stringList populationIds  
}
StudyCell {
    string id  
    string armId  
    stringList elementIds  
    string epochId  
    string instanceType  
}
StudyChange {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string rationale  
    string summary  
}
StudyCohort {
    string id  
    string name  
    string description  
    stringList criterionIds  
    boolean includesHealthySubjects  
    stringList indicationIds  
    string instanceType  
    string label  
}
StudyDefinitionDocument {
    string id  
    string name  
    string description  
    stringList childIds  
    string instanceType  
    string label  
    string templateName  
}
StudyDefinitionDocumentVersion {
    string id  
    string instanceType  
    string version  
}
StudyDesignPopulation {
    string id  
    string name  
    string description  
    stringList criterionIds  
    boolean includesHealthySubjects  
    string instanceType  
    string label  
}
StudyElement {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    stringList studyInterventionIds  
}
StudyEpoch {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string nextId  
    string previousId  
}
StudyIdentifier {
    string id  
    string instanceType  
    string scopeId  
    string text  
}
StudyIntervention {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
StudyRole {
    string id  
    string name  
    string description  
    stringList appliesToIds  
    string instanceType  
    string label  
    stringList organizationIds  
}
StudySite {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
StudyTitle {
    string id  
    string instanceType  
    string text  
}
StudyVersion {
    string id  
    stringList documentVersionIds  
    string instanceType  
    string rationale  
    string versionIdentifier  
}
SubjectEnrollment {
    string id  
    string name  
    string description  
    string forStudyCohortId  
    string forStudySiteId  
    string instanceType  
    string label  
}
Substance {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
SyntaxTemplateDictionary {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
}
Timing {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string relativeFromScheduledInstanceId  
    string relativeToScheduledInstanceId  
    string value  
    string valueLabel  
    string windowLabel  
    string windowLower  
    string windowUpper  
}
TransitionRule {
    string id  
    string name  
    string description  
    string instanceType  
    string label  
    string text  
}
Wrapper {
    string systemName  
    string systemVersion  
    string usdmVersion  
}

Abbreviation ||--}o CommentAnnotation : "notes"
Abbreviation ||--}o ExtensionAttribute : "extensionAttributes"
Activity ||--}o CommentAnnotation : "notes"
Activity ||--}o ExtensionAttribute : "extensionAttributes"
Activity ||--}o Procedure : "definedProcedures"
Address ||--|o Code : "country"
Address ||--}o ExtensionAttribute : "extensionAttributes"
AdministrableProduct ||--|o Code : "pharmacologicClass, sourcing"
AdministrableProduct ||--|| AliasCode : "administrableDoseForm"
AdministrableProduct ||--|| Code : "productDesignation"
AdministrableProduct ||--}o AdministrableProductIdentifier : "identifiers"
AdministrableProduct ||--}o AdministrableProductProperty : "properties"
AdministrableProduct ||--}o CommentAnnotation : "notes"
AdministrableProduct ||--}o ExtensionAttribute : "extensionAttributes"
AdministrableProduct ||--}o Ingredient : "ingredients"
AdministrableProductIdentifier ||--}o ExtensionAttribute : "extensionAttributes"
AdministrableProductProperty ||--|o Quantity : "quantity"
AdministrableProductProperty ||--|| Code : "type"
AdministrableProductProperty ||--}o ExtensionAttribute : "extensionAttributes"
Administration ||--|o AliasCode : "frequency, route"
Administration ||--|o Quantity : "dose"
Administration ||--|| Duration : "duration"
Administration ||--}o CommentAnnotation : "notes"
Administration ||--}o ExtensionAttribute : "extensionAttributes"
AliasCode ||--|| Code : "standardCode"
AliasCode ||--}o Code : "standardCodeAliases"
AliasCode ||--}o ExtensionAttribute : "extensionAttributes"
AnalysisPopulation ||--}o CommentAnnotation : "notes"
AnalysisPopulation ||--}o ExtensionAttribute : "extensionAttributes"
AssignedPerson ||--|| PersonName : "personName"
AssignedPerson ||--}o ExtensionAttribute : "extensionAttributes"
BiomedicalConcept ||--|| AliasCode : "code"
BiomedicalConcept ||--}o BiomedicalConceptProperty : "properties"
BiomedicalConcept ||--}o CommentAnnotation : "notes"
BiomedicalConcept ||--}o ExtensionAttribute : "extensionAttributes"
BiomedicalConceptCategory ||--|o AliasCode : "code"
BiomedicalConceptCategory ||--}o CommentAnnotation : "notes"
BiomedicalConceptCategory ||--}o ExtensionAttribute : "extensionAttributes"
BiomedicalConceptProperty ||--|| AliasCode : "code"
BiomedicalConceptProperty ||--}o CommentAnnotation : "notes"
BiomedicalConceptProperty ||--}o ExtensionAttribute : "extensionAttributes"
BiomedicalConceptProperty ||--}o ResponseCode : "responseCodes"
BiomedicalConceptSurrogate ||--}o CommentAnnotation : "notes"
BiomedicalConceptSurrogate ||--}o ExtensionAttribute : "extensionAttributes"
BiospecimenRetention ||--}o ExtensionAttribute : "extensionAttributes"
Characteristic ||--}o CommentAnnotation : "notes"
Characteristic ||--}o ExtensionAttribute : "extensionAttributes"
Code ||--}o ExtensionAttribute : "extensionAttributes"
CommentAnnotation ||--}o Code : "codes"
CommentAnnotation ||--}o ExtensionAttribute : "extensionAttributes"
Condition ||--}o CommentAnnotation : "notes"
Condition ||--}o ExtensionAttribute : "extensionAttributes"
ConditionAssignment ||--}o ExtensionAttribute : "extensionAttributes"
DocumentContentReference ||--}o ExtensionAttribute : "extensionAttributes"
Duration ||--|o Any : "quantity"
Duration ||--}o ExtensionAttribute : "extensionAttributes"
EligibilityCriterion ||--|| Code : "category"
EligibilityCriterion ||--}o CommentAnnotation : "notes"
EligibilityCriterion ||--}o ExtensionAttribute : "extensionAttributes"
EligibilityCriterionItem ||--}o CommentAnnotation : "notes"
EligibilityCriterionItem ||--}o ExtensionAttribute : "extensionAttributes"
Encounter ||--|o TransitionRule : "transitionEndRule, transitionStartRule"
Encounter ||--|| Code : "type"
Encounter ||--}o Code : "contactModes, environmentalSettings"
Encounter ||--}o CommentAnnotation : "notes"
Encounter ||--}o ExtensionAttribute : "extensionAttributes"
Endpoint ||--|| Code : "level"
Endpoint ||--}o CommentAnnotation : "notes"
Endpoint ||--}o ExtensionAttribute : "extensionAttributes"
Estimand ||--}o CommentAnnotation : "notes"
Estimand ||--}o ExtensionAttribute : "extensionAttributes"
Estimand ||--}| IntercurrentEvent : "intercurrentEvents"
ExtensionAttribute ||--|o AliasCode : "valueAliasCode"
ExtensionAttribute ||--|o Code : "valueCode"
ExtensionAttribute ||--|o ExtensionClass : "valueExtensionClass"
ExtensionAttribute ||--|o Quantity : "valueQuantity"
ExtensionAttribute ||--|o Range : "valueRange"
ExtensionAttribute ||--}o ExtensionAttribute : "extensionAttributes"
ExtensionClass ||--}| ExtensionAttribute : "extensionAttributes"
GeographicScope ||--|o AliasCode : "code"
GeographicScope ||--|| Code : "type"
GeographicScope ||--}o ExtensionAttribute : "extensionAttributes"
GovernanceDate ||--|| Code : "type"
GovernanceDate ||--}o ExtensionAttribute : "extensionAttributes"
GovernanceDate ||--}| GeographicScope : "geographicScopes"
Indication ||--}o Code : "codes"
Indication ||--}o CommentAnnotation : "notes"
Indication ||--}o ExtensionAttribute : "extensionAttributes"
Ingredient ||--|| Code : "role"
Ingredient ||--|| Substance : "substance"
Ingredient ||--}o ExtensionAttribute : "extensionAttributes"
IntercurrentEvent ||--}o CommentAnnotation : "notes"
IntercurrentEvent ||--}o ExtensionAttribute : "extensionAttributes"
InterventionalStudyDesign ||--|o AliasCode : "blindingSchema, studyPhase"
InterventionalStudyDesign ||--|o Code : "studyType"
InterventionalStudyDesign ||--|| Code : "model"
InterventionalStudyDesign ||--|| StudyDesignPopulation : "population"
InterventionalStudyDesign ||--}o Activity : "activities"
InterventionalStudyDesign ||--}o AnalysisPopulation : "analysisPopulations"
InterventionalStudyDesign ||--}o BiospecimenRetention : "biospecimenRetentions"
InterventionalStudyDesign ||--}o Code : "characteristics, intentTypes, subTypes, therapeuticAreas"
InterventionalStudyDesign ||--}o CommentAnnotation : "notes"
InterventionalStudyDesign ||--}o Encounter : "encounters"
InterventionalStudyDesign ||--}o Estimand : "estimands"
InterventionalStudyDesign ||--}o ExtensionAttribute : "extensionAttributes"
InterventionalStudyDesign ||--}o Indication : "indications"
InterventionalStudyDesign ||--}o Objective : "objectives"
InterventionalStudyDesign ||--}o ScheduleTimeline : "scheduleTimelines"
InterventionalStudyDesign ||--}o StudyElement : "elements"
InterventionalStudyDesign ||--}| EligibilityCriterion : "eligibilityCriteria"
InterventionalStudyDesign ||--}| StudyArm : "arms"
InterventionalStudyDesign ||--}| StudyCell : "studyCells"
InterventionalStudyDesign ||--}| StudyEpoch : "epochs"
Masking ||--}o ExtensionAttribute : "extensionAttributes"
MedicalDevice ||--|o Code : "sourcing"
MedicalDevice ||--}o CommentAnnotation : "notes"
MedicalDevice ||--}o ExtensionAttribute : "extensionAttributes"
MedicalDevice ||--}o MedicalDeviceIdentifier : "identifiers"
MedicalDeviceIdentifier ||--|| Code : "type"
MedicalDeviceIdentifier ||--}o ExtensionAttribute : "extensionAttributes"
NarrativeContent ||--}o ExtensionAttribute : "extensionAttributes"
NarrativeContentItem ||--}o ExtensionAttribute : "extensionAttributes"
Objective ||--|| Code : "level"
Objective ||--}o CommentAnnotation : "notes"
Objective ||--}o Endpoint : "endpoints"
Objective ||--}o ExtensionAttribute : "extensionAttributes"
ObservationalStudyDesign ||--|o AliasCode : "studyPhase"
ObservationalStudyDesign ||--|o Code : "samplingMethod, studyType"
ObservationalStudyDesign ||--|| Code : "model, timePerspective"
ObservationalStudyDesign ||--|| StudyDesignPopulation : "population"
ObservationalStudyDesign ||--}o Activity : "activities"
ObservationalStudyDesign ||--}o AnalysisPopulation : "analysisPopulations"
ObservationalStudyDesign ||--}o BiospecimenRetention : "biospecimenRetentions"
ObservationalStudyDesign ||--}o Code : "characteristics, subTypes, therapeuticAreas"
ObservationalStudyDesign ||--}o CommentAnnotation : "notes"
ObservationalStudyDesign ||--}o Encounter : "encounters"
ObservationalStudyDesign ||--}o Estimand : "estimands"
ObservationalStudyDesign ||--}o ExtensionAttribute : "extensionAttributes"
ObservationalStudyDesign ||--}o Indication : "indications"
ObservationalStudyDesign ||--}o Objective : "objectives"
ObservationalStudyDesign ||--}o ScheduleTimeline : "scheduleTimelines"
ObservationalStudyDesign ||--}o StudyElement : "elements"
ObservationalStudyDesign ||--}| EligibilityCriterion : "eligibilityCriteria"
ObservationalStudyDesign ||--}| StudyArm : "arms"
ObservationalStudyDesign ||--}| StudyCell : "studyCells"
ObservationalStudyDesign ||--}| StudyEpoch : "epochs"
Organization ||--|o Address : "legalAddress"
Organization ||--|| Code : "type"
Organization ||--}o ExtensionAttribute : "extensionAttributes"
Organization ||--}o StudySite : "managedSites"
ParameterMap ||--}o ExtensionAttribute : "extensionAttributes"
PersonName ||--}o ExtensionAttribute : "extensionAttributes"
Procedure ||--|| Code : "code"
Procedure ||--}o CommentAnnotation : "notes"
Procedure ||--}o ExtensionAttribute : "extensionAttributes"
ProductOrganizationRole ||--|| Code : "code"
ProductOrganizationRole ||--}o ExtensionAttribute : "extensionAttributes"
Quantity ||--|o AliasCode : "unit"
Quantity ||--}o ExtensionAttribute : "extensionAttributes"
Range ||--|| Quantity : "maxValue, minValue"
Range ||--}o ExtensionAttribute : "extensionAttributes"
ReferenceIdentifier ||--|| Code : "type"
ReferenceIdentifier ||--}o ExtensionAttribute : "extensionAttributes"
ResponseCode ||--|| Code : "code"
ResponseCode ||--}o ExtensionAttribute : "extensionAttributes"
ScheduleTimeline ||--|o Duration : "plannedDuration"
ScheduleTimeline ||--}o Any : "instances"
ScheduleTimeline ||--}o ExtensionAttribute : "extensionAttributes"
ScheduleTimeline ||--}o ScheduleTimelineExit : "exits"
ScheduleTimeline ||--}o Timing : "timings"
ScheduleTimelineExit ||--}o ExtensionAttribute : "extensionAttributes"
ScheduledActivityInstance ||--}o ExtensionAttribute : "extensionAttributes"
ScheduledDecisionInstance ||--}o ExtensionAttribute : "extensionAttributes"
ScheduledDecisionInstance ||--}| ConditionAssignment : "conditionAssignments"
Strength ||--|o Quantity : "denominator"
Strength ||--|| Any : "numerator"
Strength ||--}o ExtensionAttribute : "extensionAttributes"
Study ||--}o ExtensionAttribute : "extensionAttributes"
Study ||--}o StudyDefinitionDocument : "documentedBy"
Study ||--}o StudyVersion : "versions"
StudyAmendment ||--|| StudyAmendmentReason : "primaryReason"
StudyAmendment ||--}o CommentAnnotation : "notes"
StudyAmendment ||--}o ExtensionAttribute : "extensionAttributes"
StudyAmendment ||--}o GovernanceDate : "dateValues"
StudyAmendment ||--}o StudyAmendmentImpact : "impacts"
StudyAmendment ||--}o StudyAmendmentReason : "secondaryReasons"
StudyAmendment ||--}o SubjectEnrollment : "enrollments"
StudyAmendment ||--}| GeographicScope : "geographicScopes"
StudyAmendment ||--}| StudyChange : "changes"
StudyAmendmentImpact ||--|| Code : "type"
StudyAmendmentImpact ||--}o CommentAnnotation : "notes"
StudyAmendmentImpact ||--}o ExtensionAttribute : "extensionAttributes"
StudyAmendmentReason ||--|| Code : "code"
StudyAmendmentReason ||--}o ExtensionAttribute : "extensionAttributes"
StudyArm ||--|| Code : "dataOriginType, type"
StudyArm ||--}o CommentAnnotation : "notes"
StudyArm ||--}o ExtensionAttribute : "extensionAttributes"
StudyCell ||--}o ExtensionAttribute : "extensionAttributes"
StudyChange ||--}o ExtensionAttribute : "extensionAttributes"
StudyChange ||--}| DocumentContentReference : "changedSections"
StudyCohort ||--|o Any : "plannedCompletionNumber, plannedEnrollmentNumber"
StudyCohort ||--|o Range : "plannedAge"
StudyCohort ||--}o Characteristic : "characteristics"
StudyCohort ||--}o Code : "plannedSex"
StudyCohort ||--}o CommentAnnotation : "notes"
StudyCohort ||--}o ExtensionAttribute : "extensionAttributes"
StudyDefinitionDocument ||--|| Code : "language, type"
StudyDefinitionDocument ||--}o CommentAnnotation : "notes"
StudyDefinitionDocument ||--}o ExtensionAttribute : "extensionAttributes"
StudyDefinitionDocument ||--}o StudyDefinitionDocumentVersion : "versions"
StudyDefinitionDocumentVersion ||--|| Code : "status"
StudyDefinitionDocumentVersion ||--}o CommentAnnotation : "notes"
StudyDefinitionDocumentVersion ||--}o ExtensionAttribute : "extensionAttributes"
StudyDefinitionDocumentVersion ||--}o GovernanceDate : "dateValues"
StudyDefinitionDocumentVersion ||--}o NarrativeContent : "contents"
StudyDesignPopulation ||--|o Any : "plannedCompletionNumber, plannedEnrollmentNumber"
StudyDesignPopulation ||--|o Range : "plannedAge"
StudyDesignPopulation ||--}o Code : "plannedSex"
StudyDesignPopulation ||--}o CommentAnnotation : "notes"
StudyDesignPopulation ||--}o ExtensionAttribute : "extensionAttributes"
StudyDesignPopulation ||--}o StudyCohort : "cohorts"
StudyElement ||--|o TransitionRule : "transitionEndRule, transitionStartRule"
StudyElement ||--}o CommentAnnotation : "notes"
StudyElement ||--}o ExtensionAttribute : "extensionAttributes"
StudyEpoch ||--|| Code : "type"
StudyEpoch ||--}o CommentAnnotation : "notes"
StudyEpoch ||--}o ExtensionAttribute : "extensionAttributes"
StudyIdentifier ||--}o ExtensionAttribute : "extensionAttributes"
StudyIntervention ||--|o Quantity : "minimumResponseDuration"
StudyIntervention ||--|| Code : "role, type"
StudyIntervention ||--}o Administration : "administrations"
StudyIntervention ||--}o Code : "codes"
StudyIntervention ||--}o CommentAnnotation : "notes"
StudyIntervention ||--}o ExtensionAttribute : "extensionAttributes"
StudyRole ||--|o Masking : "masking"
StudyRole ||--|| Code : "code"
StudyRole ||--}o AssignedPerson : "assignedPersons"
StudyRole ||--}o CommentAnnotation : "notes"
StudyRole ||--}o ExtensionAttribute : "extensionAttributes"
StudySite ||--|| Code : "country"
StudySite ||--}o ExtensionAttribute : "extensionAttributes"
StudyTitle ||--|| Code : "type"
StudyTitle ||--}o ExtensionAttribute : "extensionAttributes"
StudyVersion ||--}o Abbreviation : "abbreviations"
StudyVersion ||--}o AdministrableProduct : "administrableProducts"
StudyVersion ||--}o Any : "studyDesigns"
StudyVersion ||--}o BiomedicalConcept : "biomedicalConcepts"
StudyVersion ||--}o BiomedicalConceptCategory : "bcCategories"
StudyVersion ||--}o BiomedicalConceptSurrogate : "bcSurrogates"
StudyVersion ||--}o Code : "businessTherapeuticAreas"
StudyVersion ||--}o CommentAnnotation : "notes"
StudyVersion ||--}o Condition : "conditions"
StudyVersion ||--}o EligibilityCriterionItem : "eligibilityCriterionItems"
StudyVersion ||--}o ExtensionAttribute : "extensionAttributes"
StudyVersion ||--}o GovernanceDate : "dateValues"
StudyVersion ||--}o MedicalDevice : "medicalDevices"
StudyVersion ||--}o NarrativeContentItem : "narrativeContentItems"
StudyVersion ||--}o Organization : "organizations"
StudyVersion ||--}o ProductOrganizationRole : "productOrganizationRoles"
StudyVersion ||--}o ReferenceIdentifier : "referenceIdentifiers"
StudyVersion ||--}o StudyAmendment : "amendments"
StudyVersion ||--}o StudyIntervention : "studyInterventions"
StudyVersion ||--}o StudyRole : "roles"
StudyVersion ||--}o SyntaxTemplateDictionary : "dictionaries"
StudyVersion ||--}| StudyIdentifier : "studyIdentifiers"
StudyVersion ||--}| StudyTitle : "titles"
SubjectEnrollment ||--|o GeographicScope : "forGeographicScope"
SubjectEnrollment ||--|| Quantity : "quantity"
SubjectEnrollment ||--}o ExtensionAttribute : "extensionAttributes"
Substance ||--|o Substance : "referenceSubstance"
Substance ||--}o Code : "codes"
Substance ||--}o ExtensionAttribute : "extensionAttributes"
Substance ||--}| Strength : "strengths"
SyntaxTemplateDictionary ||--}o ExtensionAttribute : "extensionAttributes"
SyntaxTemplateDictionary ||--}| ParameterMap : "parameterMaps"
Timing ||--|| Code : "relativeToFrom, type"
Timing ||--}o ExtensionAttribute : "extensionAttributes"
TransitionRule ||--}o ExtensionAttribute : "extensionAttributes"
Wrapper ||--|| Study : "study"

```

