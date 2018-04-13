---
layout: default
---

## gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [http://bioentity.io/vocab/GeneOrGeneProduct](http://bioentity.io/vocab/GeneOrGeneProduct)


![img](http://yuml.me/diagram/nofunky/class/%5Bgenomic%20entity%5D%5E-%5Bgene%20or%20gene%20product%5D%2C%20%5Bgene%20or%20gene%20product%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings


## Inheritance

 *  is_a: [genomic entity](GenomicEntity.html)

## Children

 *  child: [gene](Gene.html)
 *  child: [gene product](GeneProduct.html)

## Used in

 *  class: [sequence variant](SequenceVariant.html) references: [gene](Gene.html)
 *  class: [genotype to gene association](GenotypeToGeneAssociation.html) references: [gene](Gene.html)
 *  class: [gene to gene association](GeneToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to gene homology association](GeneToGeneHomologyAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene product](GeneProduct.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to thing association](GeneToThingAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [gene or gene product](GeneOrGeneProduct.html)
 *  class: [transcript to gene relationship](TranscriptToGeneRelationship.html) references: [gene](Gene.html)
 *  class: [gene to gene product relationship](GeneToGeneProductRelationship.html) references: [gene](Gene.html)
 *  class: [gene regulatory relationship](GeneRegulatoryRelationship.html) references: [gene or gene product](GeneOrGeneProduct.html)

## Fields

 * [has biological sequence](has_biological_sequence.html)
    * _connects a genomic feature to its sequence_
    * __range__: biological sequence
    * inherited from: [genomic entity](GenomicEntity.html)
 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _genes are typically designated by a short symbol and a full name. We map the symbol to the default display label and use an additional slot for full name_
    * __range__: symbol type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
