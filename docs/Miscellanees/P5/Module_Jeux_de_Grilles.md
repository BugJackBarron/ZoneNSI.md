# Module Jeux de Grille pour P5 Capytale

Ce module, disponible [ici](https://github.com/LuxuriousCobra/gitStage/tree/main/Projet%20jeux%20de%20grilles){target="_blank"} a été créé par Stanislas Le Quellec lors de son stage de 3ème année de Licence d'info à l'ISTIc de Rennes. Il a pour objectif de simplifier la création de jeux de grilles (morpion, reversi, etc.) avec la version du module `p5` disponible sur Capytale.

En voici un descriptif succinct :

## Classe `Interface`

### Méthode constructeur `Interface`

* `tGrille` : taille en pixels d'une case (obligatoire) ;
* `lGrille` : nombre de lignes et de colonnes (obligatoire) ;
* `val` : argument optionnel, par défaut `None`, une valeur, de type `None` ou `Forme` insérée par défaut dans chaque case ;
* `estDamier` : booléen par défaut `False`, si égal à `True`, la grille sera un damier avec deux couleurs, la première case en haut à gauche sera blanche ;
* `cDamier` : tuple par défaut `('white' , 'black')`, contenant les couleurs du damier. N'a pas d'effet si `estDamier` est `False`.

### Méthodes de la classe `Interface`


* `ajouterForme (matX, matY, nomF, couleurF= None)` : ajoute une forme dans la case de coordonnées `(matX, matY)`. Les formes possibles sont : ` "carre"`, `"triangle"`, `"cercle"`, `"croix"`, `"etoile"`, `"losange"`, `None` ou une image disponible. `couleurF` couleur de la forme à dessiner. Le nom renseigné doit être en anglais. Ex : `"red"` -> valide. `"Bleu"` -> invalide.
* `supprimerForme(self, matX, matY)` : supprime la forme dans la case de coordonnées `(matX, matY)`.
* `reset()` : remet le nom de toutes les formes de la matrice à `None`.
* `lierTouche(touche, fonction):` : lie une touche à une fonction. `touche` le code ou le nom de la touche. Ex : `"ENTER"` (touche entrée), `"d"` la touche D du clavier ou `"left"` le clic gauche de la souris.
* `gereAppuieTouche(touche)` : appelle la fonction liée à `touche`.
* `getCasePointee()` : renvoie la case sur laquelle se trouve le pointeur de la souris ou `None` s'il est en dehors de la grille.
* `getSize()` : renvoie la taille de la grille (le nombre de lignes, et donc le nombre de colonnes).
* `getCase(matX, matY)` : renvoie le nom de la forme dans la grille à la position `(matX, matY)`.
* `getMatrix()` : renvoie sous la forme d'une liste les formes présentes dans la grille.
* `getRandomEmptyCase()` : renvoie les coordonnées d'une case vide aléatoire de la grille, et `None` sinon.
* `run()` : exécute le code. Appelle les méthodes `setup` et `draw` classiques de `p5`.
* `stop()` : arrête l'interface.

### Exemple d'utilisation 

```python
i = Interface(400, 11, estDamier = True, cDamier = ("hotpink", "darkorange"))
i.reset()

def clicGauche() :
    c = i.getCasePointee()

    if (c != None) :
        i.ajouterForme(c.X, c.Y, "grosChat.png")
        
def clicDroit() :
    c = i.getCasePointee()
    if (c != None) :
        i.supprimerForme(c.X, c.Y)
        
i.lierTouche('left', clicGauche)
i.lierTouche('right', clicDroit)

i.run()
```

## Exemple d'application

Voir le fichier sur [Capytale](https://capytale2.ac-paris.fr/web/c/1eb9-7136590){target="_blank"}

!!! danger "Problèmes"

    Il y a encore un certain nombres de limites au module. Elles seront corrigées au fur et à mesure des problèmes rencontrés.