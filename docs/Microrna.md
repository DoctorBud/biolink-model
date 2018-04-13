---
layout: default
---

## microRNA


None

URI: [http://bioentity.io/vocab/Microrna](http://bioentity.io/vocab/Microrna)


![img](http://yuml.me/diagram/nofunky/class/%5Bnoncoding%20RNA%20product%5D%5E-%5BmicroRNA%5D%2C%20%5BmicroRNA%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [SO:0000276](http://purl.obolibrary.org/obo/SO_0000276)
 * [SIO:001397](http://semanticscience.org/resource/SIO_001397)
 * [WD:Q310899](http://purl.obolibrary.org/obo/WD_Q310899)

## Inheritance

 *  is_a: [noncoding RNA product](NoncodingRnaProduct.html)

## Children



## Fields

 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * inherited from: [genomic entity](GenomicEntity.html)
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
