# Modularité et initiation à la Programmation Orientée Objet

Quand nous utilisons certaines fonctions où certains objets Python, qu'ils soient *built-in* ou bien importés à partir de *modules*, nous nous posons rarement la question de savoir quelle est leur **implémentation**, c'est-à-dire la manière dont-ils ont été conçu et programmé. Nous faisons globalement confiance aux concepteurs du langage ou du module. 

Ce qui nous importe est plutôt **l'interface** de ces objets, c'est-à-dire la façon dont nous pouvons interagir avec ces objets : les créer, les affecter, les additionner, les supprimer,...

Dans cette partie nous verrons comment créer un module, le documenter, et définir une interface claire. Nous verrons les prémices d'un nouveau **paradigme de programmation** : la Programmation Orientée Objet(**POO**).

*La suite de cette partie est grandement inspirée de [Numériques et Sciences Informatique, 24 leçons avec exercices corrigé, Ellipse](https://www.editions-ellipses.fr/accueil/10445-specialite-numerique-et-sciences-informatiques-lecons-avec-exercices-corriges-terminale-nouveaux-programmes-9782340038554.html)*

## Un premier problème

!!! abstract 
	Voici une propriété probabiliste peu intuitive : il suffit d'avoir un groupe de
	23 personnes pour que la probabilité que deux personnes aient la même date
	d'anniversaire soit supérieure à 50%.
	
Nous allons construire un programme Python qui permettra de vérifier expérimentalement cette propriété.

Pour modéliser le problème :

* plutôt que d'utiliser des dates, nous allons utiliser des entiers de 1 à 365 ;
* nous allons créer une fonction ``genere_groupe()`` qui renvoie un tableau aléatoire de 23 entiers de 1 à 365 ;
* nous allons créer une fonction ``contient_doublon(t)`` qui renverra `True` si le tableau contient un doublon, et ``False`` sinon ;
* puis nous créerons une fonction ``teste_hypothese()`` qui testera sur un échantillon de 100 groupes la présence d'un doublon ou non, et renverra le nombre de groupes ayant eu des doublons.

!!! question "Exercice"
	Créer un fichier ``recherchesDates.py`` et **implémenter** les fonctions précédentes.
	Des solutions sont proposées dans les parties ci-dessous, mais vous **devez d'abord tester par vous-mêmes**.

??? done "Solution"
	=== "``genere_groupe()``"
		``` python
		from random import randint
		
		def genere_groupe() :
			"""fonction renvoyant un tableau de 23 nombres aléatoires entre 1 et 365"""
			return [randint(1,365) for _ in range(23)]
		```
	=== "``contient_doublon(t)``"
		``` python
		def contient_doublon(t) :
			"""fonction renvoyant un booléen signalant la présence ou non d'un doublon dans le tableau"""
			s = [] # s est un tableau temporaire contenant les valeurs testées
			for data in t :
				if data in s : # si data est déjà dans s, alors c'est un doublon
					return True
				else : # sinon on ajoute data à la liste des valeurs testées.
					s.append(data)
			return False
			
		```
	=== "``teste_hypothese()``"
		``` python
		def teste_hypothese() :
			"""fonction renvoyant le nombre de groupes contenant un doublon
			sur un échantillon de 100 groupes"""
			nbDoublons = 0 
			for _ in range(100) :
				t = genere_groupe()
				if contient_doublon(t) :
					nbDoublons +=1
			return nbDoublons
		```



	
