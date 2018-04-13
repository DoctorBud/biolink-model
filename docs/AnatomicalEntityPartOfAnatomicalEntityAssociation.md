---
layout: default
---

## anatomical entity part of anatomical entity association


None

URI: [http://bioentity.io/vocab/AnatomicalEntityPartOfAnatomicalEntityAssociation](http://bioentity.io/vocab/AnatomicalEntityPartOfAnatomicalEntityAssociation)


![img](http://yuml.me/diagram/nofunky/class/%5Banatomical%20entity%20to%20anatomical%20entity%20association%5D%5E-%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-association%20type%20%3E%5Bontology%20class%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-subject%20%3E%5Banatomical%20entity%5D%2C%20%5Borganismal%20entity%5D%5E-%5Banatomical%20entity%5D%2C%20%5Banatomical%20entity%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-relation%20%3E%5Banatomical%20entity%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-object%20%3E%5Banatomical%20entity%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-qualifiers%20%3E%5Bontology%20class%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-publications%20%3E%5Bpublication%5D%2C%20%5Binformation%20content%20entity%5D%5E-%5Bpublication%5D%2C%20%5Banatomical%20entity%20part%20of%20anatomical%20entity%20association%5D-provided%20by%20%3E%5Bprovider%5D%2C%20%5Badministrative%20entity%5D%5E-%5Bprovider%5D)
## Mappings


## Inheritance

 *  is_a: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _the part_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the whole_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _the whole_
    * __range__: [anatomical entity](AnatomicalEntity.html) [required]
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
