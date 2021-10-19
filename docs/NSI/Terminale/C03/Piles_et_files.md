# Piles et files

## Définitions et exemples

### Piles

!!! abstract "Définition"

	Une {==**pile**==} (*stack* en anglais) est une structure de donnée permettant de stocker un ensemble d'objets tout en respectant certaines règles d'insertion et de délétion :
	
	* un objet est ajouté toujours en haut de la pile (**empiler**);
	* quand on supprime un objet, il s'agit toujours du **dernier objet ajouté** (**dépiler**).
	
	On associe à cette structure l'image d'une *pile d'assiettes* :
	
	<p align="center">
	![pile 1](piles1.png){: style="width : 50%;"}
	</p>
	
	Un tel type de structure est souvent appelé :
	
	* *Dernier entré, premier sorti* (*DEPS*) en français ;
	* *Last in, first out* (*LIFO*) en anglais.
	
!!! abstract "Interface"
	Pour définir l'interface d'un objet de type **pile**, nous supposerons d'abord que les éléments de la pile sont tous du même type (la pile est **homogène**).
	
	Pour parler d'une pile d'éléments de type `T`, on utilisera la notation `Pile[T]`.
	
	L'interface sera simple puisque seulement 4 fonctions sont nécessaires : création d'une pile vide, empiler (*push* en anglais), dépiler (*pop* en anglais), et tester la *vacuité* d'une pile.
	
	| fonction|  description|
	|:---:| :--- |
	| `creer_pile() -> Pile[T]` | crée une pile vide |
	| `est_vide(p : Pile[T]) -> bool` | renvoie `True si l'objet `p` de`type `Pile[T]` est vide, `False` sinon. |
	| `empiler(e : T, p : Pile[T]) -> None` | ajoute l'élément `e` de type `T` au sommet de la pile `p`. |
	| `dépiler(p : Pile[T]) -> e : T` | retire et renvoie l'élément `e` de type `T` situé au sommet de la pile `p`. |
	
		
!!! example "Situations utilisant des piles"

	=== "Bouton retour dans un navigateur"
	
		Lors d'une navigation web, on utilise une pile pour stocker les différentes pages visitées les unes après les autres. Le bouton de retour a pour fonction de **dépiler** la pile ainsi constituée.
		
		Par exemple :
		<p align="center">
		![exemple retour](pileRetour.png){: style="width : 50%;"}
		</p>
	
	
	=== "Pile d'appels d'une fonction récursive"
	
		Une pile est crée lors des différents appels récursifs d'une fonction, et cette pile est dépilée à chaque retour de fonction.
		
		Par exemple, avec la fonction factorielle :
		<p align="center">
		![exemple factorielle](pileFacto.png){: style="width : 90%;"}
		</p>
	
		
	
	
	=== "Fonction « Annuler la frappe » d'un traitement de texte"
	
		De la même manière que pour le bouton retour d'une page web, les modifications apportées dans un traitement de texte sont stockées dans une pile. L'appui sur ++ctrl++ + Z a pour effet de dépiler, 
		et donc de rétablir le texte à la situation précédente sauvegardée dans la pile.
		
### Files

!!! abstract "Définition"
	
	Une {==**file**==} (*queue* en anglais) est une structure de donnée permettant de stocker un ensemble d'objets tout en respectant certaines règles d'insertion et de délétion :
	
	* un objet est ajouté toujours au début de la file (**enfiler**);
	* quand on supprime un objet, il s'agit toujours du **dernier objet de la file** (**défiler**).
	
	On associe à cette structure l'image d'une *file de personnes faisant la queue* :	

	<p align="center">
	![file 1](files1.png){: style="width : 70%;"}
	</p>
	
	
	Une filer est particulièrement adaptée aux *traitements séquentiels*.
	
	Un tel type de structure est souvent appelé :
	
	* *Premier entré, premier sorti* (*PEPS*) en français ;
	* *First in, first out* (*FIFO*) en anglais.
	
!!! abstract "Interface"

	Pour définir l'interface d'un objet de type **file**, nous supposerons d'abord que les éléments de la file sont tous du même type (la file est **homogène**).
	
	Pour parler d'une file d'éléments de type `T`, on utilisera la notation `File[T]`.
	
	L'interface sera simple puisque seulement 4 fonctions sont nécessaires : création d'une file vide, enfiler (*enqueue* en anglais), défiler (*dequeue* nen aglais), et tester la *vacuité* d'une file.
	
	| fonction|  description|
	|:---:| :--- |
	| `creer_file() -> File[T]` | crée une pile vide |
	| `est_vide(f : File[T]) -> bool` | renvoie `True si l'objet `f` de`type `File[T]` est vide, `False` sinon. |
	| `enfiler(e : T, f : File[T]) -> None` | ajoute l'élément `e` de type `T` à la fin de la file `f`. |
	| `defiler(f : File[T]) -> e : T` | retire et renvoie l'élément `e` de type `T` situé au début de la file `f`. |
	
!!! example "Situations utilisants une file"

	=== "Jeu de Bataille"
	
		Dans un jeu de bataille, chaque joueur possède une file de carte. On *défile* chaque paquet, compare les cartes, et le vainqueur *enfile* les cartes récoltées dans son paquet, jusqu'à ce qu'un des joueurs ait une file vide.
		
	=== "Serveurs d'impressions"
	
		Les serveurs d'impression traitent les requêtes dans l'ordre dans lequel elles arrivent, et les insèrent dans une file d'attente (dite aussi queue ou spool), lorsque d'autres travaux sont en exécution.
	
	=== "Mémoire tampon (*buffers*)"
		
		Une **mémoire tampon**, ou **buffer**, est une zone de mémoire vive qui va être utilisée pour stocker des données circulant entre deux périphériques ne fonctionnant pâs à la même vitesse, par exemple entre la connexion internet et le flux vidéo :
		
		* si la vitesse de connexion est supérieure au débit vidéo, le buffer va se remplir des données vidéo, et le lecteur vidéo les lira dans leur ordre d'arrivée (PEPS) ;
		* si le lecteur vidéo constate une chute du débit - il n'a plus de données à lire, il va attendre que la file du buffer atteigne une certaine taille afin de relancer une lecture vidéo plus fluide - c'est le *buffering*.
		

## Implémentations d'une Pile

### A partir d'une liste python


!!! question "Implémentation à partir du type `list`"
	=== "Enoncé"

		Compléter le code suivant afin qu'il corresponde à l'interface définie pour les piles, en utilisant le type `list` de python:
		
		``` python
					
		class Pile :
			def __init__(self) :
				...
				
			def est_vide(self) :
				...
				
			def empiler(self, v) :
				...
				
			def depiler(self) :
				...
		```
	=== "Une solution"
	
		``` python
					
		class Pile :
			def __init__(self) :
				self.p = []
				
			def est_vide(self) :
				return self.p == []
				
			def empiler(self, v) :
				self.p.append(v)
				
			def depiler(self) :
				return self.p.pop()
		```
		
!!! warning "Un code simple et efficace ?"

	Certes le codage effectué est simple, et ne présente aucune difficulté. Cependant certains mécanismes du type  `list` en python sont cachés, comme par exemple l'**allocation dynamique de mémoire**. Cette allocation se fait à la création, puis quand la lite dépasse certaines valeurs (définies spécifiquement dans la doc : 0, 4, 8, 16, 25, 35, 46, 58, 72, 88... [voir ici](https://www.it-swarm-fr.com/fr/python/taille-de-la-liste-en-memoire/940441450/)), la réservation mémoire pour la liste est augmentée puis la liste originelle est copiée dans le nouvel emplacement. Cela génère bien entendu une complexité en temps comme en mémoire inutile dans la plupart des cas.

### A partir d'une liste chaînée

Une des possibilités les plus simple pour implémenter une pile est d'utiliser les liste chaînée. En effet, dans une liste chaînée nous pouvons insérer et supprimer facilement la tête de la liste, ce qui correspondra au sommet de la pile, et nous n'aurons plus le problème d'agrandissement généré par le type `list` de python.

!!! question "Implémentation par les listes chainées"

	=== "Enoncé"

		Compléter le code suivant afin qu'il corresponde à l'interface définie pour les piles :
		
		``` python
		
		class Chainon(valeur, suivant) :
			self.valeur = valeur
			self.suivant = suivant
			
		class Pile :
			"""interface de pile"""
			def __init__(self) :
				...
				
			def est_vide(self) :
				...
				
			def empiler(self, v) :
				...
				
			def depiler(self) :
				...
		```
	=== "Une solution"
	
		A venir !
	

	

## Implémentations d'une File

### Implémentation par une liste chaînée mutable

!!! question "Implémentation par liste chaînée mutable"
	
	Bien que nous ayons vu qu'utiliser des listes mutables puisse être parfois une [mauvaise idée](www.zonensi.fr/NSI/Terminale/C03/ListeChaineeConcatener3.png), il est cependant possible de les utiliser, du moins dans une version adaptée, afin de construire un objet correspondant à l'interface définie pour les files. 
	
	Pour cela il faudra utiliser deux attributs `tete` et `queue`, qui représenteront respectivement le chainon de début et le chainon de fin de la file.
	
	=== "Enoncé"

		Compléter le code suivant pour qu'il respecte l'interface définie pour une file :
	
		``` python
		
		class Chainon(valeur, suivant) :
			self.valeur = valeur
			self.suivant = suivant
			
		class File :
			"""interface de file"""
			def __init__(self) :
				self.tete = None				
				self.queue = None
				
			def est_vide(self) :
				...
				
			def enfiler(self, v) :
				...
				
			def defiler(self) :
				...
		```
		
	=== "Solution"
		A venir !
		
### Implémentation par deux piles

!!! 


	
	

## Exercices