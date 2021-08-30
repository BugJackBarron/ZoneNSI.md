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
* nous allons créer une procédure (*une fonction sans paramètres*) ``genere_groupe()`` qui renvoie un tableau aléatoire de 23 entiers de 1 à 365 ;
* nous allons créer une fonction ``contient_doublon(t)`` qui renverra `True` si le tableau contient un doublon, et ``False`` sinon ;
* puis nous créerons une procédure ``teste_hypothese()`` qui testera sur un échantillon de 100 groupes la présence d'un doublon ou non, et renverra le nombre de groupes ayant eu des doublons.

!!! question "Exercice"
	Créer un fichier ``recherchesDates.py`` et **implémenter** les fonctions précédentes.
	Des solutions sont proposées dans les parties ci-dessous, mais vous {==**devez d'abord tester par vous-mêmes**==}.

??? done "Solutions"
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

??? info "Exécution dans Basthon"
	<iframe src="https://console.basthon.fr/?script=eJyFU8Fq4zAQPTuQfxiyhzpsKUnD7qHQ27JfsLdSgmyNExVlxkijQv9mr_kO_9iOLKdJSssKg-UnzZv3ZsZd4AMEQ1Zf7tBzkPHLkcxnVTWfWexgh4QBt7vAqcd6CQ_zGehaLBYdUyuOCQLSK78ZEkgEYhqPJoFFuN8A8aEJGMH44WiEXd4jSUBYAwpsfv5QosIYUFIgeJoU1OtbPV1CxwG24Cgr22F9v1k-z2dFWsskTtm2llPjmWr5v7yGWaUgQXQ7Mj6j3kAfhmNEahE4qWYCe6N3J1qwhiJ4PFl7VxzhEZ6e4ZtuMF6ZF8zVNGp3FIk05lHvr8ZjClEvRFEZsRBlj9aIyTblZCEv173jER5yJleAnM8Ox5fhb1EXb7XErMTtzSRlEn_muqjxn5DwfIA-4kSeretjXjgJlkyaQQvkXczAJw7urjPEO9P3SLbOwcurzv42mkgHqzQvx-N2_9az7DFOk1V93jetfRmkPFVlEuNFYS_dVjGFDAzHdq9nzo8N1HFbrU6RY_8qan6VmNzFFSjyYdI0omiqRG98-A0y7L6cwKq6pP_-uFZoKsIZ_wfGJR4o" width="100%" height="400"> </iframe>
	
??? info "Preuve mathématique"
	*Cette pruve est donnée à titre indicatif, et n'a ni à être connue, ni même à être comprise.*
	
	Considérons notre groupe de 23 personnes, et cherchons la probabilité que les 23 personnes **n'aient pas la même date anniversaire** :
	
	* la première peut avoir n'importe quel date anniversaire, donc 365 possibilité sur 365 dates possibles.
	* La deuxième ne peut pas avoir la même date que les deux premiers, donc 364 possibilités sur 365.
	* La troisième ne peut avoir la même date que les deux premiers, donc 363 possibilités sur 365.
	* ...
	* La $n-ième$ ne peut avoir la même date que les $n-1$ précédents, donc $365-(n-1)$ possibilités.
	* ...
	* La 23ème ne peut avoir la même date que les 22 précédents, donc $365-22 = 343$ possibilités.
	
	La probabilité cherchée est donc $p = \dfrac{365}{365} \times \dfrac{364}{365} \times ... \times \dfrac{343}{365} = \dfrac{365~!}{342~!.365^{23}}$ où $365~!$ est la factorielle de 365, soit la multiplication $365 \times 364 \times 363 \times ... \times 2 \times 1$.
	
	Or l'événement contraire de  *"les 23 personnes n'ont pas la même date anniversaire"* est l'événement *"au moins 2 personnes parmi les 23 ont la même date d'anniversaire"*. Donc sa probabilité est $p' = 1-p$ soit en calculant environ $0,5073$, soit $50,73$ \%.
	
	Plus d'informations peuvent être trouvées sur l'[article correspondant de wikipedia](https://fr.wikipedia.org/wiki/Paradoxe_des_anniversaires).




## Différentes solutions ?

Bien entendu, les solutions proposées ci-dessus ne sont pas uniques. Elles sont mêmes **non optimales** (p
	
