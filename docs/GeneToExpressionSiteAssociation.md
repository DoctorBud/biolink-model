---
layout: default
---

## gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [http://bioentity.io/vocab/GeneToExpressionSiteAssociation](http://bioentity.io/vocab/GeneToExpressionSiteAssociation)


![img](http://yuml.me/diagram/nofunky/class/%5Bassociation%5D%5E-%5Bgene%20to%20expression%20site%20association%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-stage%20qualifier%20%3E%5Blife%20stage%5D%2C%20%5Borganismal%20entity%5D%5E-%5Blife%20stage%5D%2C%20%5Blife%20stage%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-quantifier%20qualifier%20%3E%5Bontology%20class%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-association%20type%20%3E%5Bontology%20class%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-subject%20%3E%5Bgene%20or%20gene%20product%5D%2C%20%5Bgenomic%20entity%5D%5E-%5Bgene%20or%20gene%20product%5D%2C%20%5Bgene%20or%20gene%20product%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-relation%20%3E%5Brelationship%20type%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-object%20%3E%5Banatomical%20entity%5D%2C%20%5Borganismal%20entity%5D%5E-%5Banatomical%20entity%5D%2C%20%5Banatomical%20entity%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-qualifiers%20%3E%5Bontology%20class%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-publications%20%3E%5Bpublication%5D%2C%20%5Binformation%20content%20entity%5D%5E-%5Bpublication%5D%2C%20%5Bgene%20to%20expression%20site%20association%5D-provided%20by%20%3E%5Bprovider%5D%2C%20%5Badministrative%20entity%5D%5E-%5Bprovider%5D)
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children



## Fields

 * [stage qualifier](stage_qualifier.html)
    * _stage at which the gene is expressed in the site_
    * __range__: [life stage](LifeStage.html)
    * Example: [UBERON:0000069](http://purl.obolibrary.org/obo/UBERON_0000069) larval stage
    * __Local__
 * [quantifier qualifier](quantifier_qualifier.html)
    * _can be used to indicate magnitude, or also ranking_
    * __range__: [ontology class](OntologyClass.html)
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _gene in which variation is correlated with the phenotypic feature_
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _expression relationship_
    * __range__: [relationship type](RelationshipType.html) [required]
    * subproperty_of: [RO:0002206](http://purl.obolibrary.org/obo/RO_0002206)
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _location in which the gene is expressed_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
    * Example: [UBERON:0002037](http://purl.obolibrary.org/obo/UBERON_0002037) cerebellum
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
