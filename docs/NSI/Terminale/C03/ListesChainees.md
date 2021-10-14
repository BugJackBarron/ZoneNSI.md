# Listes Chaînées

## Le problème de la structure tableau

La structure de type **tableau** permet de stocker des séquences d'éléments dans des zones contigües de la mémoire, mais n'est pas forcément adaptée 
à toutes les opérations  possibles sur ces séquences.

Par exemple, la structure de tableau de Python permet grâce aux méthodes `append` et `pop` d'ajouter et de supprimer
 relativement efficacement un élément en **dernière position** dans un tableau déjà existant (ce n'est pas le cas dans d'autres
 langages, *où de telles méthodes n'existent pas forcément*). 
 
Lorsqu'on veut insérer un élément à une autre position on peut, toujours en Python, utiliser a méthode `insert` qui insère un élément à une position donnée. Mais cette méthode
*cache un certain nombre de problèmes*, dont le **coût en temps**.

!!! example "Que fait `insert` lorsqu'on veut ajouter un élément en position 0"
	
	Imaginons que nous avons un tableau `tab`, pour lequel nous voulons insérer la valeur $8$ en première position :
	
	<p align="center">
	![Manim gif](addFirstElement_ManimCE_v0.11.0.gif){: style="width:50%;"}
	</p>
	
	Au total, nous avons réalisé un nombre d'opérations qui est **proportionnel à la taille du tableau !**Sur un petit, tel que celui-ci, il n'y a pas trop de problèmes, 
	mais sur un tableau contenant *plusieurs millions* d'entrées, le nombre d'opérations devient bien trop important.
	
	Heureusement, il existe d'autres ménières de stocker des informations, qui permettent une modification bien plus rapide des différents éléments.	
	

## Les listes chaînées

### Construction d'une liste chaînées

!!! abstract "Liste chaînée"
	Une {==**liste chaînée**==} est une structure permettant d'implémenter une liste, c'est-à-dire une séquence finie de valeurs (de même type ou non). Les éléments dont dits **chaînés**
	car chque élément possède l'adresse mémoire de l'élément suivant de la liste.
	
!!! example "Exemple"
	
	<p align="center">
	![LC1](ListeChainee1.png){: style="width : 30%;"}
	</p>
	
	On a représenté ici une liste chaînée de trois éléments :
	
	* Le premier est $21$, et il pointe vers l'adresse mémoire du second ;
	* Le deuxième élément est $15$ et il pointe vers l'adresse mémoire du troisième ;
	* Le troisième élément est $45$. Il ne pointe vers rien (l'adresse du suivant est `None`). On a atteint la fin de la liste.
	
!!! tips "Implémentation d'une liste chaînée en Python"

	La méthode classique pour implémenter une liste chaînée est de construire une **classe d'objets** possédant deux attributs : un pour la **valeur** et un pour l'adresse du chainon suivant :
	
	``` python linenums="1"
	
	class Chainon :
		"""Chainon d'une liste chainée"""
		def __init__(self, valeur, suivant) :
			self.valeur = valeur
			self.suivant = suivant
	```
	
	
	Une fois cette classe définie, la construction de la liste s'effectue de la manière suivante :
	
	``` python
	chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
	```
	
	
	Ici, on a créé une liste nommée `chaine` à partir de trois objets de classe `Chainon` qu'on peut visualiser ainsi :
	
	<p align="center">
	![LC2](ListeChainee2.png){: style="width : 70%;"}
	</p>

!!! info "Remarque"

	Cette construction est une construction récursive basée sur des objets. Il aurait été possioble d'utiliser des tuples ou des listes python, mais l'utilisation serait moins pratique :
	``` python
	(21,(15, (45, (None))))
	```
	
### Opérations sur les listes chaînées.

!!! exemple "Longueur d'une liste chaînée"

	Nous allons créer maintenant une fonction `longueur` qui calcule la longueur d'une liste chaînée telle que nous l'avons implémentée.
	
	Cette fonction devra :
	
	* renvoyer 0 si la liste est vide ;
	* renvoyer le nombre d'éléments de la chaîne sinon.
	
	
	Le plus simple est d'utiliser la récursivité :
	
	``` python
	def longueur(chaine) :
		if chaine == None :
			return 0
		else :
			return 1 + longueur(chaine.suivant)
	```
	
	La **complexité** de cette fonction est directement proportionnelle à la longueur de la liste : pour une liste de $1~000$ éléments,
	la fonction effectuera :
	
	* $1~000$ comparaisons ;
	* $1~000$ additions ;
	* $1~000$ appels récursifs.
	
	On en conclut que la complexité en temps de cette fonction est en $\mathbb{O}(n)$.
	
	??? question "Et en itératif ?"
	
		``` python
		def longueur(chaine) :
			n = 0
			chainon = chaine
			while chainon is not None :
				n+=1
				chainon = chainon.suivant
			return n
		```
!!! question "Exercice : n-ième élément"

	=== "Enoncé" 
		
		Créer une fonction `niemeElement(chaine, i)` qui renvoie la valeur du i-ième élément de la liste chaînée passée en argument.
		
	=== "Solution récursive"
	
		``` python
		def niemeElement(chaine, i) :
			if chaine == None :
				raise IndexError("Invalid index")
			if i == 0 :
				return chaine.valeur
			else :
				return niemeElement(chaine.suivant, i-1)
		```
		
		La question de la complexité est un peu plus subtile :
		
		* dans un cas correct (l'indice `i` fourni corresond bien à un élément de la liste), le nombre d'opérations est bien proportionnel à `i` ;
		* dans le cas où `i` est supérieur à la longueur de la liste, par contre, on va parcourir la totalité de la liste avant de pouvoir signaler une erreur.
		Ce serait cependant une très mauvaise idée de calculer la longueur de la liste pour le comparer à $i$, car le calcul de la longueur parcoure déjà toutes la liste.
		Faire ce calcul en appel récursif générerait donc une complexité **quadratique**. On pourrait cependant encapsuler la fonction récursive dans une fonction dont l'objectif serait
		de vérifier la valeur de l'indice avant d'effectuer les appels récursifs.
		* Pire, dans le cas où l'indice passé est négatif, la liste chaînée sera elle aussi parcourue intégralement avant de renvoyer une erreur d'indice.On peut cependant corriger celà par la ligne :
		
		``` python
		if chaine == None or i<0 
		:
		```
		
		
	=== "Solution Itérative"
	
		``` python
		def niemeElementI(chaine, i) :
			if i<0 :
				raise IndexError("Invalid index")
			ni = 0
			chainon = chaine
			while  chainon != None and ni != i :
				ni += 1
				chainon = chainon.suivant
			if chainon != None :
				return chainon.valeur
			else :
				raise IndexError("Invalid index")
		```
		 On retrouve en terme de complexité les mêmes éléments que pour la fonction récursive. Cependant les erreurs 
		 ainsi que les conditions de sorties sont plus complexes à prendre en compte.
		
		
!!! question "Exercice :  Concaténation de deux listes"

	=== "Enoncé" 
		
		Créer une fonction `concatener(c1, c2)` qui renvoie la liste chaînée obtenue par concaténation de `c1` et `c2`.
		
	=== "Solution récursive"
	
		``` python
		def concatener(c1, c2) :
			if c1 == None :
				return c2
			else :
				return Chainon(c1.valeur,concatener(c1.suivant, c2))
		```
		
		La complexité dépend fortement de la longueur de la liste `c1`. par contre elle ne dépend pas de celle de `c2`.
		Dans cette version, les chaines `c1` et `c2` ne sont pas modifiée ! `concatener` renvoie 
		une nouvelle liste chaînée qui a copié les valeurs de `c1` avant de les lier à celles de `c2`.
		
		<p align="center">
		![LC1](ListeChaineeConcatener1.png){: style="width : 60%;"}
		</p>
		
	=== "Solution Itérative"
		
		``` python 
		def concatenerI(c1, c2) :
			chainon = c1
			while chainon.suivant != None :
				chainon = chainon.suivant
			chainon.suivant = c2
			return c1
			
		```
		Attention ! Dans cette solution, `c1` est modifiée ! 
		<p align="center">
		![LC2](ListeChaineeConcatener2.png){: style="width : 60%;"}
		</p>
		
		
		
??? bug "Un cas limite : renverser la liste"
	
	Comment faire pour renverser une liste chaînée ? Sachant que nous avons vu des procédés récursif pour les questions précédentes,
	nous sommes tenter d'en utiliser un aussi pour ce cas, par exemple en sélectionnant le premier chaînon et en le concaténant
	à la liste renversée de la suite de la chaîne, Le cas de base étant celui d'une liste vide, auquel cas on renvoie cette liste :
	
	``` python
	def renverser(chaine) :
		if chaine == None :
			return None
		else :
			concatener(renverser(chaine.suivant), Chainon(chaine.valeur, None))
	```
	
	Cependant cette solution n'est pas efficace !
	
	
		
### Modification de listes chaînées
		
!!! question "Exercice :  Insertion d'un chainon"

	=== "Enoncé" 
		
		Créer une fonction `inserer(v, n, chaine)` qui insère l'élément `v` à la position `n` dans la liste passée en argument.
		
	=== "Solution"
	
		A venir !
	
!!! question "Exercice :  Suppression d'un chainon"

	=== "Enoncé" 
		
		Créer une fonction `supprime(n, chaine)` qui supprime l'élément à la position `n` dans la liste passée en argument.
		
	=== "Solution"
	
		A venir !
		