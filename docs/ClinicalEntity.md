---
layout: default
---

## clinical entity


Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities

URI: [http://bioentity.io/vocab/ClinicalEntity](http://bioentity.io/vocab/ClinicalEntity)


![img](http://yuml.me/diagram/nofunky/class/%5Bnamed%20thing%5D%5E-%5Bclinical%20entity%5D)
## Mappings


## Inheritance

 *  is_a: [named thing](NamedThing.html)

## Children

 *  child: [clinical trial](ClinicalTrial.html)
 *  child: [clinical intervention](ClinicalIntervention.html)


## Fields

 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
