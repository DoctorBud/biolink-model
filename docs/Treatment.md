---
layout: default
---

## treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [http://bioentity.io/vocab/Treatment](http://bioentity.io/vocab/Treatment)


![img](http://yuml.me/diagram/nofunky/class/%5Benvironment%5D%5E-%5Btreatment%5D%2C%20%5Btreatment%5D-treats%20%3E%5Bdisease%20or%20phenotypic%20feature%5D%2C%20%5Bbiological%20entity%5D%5E-%5Bdisease%20or%20phenotypic%20feature%5D%2C%20%5Bdisease%20or%20phenotypic%20feature%5D-in%20taxon%20%3E%5Borganism%20taxon%5D%2C%20%5Bontology%20class%5D%5E-%5Borganism%20taxon%5D%2C%20%5Btreatment%5D-has%20exposure%20parts%20%3E%5Bdrug%20exposure%5D%2C%20%5Benvironment%5D%5E-%5Bdrug%20exposure%5D)
## Mappings

 * [OGMS:0000090](http://purl.obolibrary.org/obo/OGMS_0000090)
 * [SIO:001398](http://semanticscience.org/resource/SIO_001398)

## Inheritance

 *  is_a: [environment](Environment.html)

## Children


## Used in

 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html) references: [treatment](Treatment.html)

## Fields

 * [treats](treats.html)
    * __range__: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) [required]
    * __Local__
 * [has exposure parts](has_exposure_parts.html)
    * __range__: [drug exposure](DrugExposure.html) [required]
    * __Local__
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
