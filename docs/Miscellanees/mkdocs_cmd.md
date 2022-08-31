# Syntaxe des documents MkDocs

Pour la documentation complète : [mkdocs.org](https://www.mkdocs.org).

Documentation sur materials :  [materials reference ](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/)

La documentation sur le plugin **macro** : [macro plugin](https://mkdocs-macros-plugin.readthedocs.io/en/latest/#installation)

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

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Test code

``` python linenums="1"  hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```



<iframe src="https://trinket.io/embed/python/3d8d7ce66b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

 :smile:
 
 {--supprime--} et {++insere++} et {== Surligne ==}
 
## Keys

++ctrl++ => `++ctrl++`

++alt++ => `++alt++`

++delete++ => `++delete++`


## Latex

$$
 \dfrac{3}{4x}
$$

The homomorphism $f$ is injective if and only if its kernel is only the 
singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such 
that $f(a)=f(b)$.

## Admonitions (?)

!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

    ``` python
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

    Nunc eu odio eleifend, blandit leo a, volutpat sapien. Phasellus posuere in
    sem ut cursus. Nullam sit amet tincidunt ipsum, sit amet elementum turpis.
    Etiam ipsum quam, mattis in purus vitae, lacinia fermentum enim.


??? Question
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
	
	
!!! Note
	On teste l'auto deploiement
	
## Quelques points précis :

[https://squidfunk.github.io/mkdocs-material/reference/formatting/](https://squidfunk.github.io/mkdocs-material/reference/formatting/){:target="_blank"}