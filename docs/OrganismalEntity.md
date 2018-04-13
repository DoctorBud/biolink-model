---
layout: default
---

## organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [http://bioentity.io/vocab/OrganismalEntity](http://bioentity.io/vocab/OrganismalEntity)


![img](http://yuml.me/diagram/nofunky/class/%5Bbiological%20entity%5D%5E-%5Borganismal%20entity%5D)
## Mappings

 * [WD:Q7239](http://purl.obolibrary.org/obo/WD_Q7239)

## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)

## Children

 *  child: [individual organism](IndividualOrganism.html)
 *  child: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  child: [biosample](Biosample.html)
 *  child: [anatomical entity](AnatomicalEntity.html)
 *  child: [life stage](LifeStage.html)

## Used in

 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [life stage](LifeStage.html)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity part of anatomical entity association](AnatomicalEntityPartOfAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)

## Fields

 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
