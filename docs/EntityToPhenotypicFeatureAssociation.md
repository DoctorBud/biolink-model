---
layout: default
---

## entity to phenotypic feature association


None

URI: [http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation](http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/%5Bassociation%5D%5E-%5Bentity%20to%20phenotypic%20feature%20association%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-frequency%20qualifier%20%3E%5Bfrequency%20value%5D%2C%20%5Battribute%5D%5E-%5Bfrequency%20value%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-severity%20qualifier%20%3E%5Bseverity%20value%5D%2C%20%5Battribute%5D%5E-%5Bseverity%20value%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-onset%20qualifier%20%3E%5Bonset%5D%2C%20%5Battribute%5D%5E-%5Bonset%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-sex%20qualifier%20%3E%5Bbiological%20sex%5D%2C%20%5Battribute%5D%5E-%5Bbiological%20sex%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-association%20type%20%3E%5Bontology%20class%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-relation%20%3E%5Brelationship%20type%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-object%20%3E%5Bphenotypic%20feature%5D%2C%20%5Bdisease%20or%20phenotypic%20feature%5D%5E-%5Bphenotypic%20feature%5D%2C%20%5Bphenotypic%20feature%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-qualifiers%20%3E%5Bontology%20class%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-publications%20%3E%5Bpublication%5D%2C%20%5Binformation%20content%20entity%5D%5E-%5Bpublication%5D%2C%20%5Bentity%20to%20phenotypic%20feature%20association%5D-provided%20by%20%3E%5Bprovider%5D%2C%20%5Badministrative%20entity%5D%5E-%5Bprovider%5D)
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html)
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html)
 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html)
 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html)
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html)
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html)


## Fields

 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * __Local__
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * __Local__
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * __Local__
 * [sex qualifier](sex_qualifier.html)
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * __range__: [biological sex](BiologicalSex.html)
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: None [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _phenotypic class_
    * __range__: [phenotypic feature](PhenotypicFeature.html) [required]
    * Example: [HP:0002487](http://purl.obolibrary.org/obo/HP_0002487) Hyperkinesis
    * Example: [WBPhenotype:0000180](http://purl.obolibrary.org/obo/WBPhenotype_0000180) axon morphology variant
    * Example: [MP:0001569](http://purl.obolibrary.org/obo/MP_0001569) abnormal circulating bilirubin level
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
