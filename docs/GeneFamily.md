---
layout: default
---

## gene family


any grouping of multiple genes or gene products related by common descent

URI: [http://bioentity.io/vocab/GeneFamily](http://bioentity.io/vocab/GeneFamily)


![img](http://yuml.me/diagram/nofunky/class/%5Bmolecular%20entity%5D%5E-%5Bgene%20family%5D%2C%20%5Bgene%20family%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [NCIT:C20130](http://purl.obolibrary.org/obo/NCIT_C20130)
 * [SIO:001380](http://semanticscience.org/resource/SIO_001380)
 * [WD:Q417841](http://purl.obolibrary.org/obo/WD_Q417841)

## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)
 *  mixin: [gene grouping](GeneGrouping.html)

## Children



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
