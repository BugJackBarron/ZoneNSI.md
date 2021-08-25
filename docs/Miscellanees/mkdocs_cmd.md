# Syntaxe des documents MkDocs

## Bases de la syntaxe Markdown

Le langage **Mardown** est en langage de balise simple, utilisé entre autres dans les notebooks Jupyter, et pour lequel les règles d'utilisation sont simples :

* La mise en **gras** se fait par en encadrant par 2 étoiles  : `**Gras**` -> **Gras**.
* La mise en *italique* se fait par en encadrant par 1 étoile  : `*Italique*` -> *Italique*.

* Les titres de différents niveaux sont obtenus en utilisant un certain nombre de  dièse `#`
* Les images sont insérées par la commande ````![Alt text](/path/to/img.jpg "Optional title")````
* Un texte sans fortmatage est obtenu en encadrant par des guillemets invversés \` : ` '**Truc**' ` n'est pas mis en forme

Pour utiliser un caractère \* simple, il faut l'échapper avec un backslash \\, comme pour tous les autres caractère spéciaux.  

## Les citations

Pour  insérer une citation, on utilise le chevron \> devant chaque ligne de code :
````
	> Voici une citation
	
	> sur plusieurs lignes.
````
donnera 
> Voici une citation

> sur plusieurs lignes.

A noter que si on ne saute pas de ligne, MkDocs formate selon la loingueur de la ligne courante :
Pour  insérer une citation, on utilise le chevron \> devant chaque ligne de code :
````
	> Voici une citation
	> sur une seule ligne.
````
donnera 
> Voici une citation
> sur une seule ligne.




## Les hyperliens

Le fonctionnement des hyperlmens est particulier à MkDocs, donc ce qui suit n'est pas toujours valable dans 
n'importe quel environnement lisant du **MarkDown**.

Le principe de base : ``` [texte de remplacement](adresse du document)```

Il est possible de référer à des documents internes en utilisant leur chemin relatif.
````Please see the [project license](../about/license.md) for further details.````

Il est possible de faire une référence à une partie spécifique d'un document par l'intermédiaire d'ID générées automatiquement par MkDocs pour chaque **header** (⚠️ les noms sont en minuscules et les caractères spéciaux - y compris les espaces, sont remplacé par des tirets. lers tirets doubles sont alors réduits à un simple tiret).

Ainsi le lien ``[ceci](mkdocs_cmd.md#syntaxe-des-documents-mkdocs)`` renvoie [ici](mkdocs_cmd.md#syntaxe-des-documents-mkdocs) renvoie vers le header de cette partie.


## Modules de MkDocs-Material

### 