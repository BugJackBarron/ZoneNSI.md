# Arbres Binaires de Recherche (ABR)

## Premier Exemple

{==D'après *Numérique et Sciences Informatiques, 24 leçons avec exercices corrigés*, Balabonski, Conchon, Filliâtre, Nguyen, Editions Ellipses==}

Imaginez une bibliothèque contenant un très très grand nombre de livres. Cette bibliothèque est organisée de la manière suivante :

* Il y a 17 576 pièces différentes.
* Chaque pièce est repérée par une suite de trois lettres, et dans cette pièce sont rangés tous les livres dont les titres commencent par ces trois lettres.
* Chaque pièce possède deux sorties, une à droite et une à gauche.
* La sortie de gauche mène **toujours** soit à une salle dont les trois lettres sont situées avant dans l'ordre alphabétique, soit nulle part.
* La sortie de droite mène **toujours** soit à une salle dont les trois lettres sont situées après dans l'ordre alphabétique, soit nulle part.

Une représentation de cette bibliothèque peut être donnée sous la forme d'un rabre binaire tel que le suivant :

![P2_ABR_1.png](P2_ABR_1.png){: style="width:50%; margin:auto;display:block;background-color: #546d78;"}


!!! question 
	=== "Enoncé"
		1. Dans cet arbre, préciser où sont situés les livres dont le titre commence par :
			1. `KNU`
			2. `UDP`
			3. `JET`
		2. Pourquoi y-a-t-il 17 576 pièces différentes ?
	
	=== "Réponses"	
		A venir !
		
Cette répartion, *pour peu qu'elle soit correctement faite* (c'est-à-dire que le choix des lettres soit pertinent), peut être incroyablement efficace. Dans **le meilleur des cas**, il ne faudra traverser qu'au maximum 15 salles pour trouver n'importe quel livre. 

Cette structure sera particulièrement utile pour effectuer des recherches : on l'appelle ainsi un {==**arbre binaire de recherche**==} (ou **BST**, *Binary Search Tree* en anglais).

!!! warning "Une mauvaise répartition"
	L'importance de l'organisation des salles est ici primordial, toutes les solutions ne se valant pas. Ci-dessous une répartition qui est dans le pire des cas : les sous-arbres gauche sont toujours vide.
	
	![P2_ABR_2.png](P2_ABR_2.png){: style="width:50%; margin:auto;display:block;background-color: #546d78;"}
	
	Dans cette situation, il faudra traverser les 17 576 pièces pour atteindre les livres dont le titre commence par `ZZZ`.
	
## Arbres Binaires de recherches et algorithmes

### Définition

!!! abstract "Arbre Binaire de Recherche (ABR)"

	Un {==**ABR**==} ou {==**Arbre Binaire de Recerche**==} est un arbre binaire vérifiant les propriétés suivantes :
	
	* les noeuds contiennent des valeurs appelées {==**clés**==} pouvant être comparées entre elles (nombres, chaînes de caractères, ...) ;
	* toutes les clés situées dans le **sous-arbre gauche** (resp. droit) d'un noeud sont **inférieures** (resp. supérieures) à la clé du noeud.
	
	
!!! example "Exemples"
	
	=== "Exemple 1"
	
		![P2_ABR_3.png](P2_ABR3.png){: style="width:30%; margin:auto;display:block;background-color: #546d78;"}
	
	=== "Exemple 2"
	
		![P2_ABR_4.png](P2_ABR4.png){: style="width:30%; margin:auto;display:block;background-color: #546d78;"}
		
	=== "Contre-exemple 1"
	
		![P2_ABR_5.png](P2_ABR5.png){: style="width:30%; margin:auto;display:block;background-color: #546d78;"}
		
	=== "Contre-exemple 2"
		
		![P2_ABR_6.png](P2_ABR6.png){: style="width:30%; margin:auto;display:block;background-color: #546d78;"}


### Recherche dans un ABR

### Ajout dans un ABR

### Suppression dans un ABR

## Arbre Binaires Equilibrés

### Pourquoi équilibrer

### Un exemple d'arbre binaires de recherches équilibrés : les AVL

#### Les AVL


#### Rotations droites et gauches


#### Application en Python
