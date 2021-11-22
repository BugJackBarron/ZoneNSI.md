# Modification des bases de données et requêtes complexes

*Les exemples et exercices donnés ci-dessous sont, sauf mention contraire, disponibles directement dans un [notebook Capytale](https://capytale2.ac-paris.fr/web/c-auth/list?returnto=/web/code/c156-162763){target=_blank}.*

##Modification des bases de données

### Suppression de lignes

Pour supprimer des lignes selon une condition donnée, on utilise l'ordre :

```` SQL
DELETE FROM table WHERE conditions;
````

!!! example "Exemple" 
	
	La requête suivante :
	
	````SQL
	SELECT * FROM emprunt WHERE code_barre='934701281931582';
	````
	
	donne la table suivante en réponse :
	
	<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>code_barre</th><th>isbn</th><th>retour</th></tr></thead><tbody><tr><td>934701281931582</td><td>978-2260019183</td><td>2020-01-01</td></tr><tr><td>934701281931582</td><td>978-2371240087</td><td>2020-01-01</td></tr></tbody></table>
	
	Pour supprimer la ligne référençant l'isbn `978-2260019183` :
	
	````SQL
	DELETE FROM emprunt WHERE code_barre='934701281931582' AND isbn='978-2260019183';
	````
	On vérifie ensuite :
	
	````SQL
	SELECT * FROM emprunt WHERE code_barre='934701281931582';
	````
	
	<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>code_barre</th><th>isbn</th><th>retour</th></tr></thead><tbody><tr><td>934701281931582</td><td>978-2371240087</td><td>2020-01-01</td></tr></tbody></table>
	
	
!!! warning "Quelques points de remarques"

	* L'**oubli** de la clause `WHERE` **supprime toutes les données** de la table ! Cependant la table existe encore et il est possible d'insérer de nouvelles données. Pour supprimer complètement une table, il faut utiliser l'instruction :
	
		```` SQL
		DROP TABLE nom_table;
		````
		
	* Il est impossible de supprimer une ligne dont l'absence violerait la contrainte de références (clé étrangère). Par exemple l'ordre suivant ne fonctionnera pas, car l'isbn donné est présent dans la table `emprunt` :
	
		```` SQL
		DELETE FROM livre WHERE isbn='934701281931582';
		````

!!! info "Tout ou rien"

	Si un ordre passé devant supprimer plusieurs lignes rencontre à un moment une erreur, alors **toutes les suppressions effectuées par cet ordre sont annulées** ! On parle d'éxecution de type &laquo: tout ou rien &raquo;.
	
### Mise à jour de lignes

Pour mettre à jour des lignes, on utiise un ordre SQL de type :

```` SQL
UPDATE nom_table
SET attribut1 = nouvelle_valeur1,
SET	attribut2 = nouvelle_valeur2,
...
WHERE conditions;	
````

!!! example "Exemple"

	La requête suivante :
	
	```` SQL
	SELECT * FROM usager WHERE prenom='ALAIN';
	````
	
	donne comme table résultat :
	
	<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>nom</th><th>prenom</th><th>adresse</th><th>cp</th><th>ville</th><th>email</th><th>code_barre</th></tr></thead><tbody><tr><td>MOREAU</td><td>ALAIN</td><td>48, Rue du Château</td><td>75005</td><td>Paris</td><td>amoreau1@abc.de</td><td>421921003090881</td></tr></tbody></table>
	
	Pour changer l'email de cet utilisateur, on peut utiliser l'ordre suivant :
	
	```` SQL
	UPDATE usager
	SET email = 'alain.moreau@truc.com'
	WHERE code_barre ='421921003090881';
	````
	et une nouvelle requête de recherche renvoie bien comme table :
	
	<table class="dataframe" border="1"><thead><tr style="text-align: right;"><th>nom</th><th>prenom</th><th>adresse</th><th>cp</th><th>ville</th><th>email</th><th>code_barre</th></tr></thead><tbody><tr><td>MOREAU</td><td>ALAIN</td><td>48, Rue du Château</td><td>75005</td><td>Paris</td><td>alain.moreau@truc.com</td><td>421921003090881</td></tr></tbody></table>

## Requêtes complexes

### Jointures

Jusqu'à présent, les requêtes que nous avons écrites ne nécessitent que l'utilisation d'une seule et unique table. mais bien souvent, nous avons a effectuer de requêtes récupérant des données de plusieurs tables simultanément.
Pour effectuer une telle requête il faudra utiliser une ou des {==**jointures de tables**==}.

!!! abstract "Jointure naturelle de deux tables"

Par exemple, 

### Requêtes imbriquées

## Exercices


		