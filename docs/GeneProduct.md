---
layout: default
---

## gene product


The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

URI: [http://bioentity.io/vocab/GeneProduct](http://bioentity.io/vocab/GeneProduct)


![img](http://yuml.me/diagram/nofunky/class/%5Bgene%20or%20gene%20product%5D%5E-%5Bgene%20product%5D%2C%20%5Bgene%20product%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [WD:Q424689](http://purl.obolibrary.org/obo/WD_Q424689)

## Inheritance

 *  is_a: [gene or gene product](GeneOrGeneProduct.html)

## Children

 *  child: [protein](Protein.html)
 *  child: [gene product isoform](GeneProductIsoform.html)
 *  child: [RNA product](RnaProduct.html)

## Used in

 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene product](GeneProduct.html)

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
