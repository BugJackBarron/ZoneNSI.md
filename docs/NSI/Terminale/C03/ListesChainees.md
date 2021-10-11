# Listes Chaînées

## Le problème de la structure tableau

La structure de type **tableau** permet de stocker des séquences d'éléments, mais n'est pas forcément adaptée 
à toutes les opérations  possibles sur ces séquences.

Par exemple, la structure de tableau de Python permet grâce aux méthodes `append` et `pop` d'ajouter et de supprimer
 relativement efficacement un élément en **dernière position** dans un tableau déjà existant (ce n'est pas le cas dans d'autres
 langages, *où de telles méthodes n'existent pas forcément*). 
 
Cependant, lorsqu'on veut inséerer un élément à une autre position, la méthode `insert` qui insère un élément à une position donnée
cache un certain nombre de problème, dont le coût en temps.

!!! example "Que fait `insert` lorsqu'on veut ajouter un élément en position 0"
	
	Imaginons que nous avons un tableau `tab`

## Les listes chaînées