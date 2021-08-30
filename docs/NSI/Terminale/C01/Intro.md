# Modularité et initiation à la Programmation Orientée Objet

Quand nous utilisons certaines fonctions où certains objets Python, qu'ils soient *built-in* ou bien importés à partir de *modules*, nous nous posons rarement la question de savoir quelle est leur **implémentation**, c'est-à-dire la manière dont-ils ont été conçu et programmé. Nous faisons globalement confiance aux concepteurs du langage ou du module. 

Ce qui nous importe est plutôt **l'interface** de ces objets, c'est-à-dire la façon dont nous pouvons interagir avec ces objets : les créer, les affecter, les additionner, les supprimer,...

Dans cette partie nous verrons comment créer un module, le documenter, et définir une interface claire. Nous verrons les prémices d'un nouveau **paradigme de programmation** : la Programmation Orientée Objet(**POO**).


## Un premier problème

!!! abstract 
	Voici une propriété probabiliste peu intuitive : il suffit d'avoir un groupe de
	23 personnes pour que la probabilité que deux personnes aient la même date
	d'anniversaire soit supérieure à 50%.
	
Nous allons construire un programme Python qui permettra de vérifier expérimentalement cette propriété.

