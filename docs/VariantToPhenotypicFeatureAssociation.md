---
layout: default
---

## variant to phenotypic feature association


None

URI: [http://bioentity.io/vocab/VariantToPhenotypicFeatureAssociation](http://bioentity.io/vocab/VariantToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/%5Bassociation%5D%5E-%5Bvariant%20to%20phenotypic%20feature%20association%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-association%20type%20%3E%5Bontology%20class%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-subject%20%3E%5Bsequence%20variant%5D%2C%20%5Bgenomic%20entity%5D%5E-%5Bsequence%20variant%5D%2C%20%5Bsequence%20variant%5D-has%20gene%20%3E%5Bgene%5D%2C%20%5Bgene%20or%20gene%20product%5D%5E-%5Bgene%5D%2C%20%5Bgene%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Bsequence%20variant%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-relation%20%3E%5Brelationship%20type%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-object%20%3E%5Bphenotypic%20feature%5D%2C%20%5Bdisease%20or%20phenotypic%20feature%5D%5E-%5Bphenotypic%20feature%5D%2C%20%5Bphenotypic%20feature%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-qualifiers%20%3E%5Bontology%20class%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-publications%20%3E%5Bpublication%5D%2C%20%5Binformation%20content%20entity%5D%5E-%5Bpublication%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-provided%20by%20%3E%5Bprovider%5D%2C%20%5Badministrative%20entity%5D%5E-%5Bprovider%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-frequency%20qualifier%20%3E%5Bfrequency%20value%5D%2C%20%5Battribute%5D%5E-%5Bfrequency%20value%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-severity%20qualifier%20%3E%5Bseverity%20value%5D%2C%20%5Battribute%5D%5E-%5Bseverity%20value%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-onset%20qualifier%20%3E%5Bonset%5D%2C%20%5Battribute%5D%5E-%5Bonset%5D%2C%20%5Bvariant%20to%20phenotypic%20feature%20association%5D-sex%20qualifier%20%3E%5Bbiological%20sex%5D%2C%20%5Battribute%5D%5E-%5Bbiological%20sex%5D)
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [variant to thing association](VariantToThingAssociation.html)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _a sequence variant in which the allele state is associated in some way with the phenotype state_
    * __range__: [sequence variant](SequenceVariant.html) [required]
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
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [phenotypic feature](PhenotypicFeature.html) [required]
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
