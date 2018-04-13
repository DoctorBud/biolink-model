---
layout: default
---

## case


An individual organism that has a patient role in some clinical context.

URI: [http://bioentity.io/vocab/Case](http://bioentity.io/vocab/Case)


![img](http://yuml.me/diagram/nofunky/class/%5Bindividual%20organism%5D%5E-%5Bcase%5D%2C%20%5Bcase%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings


## Inheritance

 *  is_a: [individual organism](IndividualOrganism.html)

## Children


## Used in

 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
