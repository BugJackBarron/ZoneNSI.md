# Piles et files

## Définitions et exemples

### Piles

!!! abstract "Définition"

	Une {==**pile**==} (*stack* en anglais) est une structure de donnée permettant de stocker un ensemble d'objets tout en respectant certaines règles d'insertion et de délétion :
	
	* un objet est ajouté toujours en haut de la pile (**empiler**);
	* quand on supprime un objet, il s'agit toujours du **dernier objet ajouté** (**dépiler**).
	
	On associe à cette struture l'image d'une *pile d'assiettes* :
	
	<p align="center">
	![pile 1](piles1.png){: style="width : 50%;"}
	</p>
	
	Un tel type de structure est souvent appelé :
	
	* *Dernier entré, premier sorti* (*DEPS*) en français ;
	* *Last in, first out* (*LIFO*) en anglais.
	
!!! abstract "Interface"
	Pour définir l'interface d'un objet de type pile, nous supposeorns d'abord que les éléments de la pile sont tous du même type (la pile est **homogène**).
	
	Pour parler d'une pile d'éléments de type `T`, on utilisera la notation `Pile[T]`.
	
	L'interface sera simple puisque seulement 4 fonctions sont nécessaires : création d'une pile vide, empiler, dépiler, et tester la *vacuité* d'une pile.
	
	| fonction|  description|
	|:---:| :--- |
	| `creer_pile() -> Pile[T]` | crée une pile vide |
	| `est_vide(p : pile[T])` | renvoie `True si l'objet `p` de`type `Pile[T]` est vide, `False` sinon. |
	| `empiler(e : T, p : Pile[T])` | ajoute l'élément `e` de type `T` au sommet de la pile `p`. |
	| `depiler(p : Pile[T]) -> e : T` | retire et renvoie l'élément `e` de type `T` situé au sommet de la pile `p`. |
	
!!! example "Exemples d'utilisations de Piles"

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
	
		De la même manière que pour le bouton retour d'une page web, les modifications apportées dans un traitement de texte sont stockées dans une pile. L'appuis sur ++ctrl++ + Z a pour effet de dépiler, 
		et donc de rétablir le texte à la situation précédente sauvegardée dans la pile.
		
### Files

!!! abstract "Définition"
	
	Une {==**file**==} (*queue* en anglais) est une structure de donnée permettant de stocker un ensemble d'objets tout en respectant certaines règles d'insertion et de délétion :
	
	* un objet est ajouté toujours au début de la file (**emfiler**);
	* quand on supprime un objet, il s'agit toujours du **dernier objet de la file** (**défiler**).
	
	On associe à cette struture l'image d'une *file de personnes faisant la queue* :	

	<p align="center">
	![file 1](files1.png){: style="width : 70%;"}
	</p>
	
	Un tel type de structure est souvent appelé :
	
	* *Premier entré, premier sorti* (*PEPS*) en français ;
	* *First in, first out* (*FIFO*) en anglais.
	

	


## Implémentation d'une Pile

## Implémentation d'une File

## Exercices