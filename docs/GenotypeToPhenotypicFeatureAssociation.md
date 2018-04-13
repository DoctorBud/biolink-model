---
layout: default
---

## genotype to phenotypic feature association


Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment

URI: [http://bioentity.io/vocab/GenotypeToPhenotypicFeatureAssociation](http://bioentity.io/vocab/GenotypeToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/%5Bassociation%5D%5E-%5Bgenotype%20to%20phenotypic%20feature%20association%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-association%20type%20%3E%5Bontology%20class%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-subject%20%3E%5Bgenotype%5D%2C%20%5Bgenomic%20entity%5D%5E-%5Bgenotype%5D%2C%20%5Bgenotype%5D-has%20zygosity%20%3E%5Bzygosity%5D%2C%20%5Battribute%5D%5E-%5Bzygosity%5D%2C%20%5Bgenotype%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-relation%20%3E%5Brelationship%20type%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-object%20%3E%5Bphenotypic%20feature%5D%2C%20%5Bdisease%20or%20phenotypic%20feature%5D%5E-%5Bphenotypic%20feature%5D%2C%20%5Bphenotypic%20feature%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-qualifiers%20%3E%5Bontology%20class%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-publications%20%3E%5Bpublication%5D%2C%20%5Binformation%20content%20entity%5D%5E-%5Bpublication%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-provided%20by%20%3E%5Bprovider%5D%2C%20%5Badministrative%20entity%5D%5E-%5Bprovider%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-frequency%20qualifier%20%3E%5Bfrequency%20value%5D%2C%20%5Battribute%5D%5E-%5Bfrequency%20value%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-severity%20qualifier%20%3E%5Bseverity%20value%5D%2C%20%5Battribute%5D%5E-%5Bseverity%20value%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-onset%20qualifier%20%3E%5Bonset%5D%2C%20%5Battribute%5D%5E-%5Bonset%5D%2C%20%5Bgenotype%20to%20phenotypic%20feature%20association%5D-sex%20qualifier%20%3E%5Bbiological%20sex%5D%2C%20%5Battribute%5D%5E-%5Bbiological%20sex%5D)
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 *  mixin: [genotype to thing association](GenotypeToThingAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _genotype that is associated with the phenotypic feature_
    * __range__: [genotype](Genotype.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * subproperty_of: [GENO:0000382](http://purl.obolibrary.org/obo/GENO_0000382)
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
 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [sex qualifier](sex_qualifier.html)
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * __range__: [biological sex](BiologicalSex.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
