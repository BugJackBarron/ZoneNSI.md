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
	2. `trois,4,5`
	3. `3,4,5,6` ;
	4. `0,3,4`
	
	Dans chacun des cas, qu'obtient-on en sortie ? Pourquoi ?
	
??? done "Solution"
	=== "`3,4,5`"
		La sortie est :
		
			`y = 22.0(x-3) + 44.0`
		
		qui est correcte.