# Gestion des exceptions

## Un exemple d'erreur à ne pas commettre


!!! abstract "Utilisation malheureuse d'un module"
	Reprenons le module `secondDegre.py`, mais en temps qu'utilisateur. Nous
	connaissons l'interface qui nous a été fournie par l'auteur. Pour tester le module
	nous lançons le script suivant, nommé `testModule.py`, et situé dans le même dossier que `secondDegre.py` :
	``` python
		import secondDegre as sD

		p = input("Donnez les coefficients du polynome séparés par des virgules :")
		p = tuple(map(float, p.split(",")))

		p = sD.polynome(p)
		print(sD.tangente(p,3))
	```
!!! question "Un problème ?"
	Copiez-collez le code ci-dessus dans un fichier `testModule.py`, puis exécutez-le en saisissant :
	
	1. `3,4,5` ;
	2. `"trois",4,5`
	3. `3,4,5,6` 
	4. `0,3,4`
	
	Dans chacun des cas, qu'obtient-on en sortie ? Pourquoi ?
	
??? done "Solution"
	=== "`3,4,5`"
		La sortie est :
		
			`y = 22.0(x-3) + 44.0`
		
		qui est correcte.
		
	=== "`"trois",4,5`"
		La sortie renvoie une erreur de type `ValueError`, mais c'est celle levée dans le premier `if`, car un élément du tuple n'est pas du bon type.
		
	=== "`3,4,5,6`"
		La sortie renvoie une erreur de type `ValueError`, mais c'est celle levée dans le premier `if`, car le tuple donné n'est pas de la bonne taille.
		
	=== "`0,3,4`"
		La sortie renvoie une erreur de type `ValueError`, mais c'est celle levée dans le deuxième `if`, car le tuple donné ne correspond pas à un polynôme de degré 2.
		
!!! tips "Lever les bonnes erreurs"
	Dans l'exemple précédent, les trois erreurs, pourtant très différentes, donnent la même erreur. L'utilisateur, qui lui ne connait pas l'implémentation, **ne peut donc pas savoir d'où provient son erreur** (ce qui peut donner des séances de debuggage particulièrement frustrantes). Il est donc nécessaire de préciser mieux les erreurs commises par l'utilisateur, pour qu'il n'ait pas à ses préoccuper des détails d'implémentation.
	
	Il est par exemple possible de rajouter un message lorsque l'erreur est levée, en la passant en paramètre directement dans l'instruction `ValueError()` :
	``` python
		def polynome(t) :
    			a,b,*c = t
			if len(c) >1 :
				raise valueError("length of tuple argument greater than 3")
			if not(isinstance(a,(int, float))
			) or not(isinstance(b,(int, float))
			) or not(isinstance(*c,(int, float))) :
        			raise ValueError("argment Error : argument must be a tuple integers or float")
    		if a == 0 :
        		raise ValueError("First element of tuple must not be 0")
    		return t
	```
	
## Tyes d'exceptions

Voici quelques exceptions courantes, et leurs utilisations
	
| exception | contexte |
------------------------
| :---: | :--- |
|`NameError` | accès à une variable inexistante dans l'espace de nom courant |
|`IndexError` | accès à un indice invalide d'une liste, d'un tuple, d'une chaine de caractères... |
|`KeyError` | accès à un indice invalide d'une liste, d'un tuple, d'une chaine de caractères... |
