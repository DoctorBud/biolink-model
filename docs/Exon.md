---
layout: default
---

## exon


A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing

URI: [http://bioentity.io/vocab/Exon](http://bioentity.io/vocab/Exon)


![img](http://yuml.me/diagram/nofunky/class/%5Bgenomic%20entity%5D%5E-%5Bexon%5D%2C%20%5Bexon%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [SO:0000147](http://purl.obolibrary.org/obo/SO_0000147)
 * [SIO:010445](http://semanticscience.org/resource/SIO_010445)
 * [WD:Q373027](http://purl.obolibrary.org/obo/WD_Q373027)

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children


## Used in

 *  class: [exon to transcript relationship](ExonToTranscriptRelationship.html) references: [exon](Exon.html)

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
