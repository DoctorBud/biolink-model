---
layout: default
---

## phenotypic feature


None

URI: [http://bioentity.io/vocab/PhenotypicFeature](http://bioentity.io/vocab/PhenotypicFeature)


![img](http://yuml.me/diagram/nofunky/class/%5Bdisease%20or%20phenotypic%20feature%5D%5E-%5Bphenotypic%20feature%5D%2C%20%5Bphenotypic%20feature%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [UPHENO:0000001](http://purl.obolibrary.org/obo/UPHENO_0000001)
 * [SIO:010056](http://semanticscience.org/resource/SIO_010056)
 * [WD:Q169872](http://purl.obolibrary.org/obo/WD_Q169872)

## Inheritance

 *  is_a: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)

## Children


## Used in

 *  class: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)
 *  class: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html) references: [phenotypic feature](PhenotypicFeature.html)

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
