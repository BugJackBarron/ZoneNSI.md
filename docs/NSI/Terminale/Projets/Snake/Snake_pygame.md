# Projet : Snake avec Pygame-ce

## Le jeu

Le joueur dirige un serpent sur une grille avec les flèches du clavier. Le serpent avance seul, case par case. Chaque pomme mangée le fait grandir d'une case et augmente le score. La partie est perdue si le serpent sort de la grille ou se mord la queue.

!!! info "Pygame ou Pygame-ce ?"
    `pygame-ce` (*Community Edition*) est une version de Pygame maintenue activement par la communauté. Elle s'importe exactement comme Pygame : `import pygame`. Son installation est :

    ```bash
    pip install pygame-ce
    ```

    Ne pas installer `pygame` et `pygame-ce` dans le même environnement : les deux paquets utilisent le même nom de module et se gênent.

## Les idées clés

### La grille

Plutôt que de manipuler des pixels, on travaille sur une **grille de cases**. Une position est un couple `(colonne, ligne)`, et c'est seulement à l'affichage qu'on la multiplie par la taille d'une case :

```python
pg.draw.rect(surface, couleur, (x * CASE, y * CASE, CASE, CASE))
```

### Le serpent

Le serpent est une **liste de positions**, la tête étant en position `0`. Pour avancer :

1. on insère la nouvelle tête au début de la liste ;
2. on supprime la dernière case (la queue), **sauf** si le serpent vient de manger une pomme, ce qui le fait grandir.

### Le temps

Le jeu est affiché à 60 images par seconde, mais le serpent ne doit avancer que toutes les 100 à 200 ms. On mesure le temps écoulé depuis le dernier pas avec `Clock.tick()` (qui renvoie des millisecondes) et on ne déplace le serpent que lorsqu'un délai est dépassé. Réduire ce délai quand le score augmente accélère le jeu.

### La boucle de jeu

Elle répète toujours les trois mêmes étapes :

```python
while en_cours :
    gerer_evenements()   # clavier, fermeture de la fenêtre
    mettre_a_jour()      # déplacement, collisions, score
    afficher()           # dessin de l'image
```

## Pistes d'organisation du code

### Constantes

Regrouper en tête de fichier : taille d'une case, dimensions de la grille, couleurs, vitesse, directions (`HAUT = (0, -1)`, etc.).

### Classe `Serpent`

| Élément | Rôle |
|---|---|
| `corps` | liste des positions, la tête en premier |
| `direction` | direction actuelle |
| `avancer()` | déplace le serpent d'une case |
| `grandir()` | le prochain `avancer()` ne supprime pas la queue |
| `changer_direction(d)` | change de direction en interdisant le demi-tour |
| `mord_sa_queue()` | `True` si la tête est dans le reste du corps |
| `sort_de_la_grille()` | `True` si la tête est hors de la grille |
| `afficher(surface)` | dessine chaque case |

### Classe `Pomme`

* un attribut `position` ;
* `replacer(serpent)` : tire une case au hasard **qui n'est pas occupée par le serpent** ;
* `afficher(surface)`.

### Classe `Jeu`

Elle contient la fenêtre, l'horloge, le serpent, la pomme et le score, et possède les méthodes :

* `reinitialiser()` : démarre une nouvelle partie ;
* `gerer_evenements()` : lit le clavier ;
* `mettre_a_jour(dt)` : fait avancer le jeu et teste les collisions et la pomme ;
* `afficher()` : dessine l'image complète ;
* `lancer()` : la boucle principale.



## Pour aller plus loin

* meilleur score sauvegardé dans un fichier ;
* écran de menu et de fin ;
* obstacles, pommes bonus, murs traversables (le serpent réapparaît de l'autre côté avec un modulo) ;
* sons et images à la place des rectangles ;
* deux joueurs sur le même clavier.

