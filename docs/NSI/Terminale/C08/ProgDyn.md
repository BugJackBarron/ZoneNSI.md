# Principes de la programmation dynamique

## Un premier exemple débranché

!!! question "Parcours sur une grille"

	=== "Énoncé"
	
		1. Combien y-a-t'il de chemin menant du point $D$ au point $A$ sur le graphique suivant, en ne se déplaçant à chaque pas que vers la droite ou vers le bas ?
		
			![ProgDyna.png](ProgDyna.png){: style="width:40%; margin:auto;display:block;background-color: #d2dce0;"}
		
		2. Combien y-a-t'il de chemin menant du point $D$ au point $A$ sur le graphique suivant, en ne se déplaçant à chaque pas que vers la droite ou vers le bas ?
		
			![ProgDyna2.png](ProgDyna2.png){: style="width:40%; margin:auto;display:block;background-color: #d2dce0;"}

	
	=== "Solution"
	
		A venir !
		
## La suite de Fibonacci

La {==**suite de [Fibonacci](https://fr.wikipedia.org/wiki/Suite_de_Fibonacci){: target="_blank"}**==} est une suite définie par une récurrence d'ordre 2 de la manière suivante, :

$$
\left\lbrace\begin{array}{rcl}
F_0 &=& 0\\
F_1 &=& 1 \\
F_{n+2} &=& F_{n+1} + F_{n} ~~ \forall n \in \mathbb{N}
\end{array}\right.
$$

!!! question "Calculer"

	=== "Énoncé"
	
		Calculer les 10 premiers termes de la suite de Fibonacci.
		
	=== "Solution"
	
		Les 10 premiers termes sont : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

!!! info "Notation"
	On notera $F(n)$ le nombre de la suite de Fibonacci de rang $n$.
	Par exemple $F(0) = 0$ et $F(6) = 13$.
	
	
Algorithmiquement parlant, la suite de Fibonacci étant une suite définie par récurrence, nous serions tentés de créer une fonction récursive pour calculer les termes $F(n)$ de la suite. Pour ce faire, nous pourrions utiliser la fonction suivante :

```` python linenums="1"
def fibo(n : int) -> int :
	if n == 0 :
		return 	0
	elif n == 1 :
		return 1
	else :
		return fibo(n-1) + fibo(n-2)
````

La question que nous devons nous poser est : est-ce un choix judicieux ? 

!!! question "Tester et voir les limites"

	=== "Énoncé"
		1. Tester la fonction `fibo` avec le code suivant :
		```` python
		import time
		for n in range(40) :
			start = time.perf_counter()
			print(f"fibo({n}) = {fibo(n)}", end="")
			end = time.perf_counter()
			print(f" Temps : {end - start}")
		````
		Que constate-t'on ?
		
		2. Réaliser un schéma de la pile d'appels récursif effectués lors de l'exécution de `fibo(6)`.
	
	=== "Solutions"
		
		
		1. Le temps d'exécution croît de manière exponentielle.
		2. On a la construction suivante :
		
			<div class="container">
			<div id="slider" class="slider">
			<div class="slider-item active"><img src="../Fibo20.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo19.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo18.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo17.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo15.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo14.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo13.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo12.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo11.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo10.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo9.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo8.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo7.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo6.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo5.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo4.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo3.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo2.png" alt="" class="img-fluid"></div>
			<div class="slider-item"><img src="../Fibo1.png" alt="" class="img-fluid"></div>
			
			<ul id="dots" class="list-inline dots"></ul>
			</div>

			</div>
		
			
!!! bug "Multiples appels"

	Dans l'exemple précédent de calcul de `fibo(6)`, on peut constater que les appels récursifs sont nombreux, et souvent pour calculer plusieurs fois la même chose :
	
	![NbAppelsFibo.png](NbAppelsFibo.png){: style="width:90%; margin:auto;display:block;background-color: #d2dce0;"}
	
	Ainsi :
	
	* `fibo(2)` est calculé à 5 reprises ;
	* `fibo(3)` est calculé à 3 reprises ;
	* `fibo(4)` est calculé à 2 reprises.
	
	Le nombre d'appels augmente exponentiellement en fonction de `n`. Par exemple le calcul récursif de `fibo(20)` nécessite $4~181$ appels au calcul `fibo(2)`, celui de `fibo(30)` le nécessite $514~229$ fois, celui de `fibo(40)` le nécessite $63~245~986$ fois....
	
	Si la limite de récursion (qui est de 1000 par défaut pour Python) n'est pas atteinte pour `fibo(40)`, le temps de calcul, lui, croît aussi exponentiellement...
	

## Programmation dynamique

### Premiers exemples sur la suite de Fibonacci

En considérant l'algorithme précédant, on comprend bien qu'il est particulièrement inefficace de calculer plusieurs fois le même sous-calcul. Afin d'améliorer le temps de calcul de l'algorithme, nous décidons donc de {==**mémoriser les calculs déjà effectués**==} dans un tableau. Il existe deux méthodes différentes :

!!! info "Programmation dynamique de la suite de Fibonacci"

	=== "Méthode ascendante"
	
		On va calculer les nombres de la suite de Fibonacci jusqu'à $F(n)$ en partant de $F(0)$ et $F(1)$. On appelle ce type de méthode une méthode {==**Bottom-Up**==}. Ce n'est pas une méthode récursive.
		
		```` python linenums="1"
		def fiboAsc(n : int) -> int :
			F = [0]*(n+1)
			F[1] = 1
			for i in range(2,n+1) :
				F[i] = F[i-1] + F[i-2]
			return F[n]
		
		````
		
	=== "Méthode descendante"
	
		On va calculer les nombres de Fibonacci récursivement, mais en sauvegardant les calculs déjà effectués dans une liste Python, en profitant de sa *mutabilité*. On appelle ce type de méthode une approche {==**Top-Down**==} :
		
		```` python linenums="1"
		def fiboDesc(n : int) -> int :
		
			memo = [0, 1]+[None]*(n-1)
			
			def compute(n, memo) :
				if memo[n] is None :
					memo[n] = compute(n-1, memo) + compute(n-2, memo)
				return memo[n]
				
			return compute(n, memo)
		
		````
		
		L'explication la plus simple du fonctionnement est visible dans Thonny, en utilisant le debugger, ou bien [ici](https://pythontutor.com/visualize.html#code=def%20fiboDesc%28n%29%20%3A%0A%0A%20%20%20%20memo%20%3D%20%5B0,%201%5D%2B%5BNone%5D*%28n-1%29%0A%20%20%20%20%0A%20%20%20%20def%20compute%28n,%20memo%29%20%3A%0A%20%20%20%20%20%20%20%20if%20memo%5Bn%5D%20is%20%20None%20%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20memo%5Bn%5D%20%3D%20compute%28n-1,%20memo%29%20%2B%20compute%28n-2,%20memo%29%0A%20%20%20%20%20%20%20%20return%20memo%5Bn%5D%0A%20%20%20%20return%20compute%28n,%20memo%29%0A%20%20%20%20%20%20%20%20%20%20%20%20%0AfiboDesc%286%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false){: target="_blank"}, pour un exemple sur `fiboDesc(6)`.
	
	=== "Quelques considérations hors programme"

		On peut se demander pourquoi utiliser une fonction auxiliaire `compute` dans l'approche descendante, et pourquoi ne pas utiliser une fonction récursive utilisant un dictionnaire vide comme paramètre par défaut telle que la suivante :

		``` python
		def bad_fibo(n, memo = dict()) :
    		if n in memo :
        		return memo[n]
    		elif n <= 1 :
        		memo[n] = 1
        		return memo[n]
    		else :
        		memo[n] = bad_fibo(n-1, memo)+bad_fibo(n-2, memo)
        		return memo[n]
				
		``` 
		En testant la fonction ci-dessus, on obtient bien le résultat escompté, et dans un temps raisonnable. 

		{==**Oui, mais c'est une mauvaise pratique !**==}.

		Utilisons l'éditeur ci-dessous :

		{{ IDEv('badFibo') }}
		
		* Lors de l'appel de la fonction `bad_fibo` en ligne 16, on constate que la récursivité s'enclenche **et la mémoisation**, puisque la fonction n'est en réalité qu'appelée 5 fois.
		* Lors de l'appel suivant de la fonction `bad_fibo` en ligne 18, la récursivité s'enclenche, mais les messages nous indiquent que la mémoïsation a déjà été effectuée pour les valeurs `5` et `4`. {==**Ce n'est pas le comportement normalement attendu !**==}


		La raison : l'utilisation d'un paramètre par défaut mutable. En observant l'affichage de l'`id`, on constate que dans les deux appels de la ligne 16 et de la ligne 18, cet identifiant est le même. cela signifie que l'objet associé au paramètre `memo` {==**n'est pas local à la fonction `bad_fibo`.**==}. En effet, quand l'interpréteur passe pour la première fois sur la ligne de définition `def bad_fibo(n, memo = dict()) :`, il crée en mémoire un objet de type `dict`, mais qui n'est pas explicitement nommé. Cet objet restera référencé dans la mémoire sans être ramassé par le *garbage collector*, le temps de l'exécution du programme.

		*Oui mais c'est pratique, me direz-vous !*

		{==**C'est surtout risqué**==} : certes des valeurs sont mémorisées pour une utilisation future, mais nous n'avons aucun contrôle réel sur l'objet en mémoire. On appelle ceci une **fuite mémoire** ({==**memory leak**==}), qui peut être un problème sérieux pour des programmes devant tourner sur de longues périodes (comme un serveur web par exemple). Avec une telle pratique, il est possible de se retrouver avec des objets non utilisés mais occupant une place importante dans la mémoire vive.
		
		Dans tous les cas, *explicit is better than implicit*, donc si vous souhaitez conserver ces valeurs dans la mémoire vive de l'ordinateur, il faut explicitement les nommer, et les supprimer effectivement lorsque ces variables deviennent inutiles (en `C` c'est impératif).
		
### Principes de la programmation dynamique

La {==**programmation dynamique**==}, introduite au début des années 1950 par [Richard Bellman](https://fr.wikipedia.org/wiki/Richard_Bellman){:target="_blank"}, est une méthode pour résoudre des problèmes en combinant des solutions de sous-problèmes, tout comme les méthodes de type *diviser pour régner*.

Un algorithme de programmation dynamique résout chaque sous-sous-problème une seule fois et mémorise sa réponse dans un tableau, évitant ainsi le re-calcul de la solution chaque fois qu'il résout chaque sous-sous-problème.

La programmation dynamique s'applique généralement aux **problèmes d'optimisation**, comme ceux que nous avons vu l'an passé lorsque nous avons étudié les algorithmes gloutons.

### Le problème du rendu de monnaie

*Largement inspiré de [https://isn-icn-ljm.pagesperso-orange.fr/NSI-TLE/res/res_rendu_de_monnaie.pdf](https://isn-icn-ljm.pagesperso-orange.fr/NSI-TLE/res/res_rendu_de_monnaie.pdf)*.


#### Le problème : introduction et traitement débranché

Vous avez à votre disposition un nombre illimité de pièces de 2 cts, 5 cts, 10 cts, 50 cts et 1 euro (100 cts). Vous devez rendre une certaine somme (rendu de monnaie). Le problème est le suivant : "Quel est le nombre minimum de pièces qui doivent être utilisées pour rendre la monnaie"

La résolution "gloutonne" de ce problème peut être la suivante :

* On prend la pièce qui a la plus grande valeur (il faut que la valeur de cette pièce soit inférieure ou égale à la somme restant à rendre).
* On recommence l’opération ci-dessus jusqu’au moment où la somme à rendre est égale à zéro.

!!! question "Questions"

	=== "Énoncé"
	
		1. Appliquer cette méthode pour une somme de 1€77 (177cts) à rendre.
		2. Appliquer cette méthode à la somme de 11 centimes.
			1. Quel est le problème ?
			2. Proposer une solution permettant de rendre 11 centimes. Est-elle unique ?

#### Mise au point d'un algorithme récursif

Nous allons essayer de mettre au point un algorithme récursif donnant une solution au problème de rendu de monnaie en utilisant le **nombre minimal de pièces**.


!!! question "Questions"

	=== "Énoncé"
		1. Compléter l'arbre suivant donnant l'ensemble des possibilités de répartition des pièces :
		
			![Monnaie1.png](Monnaie1.png){: style="width:90%; margin:auto;display:block;background-color: #d2dce0;"}
	
		2. Combien de chemins sont des impasses (on termine avec 1 cts restant) ? Combien de solutions existent ? Quelle est la solution utilisant le nombre minimal de pièces ?
		
			!!! info "Force Brute"

				Quand une méthode traite tous les cas possibles, on parle souvent de méthode en {==**force brute**==}.
		3. Compléter la fonction suivante pour qu'elle donne le nombre minimal de pièces utilisées pour une somme `s` donnée :
		
			```` python
					
			def rendu_monnaie_rec(P : list, s : int) -> int:
				""" renvoie le nombre minimal de pièces pour rendre la somme s
				en utilisant le jeu de pièces P"""
				
				if s==0:
					return 0
				else:
					mini = float('inf') # On fixe le nombre de piècé à l'infini
				for i in range(len(P)):
					if ... <= s:
						nb = 1 + ...
						if nb < mini:
							mini = nb
				return mini
			````
			
		4. Testez la fonction avec le jeu de pièces `(2, 5, 10, 100)`, et pour des sommes augmentant à partir de 11 cts. A partir de quelle v somme le programme devient-il visiblement plus lent ?


#### Passage en programmation dynamique

On constate dans la partie précédente que la méthode précédente fait de trop nombreux appels récursifs, qui ralentissent considérablement le temps de calcul, voire plante le programme dès que la taille maximale de la pile est dépassée.

On va donc utiliser la *programmation dynamique* pour accélérer la vitesse de traitement du problème :

!!! question "Questions"

	=== "Énoncé"
		
		On considère la fonction suivante :
		
		```` python 		
		def renduMonnaie1(P : list, s : int) -> int | None :
			nb = [0]+[None] * (s)
			for n in range(1, s+1) :
				for p in P :
					if p <= ... and nb[...] is not None :
						if nb[n] is ... or ... > 1 + nb[n-p]:
							nb[n] = 1 + nb[n-p]											
			return ...
		````
		1. Compléter la fonction afin qu'elle renvoie le nombre minimal de pièce pour rendre la monnaie, ou `None` s'il est impossible de rendre la monnaie.
		
		2. Est-ce une méthode ascendante ou descendante ?		
		
		3. Créer une fonction `renduMonnaie2(P : list, s : int) -> int | None` utilisant l'autre méthode.
		

??? question "Pour aller plus loin"

	=== "Énoncé"
		Nos codes précédents ne nous permettent que de connaitre le nombre minimal de pièces nécessaire pour un rendu de monnaie donné. Nous ne connaissons par contre pas quelles pièces sont nécessaires.
		
		Transformez une des fonction précédente afin qu'elle renvoie les pièces nécessaires au rendu de monnaie.
