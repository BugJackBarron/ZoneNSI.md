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
	
	
### Files

!!! abstract "Définition"

	<p align="center">
	![file 1](files1.png){: style="width : 70%;"}
	</p>



## Implémentation d'une Pile

## Implémentation d'une File

## Exercices