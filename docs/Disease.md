---
layout: default
---

## disease


None

URI: [http://bioentity.io/vocab/Disease](http://bioentity.io/vocab/Disease)


![img](http://yuml.me/diagram/nofunky/class/%5Bdisease%20or%20phenotypic%20feature%5D%5E-%5Bdisease%5D%2C%20%5Bdisease%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D)
## Mappings

 * [MONDO:0000001](http://purl.obolibrary.org/obo/MONDO_0000001)
 * [WD:Q12136](http://purl.obolibrary.org/obo/WD_Q12136)
 * [SIO:010299](http://semanticscience.org/resource/SIO_010299)
 * [UMLSSG:DISO](http://purl.obolibrary.org/obo/UMLSSG_DISO)

## Inheritance

 *  is_a: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html)

## Children


## Used in

 *  class: [disease to thing association](DiseaseToThingAssociation.html) references: [disease](Disease.html)
 *  class: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html) references: [disease](Disease.html)
 *  class: [gene to disease association](GeneToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [variant to disease association](VariantToDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html) references: [disease](Disease.html)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html) references: [disease](Disease.html)

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
