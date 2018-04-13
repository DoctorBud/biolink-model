---
layout: default
---

## protein


A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

URI: [http://bioentity.io/vocab/Protein](http://bioentity.io/vocab/Protein)


![img](http://yuml.me/diagram/nofunky/class/%5Bgene%20product%5D%5E-%5Bprotein%5D%2C%20%5Bprotein%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001)
 * [SIO:010043](http://semanticscience.org/resource/SIO_010043)
 * [WD:Q8054](http://purl.obolibrary.org/obo/WD_Q8054)

## Inheritance

 *  is_a: [gene product](GeneProduct.html)

## Children

 *  child: [protein isoform](ProteinIsoform.html)


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
