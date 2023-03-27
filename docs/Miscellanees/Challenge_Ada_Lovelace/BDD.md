# Les bases de données et le SQL

## Une brève introduction aux bases de données

!!! info "Vocabulaire"
    Une base de donnée peut être représentée comme un ensemble de {==**tables**==}, où chaque table possède plusieurs {==**colonnes**==} nommées.

    Une donnée est alors {==**une ligne**==} d'une des tables.

Prenons par exemple la base de donnée suivante concernant des groupes de musiques:

![Exemple BDD](../../NSI/Terminale/C04/modeleRelationnel1.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}

Il y a 4 tables :

* la table `chanteur`, comportant 3 colonnes :
    * `idc` : un numéro d'identifiant (un nombre entier `int` ou `INTEGER`);
    * `nom` : le nom du chanteur (une chaine de caractères `string`ou `VARCHAR`) ;
    * `prenom` : le prénom du chanteur (une chaine de caractères `string`ou `VARCHAR`) ;
* la table `groupe`, comportant 3 colonnes :
    * `idG` : : un numéro d'identifiant (un nombre entier `int` ou `INTEGER`);
    * `nom` : le nom du groupe (une chaine de caractères `string`ou `VARCHAR`) ;
    * `id_style` : un numéro d'identifiant lié à la table `style` (un nombre entier `int` ou `INTEGER`);
* la table `style` avec deux colonnes qu'on ne détaillera pas ici ;
* la table `album` avec quatre colonnes qu'on ne détaillera pas ici.

En liant les tables les unes aux autres grâce aux identifiants, on peut alors savoir que :

* L'album *Fortitude* vient du groupe d'identifiant `5`, qui est *Gojira*, dont le style est `2`, c'est-à-dire *Métal* ;
* Le chanteur de l'album *Era Vulgaris* est d'identifiant `2`, et se nomme `Josh Homme`.
* etc.

## Utilisation du langage SQL

### Présentation

Le langage `SQL` est un langage spécifique inventé pour communiquer avec des bases de données à l'aide de {==**requêtes**==}. Les requêtes peuvent être de différentes natures :

* interroger une table de la base de donnée, par exemple renvoyer les noms de tous les chanteurs ou chercher tous les albums du groupe d'identifiant `5` ;
* interroger plusieurs tables de la base de donnée en les liant, par exemple pour renvoyer tous les noms des groupes dont `Josh Homme`est le chanteur ;
* insérer une nouvelle ligne de données dans une table ;
* modifier les données d'une ligne d'une table ;
* supprimer une ligne d'une table.

### Quelques lignes de code

#### Requêtes d'interrogations simples

Chercher les noms de tous les chanteurs :

```` SQL
SELECT Nom FROM Chanteur ;
````
Chercher tous les albums du groupe d'identifiant 5 :

``` SQL
SELECT Titre FROM Album WHERE id_Groupe = 5 ;
```

#### Requêtes d'interrogations complexes

Rechercher les titres des albums dont Josh Homme est le chanteur :

``` SQL
SELECT Album.Titre 
FROM Album JOIN Chanteur ON Album.id_Chanteur == Chanteur.idC
WHERE Chanteur. nom = "Homme" and Chanteur.prenom = "Josh"
```
#### Insérer des données dans une table

Insérer deux nouveaux styles dans la table `Style` :

``` SQL
INSERT INTO Style VALUES 
(3, 'Reggae'),
(4, 'Rap'),
(5, 'HardRock');
```

Insérer une ligne incomplète dans la table `Groupe` :

``` SQL
INSERT INTO Groupe(idG, nom) VALUES
(6, 'ACDC');
``` 

!!! warning "Les données NULL"

    Dans une BDD, parfois certaines informations ne sont pas renseignées. Elles ont alors une valeur `NULL`.

#### Changer des données

Ajouter le style *HardRock* au groupe *ACDC* :

``` SQL
UPDATE Groupe
SET id_Style = 5
WHERE nom = 'ACDC';
```

#### Supprimer des données

Pour supprimer la ligne correspondant à l'album `Fortitude` :

``` SQL

DELETE FROM Album
WHERE Titre='Fortitude';
```
## Utilisation de PHP

`PHP` (*Personnal Home Page*) est un langage de programmation utilisé principalement sur le web, côté {==**serveur**==}, ce qui signifie qu'il travaille du côté de la machine serveur, pour fabriquer la page web demandée par le {==**client**==}. Un code en PHP peut être intégré au sein d'une page `HTML` grâce à une balise spéciale : `< ?PHP .... ?>`

!!! info "A lire"

    On pourra simplement considérer que, pour construire une page web **liée à `PHP`** :

    * on construit un squelette de page en `HTML`, comme d'habitude ;
    * **seules les informations spécifiques** seront intégrées à la page au moment de la construction, en remplaçant certaines parties de texte

    Considérons par exemple le morceau de code HTML suivant :

    ``` PHP
    <p> Bonjour <?php echo $name ?> ! </p>
    ```

    * on a du code `HTML` classique, avec une balise `<p>` ;
    * au sein de ce code, on à la balise `<?PHP ... ?>`, qui introduit du code ;
    * le code PHP consiste à écrire dans le `HTML` (commande `echo`) le contenu de la variable `$name`.

### Les variables

En PHP, les variables sont crées grâce au symbole `$`. On peut définir des variables comme montré ci-dessous :

```PHP 
<?php
  $prenom = 'Ada';  // Type string (chaine de caractères avec deux guillemets simples)
  $nom = "Lovelace";    // Type string ( avec deux guillemets doubles)
  $age = 25;    // Type entier
  $estLyceenne = true;  // Type booléen
  $competences = array('anglais','mathématiques','informatique','algorithmique'); // Type tableau
  
?>
```

On peut alors utiliser les variables comme dans tout autre langage :

``` PHP
<?php
$double_age = $age * 2 ; // la variable vaudra alors 50
$nom_complet = $nom.' '.$prenom //Operation de concaténation avec .
// La chaine de caractere associée à $nom_complet est alors 
// 'Lovelace Ada'
?>
```

