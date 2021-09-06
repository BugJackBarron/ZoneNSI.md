# Gestion des exceptions

## Un exemple d'erreur à ne pas commettre


!!! abstract "Utilisation malheureuse d'un module"
	Reprenons le module `secondDegre.py`, mais en temps qu'utilisateur. Nous
	connaissons l'interface qui nous a été fournie par l'auteur. Pour tester le module
	nous lançons le script suivant, nommé `testModule.py`, et situé dans le même dossier que `secondDegre.py` :
	``` python
		import secondDegre as sD

		p = input("Donnez les coefficients du polynome séparés par des virgules :")
		p = sD.polynome(p.split(","))

		print(sD.tangente(p,3))
	```
