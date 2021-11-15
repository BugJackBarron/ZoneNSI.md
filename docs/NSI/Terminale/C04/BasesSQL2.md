# Requêtes SQL et mises à jour de données

*Les exemples et exercices donnés ci-dessous sont, sauf mention contraire, disponibles directement dans un [notebook Capytale](https://capytale2.ac-paris.fr/web/c-auth/list?returnto=/web/code/c156-162763){target=_blank}.*

## Requêtes d'interrogations de bases de données

### Projections

!!! abstract "Projection"
	L'opération de {==**projection**==} consite à ne récupérer que les champs (= les colonnes) d'une table donnée.
	En SQL, on l'obtiens par l'instruction :
	
	```` SQL
	SELECT
		colonne1, colonne2,...
	FROM
		nom_table;
	````
	
!!!example "Exemple 1 : Projection"
	Pour récupérer les colonnes `titre` et `isbn` de la table `livre` :
	```` SQL
	SELECT 
		titre, isbn
	FROM
		livre;
	````
	Pour récupérer l'intégralité des colonnes, on peut utiliser l'opérateur {==**joker**==}`*` :
	```` SQL
	SELECT 
		*
	FROM
		auteur;
	````
	
!!! tips "Renommer les colonnes"
	Il est possible dans une opération de projection de renommer les colonnes obtenues, grâce à l'opérateur `AS` :
	```` SQL
	SELECT 
		titre, isbn, annee AS annee_publication
	FROM
		livre;
	````

### Sélections

!!! abstract "Sélection (ou restriction)"
	L'opération de {==**sélection**==} consiste à interroger une base de données pour ne récupérer que les lignes d'une table correspondant à une ou des conditions spécifiées.
	
	En SQL, on rajoute la {==**clause**==} `WHERE` suivie des conditions exprimées sous la forme d'une **expression booléenne**, utilisant les mots clés `AND` et `OR` par exemple :
	
	```` SQL
		SELECT
			colonne1, colonne2,...
		FROM
			nom_table
		WHERE
			conditions;
	````
	
!!! example "Exemple 2 : Sélection"

	* Sélection avec condition unique :
	
		```` SQL
			SELECT 
				titre
			FROM
				livre
			WHERE
				annee >= 2020;
		````
	* Sélection avec conditions multiples :
	
		```` SQL
		SELECT 
			titre
		FROM
			livre
		WHERE
			annee >= 1970 AND
			annee <= 2000 AND
			editeur='Dargaud';
		````
		
!!! tips "Requête sur les chaînes de caractères"
	Si on veut chercher tous les livres dont le titre contient la chaîne `Astérix`, il faudra utiliser une clause comme la suivante :
	
	```` SQL
		SELECT 
			titre
		FROM
			livre
		WHERE
			titre LIKE '%Astérix%';
	````
	
	La chaîne de caractères `'%Astérix%'` s'appelle un {==**motif**==}. L'opération `s LIKE m` renverra `True` si la chaîne de caractères `s` correspond au motif `m`.
	Le caractère `%` est un {==**joker**==} qui peut-être substitué par **n'importe quelle chaîne**. Il existe aussi l'opérateur `_` (underscore) qui lui représente **n'importe quel caractère**. Ainsi, pour chercher tous les auteurs dont le nom commence par F, se termine par R et fait 6 caractères de long :	
	
	````SQL
		SELECT
			nom, prenom
		FROM
			auteur
		WHERE
			nom LIKE 'F____R';
	````
	
### Fonctions d'aggrégats


### Tri et suppression des doublons

## Jointures de tables


	
	

		