# Gestion des exceptions

## Un exemple d'erreur à ne pas commettre


!!! abstract "Utilisation malheureuse d'un module"
	Reprenons le module `secondDegre.py` de la partie précédente, mais cette fois ci en temps qu'utilisateur·trice. Nous
	connaissons l'interface qui nous a été fournie par l'auteur·trice. Pour tester le module nous lançons le script suivant, nommé `testModule.py`, et situé dans le même dossier que `secondDegre.py` :

	``` python
		import secondDegre as sD

		p = input("Donnez les coefficients du polynome séparés par des virgules :")
		p = tuple(map(float,p.split(",")))

		p = sD.polynome(p)
		print(sD.tangente(p,3))
	```

!!! question "Un problème ?"
	Copiez-collez le code ci-dessus dans un fichier `testModule.py`, puis exécutez-le en saisissant :
	
	1. `3,4,5` ;
	2. `3,4,5,6` 
	3. `0,3,4`
	
	Dans chacun des cas, qu'obtient-on en sortie ? Pourquoi ?
	
??? done "Solution"

	=== "`3,4,5`"
		La sortie est :
		
			`y = 22.0(x-3) + 44.0`
		
		qui est correcte.
		
	=== "`3,4,5,6`"
		La sortie renvoie une erreur de type `ValueError`, qui d'après la pile d'erreur est relevée dans la fonction `polynome`, et qui est assez explicite : `ValueError: too many values to unpack (expected 3)`. On constate que le programme attend 3 valeurs en entrée, et qu'il en a reçu trop.
		
	=== "`0,3,4`"
		La sortie renvoie une erreur de type `TypeError`, causée dans la fonction `polynome`, mais qui là est plus sibylline : `TypeError: cannot unpack non-iterable NoneType object`. Nous allons devoir passer un certain temps à debugger, afin de comprendre ce qui s'est passé...

!!! tips "Lever les bonnes erreurs"
	Dans l'exemple précédent, les deux erreurs, très différentes, **sont signalées par leur type**, accompagné d'un message plus ou moins clair. L'utilisateur·trice, qui ne connait pas l'implémentation,
	  **ne peut parfois pas savoir d'où provient son erreur** (ce qui peut donner des séances de débuggage particulièrement frustrantes). Il est donc nécessaire de préciser mieux les erreurs commises par l'utilisateur·trice, pour qu'il ou elle n'ait pas à ses préoccuper des détails d'implémentation.
	
	Il est par exemple possible de {==**rajouter un message**==} lorsque l'erreur est levée, en la passant en paramètre directement dans l'instruction `ValueError()` ou `TypeError()`. On peut en outre améliorer le code en s'assurant que les éléments du tuple `t` sont bien `int` ou `float` :
	``` python
	def polynome(t) :
		if len(t)>3 :
			raise ValueError("length of tuple argument must be 3")
		a, b, c = t
		if not(isinstance(a,(int, float))
		) or not(isinstance(b,(int, float))
		) or not(isinstance(c,(int, float))) :
				raise TypeError("argument Error : argument must be a tuple integers or float")
		if a == 0 :
			raise ValueError("First element of tuple must not be 0")
		return t
	```
	
## Tyes d'exceptions

Voici quelques exceptions courantes ainsi que leurs utilisations
	
| Exception | Contexte |
| :---: | :--- |
|`NameError` | accès à une variable inexistante dans l'espace de nom courant |
|`IndexError` | accès à un indice invalide d'une liste, d'un tuple, d'une chaine de caractères... |
|`KeyError` | accès à une clé inexistante d'un dictionnaire |
| `ZeroDivisionError` | division par zéro |
| `TypeError` | opération appliquée à un ou des objets incompatibles |

!!! tips "Lever des exceptions"
	Une exception peut être {==**levée**==} (c'est-à-dire volontairement déclenchée) par l'intermédiaire de l'instruction `raise`.

	Dans ce cas **le programme est interrompu**, et *la pile d'erreurs* est renvoyées dans le terminal à l'utilisateur.
	
!!! question "Corriger le code"""
	
	Malgré nos corrections, il reste plusieurs possibilités d'erreurs dans l'utilisation de la fonction `polynome(t)`.
	
	Quelles sont-elles et comment les corriger pour lever une exception explicite ?
	
??? done "Solution"

	=== "Exécution de `polynome((2,3))` ou `polynome((4))`"
		Que se passe-t-il lorsqu'on utilise la fonction `polynome` avec un tuple de 1 ou 2 éléments ?
		
		Dans le cas d'un seul élément, l'erreur ressortie est :
		
		```` python
		a, b, c = t
		TypeError: cannot unpack non-iterable int object
		````
			 
		Dans le cas de deux éléments, l'erreur levée est  :

		```` python	
		a,b,c = t
		ValueError: not enough values to unpack (expected 3, got 2)
		````
			
		Dans les deux cas, on voit apparaitre les détails d'implémentation du code de la fonction, qui sont peu clairs en particulier pour le cas n°2.
	
	=== "Exécution de `polynome(3,4,5)`"
	 
		Une erreur possible, et que vous avez probablement commise, est celle
		de passer non pas un seul argument sous la forme d'un *tuple* (ou d'une liste) mais de multiples paramètres.
		 
		Cette erreur déclenche alors l'exception `TypeError` car les trois arguments passés ne sont pas du bon type.

	=== "Une correction possible"
	
		Le code suivant  est une solution possible (certainement perfectible) à la levée d'erreurs plus explicites :

		```python
		
		def polynome(*t) :
			try :
				if len(t) == 1 :# si on passe un tuple ou un tableau (1,2,3),
					# *t le convertit en [(1,2,3)]
					t = t[0] # d'où cette ligne
				a, b, *c  = t #Puis on unpack, c étant un tuple éventuellement vide
			except TypeError :
				raise TypeError("Must pass three argument or a tuple of 3 element.")
			if len(c) !=1 : # si c est vide ou contient au moins 2 éléments
				raise ValueError("Bad Number of argument.")
			if not(isinstance(a,(int, float))
			) or not(isinstance(b,(int, float))
			) or not(isinstance(*c,(int, float))) :
					raise TypeError("argument Error : argument must be a tuple of integers or floats.")
			if a == 0 :
				raise ValueError("First element of tuple must not be 0.")
			return t
		```

## Intercepter des exceptions

Vous avez constaté dans la solution précédente un bloc que nous n'avons encore jamais utilisé :

``` python
try :
	if len(t) == 1 :	
		t = t[0]
	a, b, *c  = t
except TypeError :
	raise TypeError("Must pass three argument or a tuple of 3 element.")
```
On a ici l'utilisation d'une structure spéciale : {==**l'interception d'erreurs**==}.


!!! tips "Interception des exceptions"

	Il arrive souvent en programmation que l'on doive utiliser une instructions ou une série d'instruction dont on sait à l'avance qu'elle peuvent générer des erreurs. La structure suivante est là pour ça :
	``` python

	try :
		# Bloc try
	except error :
		# Bloc except

	```
	Le code du bloc `try` va être exécuté, et si une erreur du type fournie en argument de l'instruction `except` est levée, alors le code du bloc `except` est exécuté.

!!! example "Exemple :"

	En première nous avons vu l'importance de rendre parfois un code **dumbproof**, et que cela générais parfois de nombreuses difficultés. Le simple fait de coder une fonction demandant à un utilisateur de saisir un nombre entier entre 1 et 10 inclus pouvait rapidement pénible à écrire. Les deux onglets ci-dessous donnent deux versions d'une fonction permettant de réaliser cette fonction, la version utilisée en première, et celle levant des exceptions.
	
	=== "Version avec des structures conditionnelles"
		
		``` python
		
		def askIntFrom1To10() :
			while True :
				nb = input("Entrez un entier entre 1 et 10 :")
				if nb.isnumeric() and "." not in (nb) :
					nb = int(nb)
					if 1<=nb and nb<=10 :
						return nb
					else :
						print("L'entier saisi n'est pas entre 1 et 10. Veuillez recommencer")
				else :
					print("Ce n'est pas un entier, veuillez recommencer !")
		```
		
	=== "Version avec interception d'erreurs"
	
		``` python
		
		def askIntFrom1To10() :
			while True :
				try :
					nb = int(input("Entrez un entier entre 1 et 10 :"))
					if 1<=nb and nb<=10 :
						return nb
					else :
						print("L'entier saisi n'est pas entre 1 et 10. Veuillez recommencer")
				except ValueError :
					print("Ce n'est pas un entier, veuillez recommencer !")
		```

!!! question "Exercice"
	Evidemment, la différence ne saute pas vraiment aux yeux... Pourquoi faire tout un plat d'une seule ligne gagnée ?
	
	Essayez donc, pour chacune des 2 fonctions précédentes, avec les chaines de caractères suivantes (à copier-coller) :
	
	* `½`
	* `3²`
	
??? done "Réponse"
	
	En fait le problème provient de la *méthode* `isnumeric()`, dont on ne contrôle pas vraiment le fonctionnement. On sait que cette méthode permet de vérifier si une chaine de caractères est bien constituée uniquement de caractères numériques. Mais sans lire réellement la documentation, qui peut se douter que les **fractions définies dans la table utf8**, ainsi que les caractères en **exposant et en indice**, sont considérés comme des valeurs numériques.
	
	L'intérêt du bloc `try` est qu'il se déclenchera dès qu'il y aura une exception levée. Et cette exception a peu de chance de se produire dans le bloc `if / else `. La fonction devient **dumbproof** (mais si vous réussissez à déclencher une erreur bloquante, signalez-le moi !!).

	Plus prosaïquement, une erreur levée et correctement traitée avec une structure `try/except` permet au programme de ne pas s'arrêter lors d'un cas particulier.
			

!!! info "Enchainer les interceptions"	
	Il est aussi possible d'avoir plusieurs blocs `except` successifs, en utilisant :
	``` python

		try :
			# Bloc try
		except error1 :
			# Bloc except1
		except error2 :
			# Bloc except2
		...
	```
	
!!! info "Etendre la gestion des exceptions"

	Il existe de nombreuses autres possibilités utilisant la levée d'exceptions, mais elles dépassent largement le programme de Terminale.
	
	Les plus curieux parmi vous pourront toujours aller lire la [doc Python](https://docs.python.org/3/tutorial/errors.html)", qui reste la référence absolue...

## Les assertions

Une autre méthode pour interrompre explicitement un programme est d'utiliser des **assertions** créées avec l'instruction `assert`, sous la forme suivante :

``` python
assert expression booléenne, chaine de caractère avec message d'erreur
```

Cette instruction lèvera alors une `AssertionError`, avec le message passé entre parenthèse. Mais attention, le programme sera alors interrompu !

Les assertions sont souvent utilisées pour s'assurer que les {==**préconditions**==} d'une fonction sont bien remplies, c'est-à-dire que les arguments fournis correspondent bien aux exigences du programme.

!!! exemple 
	Dans le cadre d'une application graphique, on veut pouvoir déplacer un point $M(x;y)$ avec un vecteur $\vec{u} (a,b)$ avec $x,y,a,b$ entiers.
	On veut créer une fonction `translation(p : tuple,v :tuple) -> tuple` qui prend en argument deux tuples de dimension 2, et qui renvoie le tuple obtenu en additionnant les éléments de même indice. Cependant, pour que la fonction soit utilisable, il faut impérativement que l'utilisateur ait bien fourni deux tuples de dimension 2 et d'entiers.

	``` python
	def translation(t : tuple , v : tuple) -> tuple :
		assert type(t) == tuple and len(t) == 2, "bad t argument, is not a tuple of length 2"
		assert type(v) == tuple and len(v) == 2, "bad v argument, is not a tuple of length 2"
		assert type(t[0]) == int and type(t[1]) == int, "tuple t must only contains integers"
		assert type(v[0]) == int and type(v[1]) == int, "tuple v must only contains integers"
		return (t[0]+v[0], t[1]+v[1])
	```
