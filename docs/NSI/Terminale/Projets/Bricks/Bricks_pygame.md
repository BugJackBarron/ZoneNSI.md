# Projet : Casse-briques avec Pygame-ce

## Le jeu

Le joueur déplace une raquette en bas de l'écran avec les flèches gauche et droite pour renvoyer une balle vers un mur de briques. Chaque brique touchée disparaît et rapporte des points. Si la balle tombe sous la raquette, le joueur perd une vie. La partie est gagnée quand toutes les briques sont détruites, et perdue quand il n'y a plus de vie.

!!! info "Installation"
    ```bash
    pip install pygame-ce
    ```
    `pygame-ce` s'importe comme Pygame (`import pygame`). Ne pas installer `pygame` et `pygame-ce` dans le même environnement.

## Les idées clés

### Le mouvement indépendant de l'ordinateur

Contrairement au Snake, tout bouge de façon continue. Pour qu'une balle ait la même vitesse sur tous les ordinateurs, on exprime les vitesses en **pixels par seconde** et on multiplie par le temps écoulé depuis la dernière image, noté `dt` :

```python
dt = horloge.tick(60) / 1000     # secondes écoulées depuis l'image précédente
x += vx * dt
```

### Des positions décimales

Un `pygame.Rect` ne contient que des entiers : une vitesse de 3,4 pixels par image serait arrondie et le mouvement serait faux. On conserve donc la position de la balle et de la raquette dans des attributs `float`, et on ne les arrondit qu'au moment de l'affichage ou du calcul des collisions.

### Les rebonds

La balle a un vecteur vitesse `(vx, vy)`. Un rebond consiste à **inverser une composante** :

* mur de gauche ou de droite : `vx = -vx` ;
* plafond : `vy = -vy`.

!!! tip "Ne pas inverser, mais imposer le signe"
    Écrire `vx = abs(vx)` contre le mur de gauche (et `-abs(vx)` contre celui de droite) plutôt que `vx = -vx`. Si la balle est restée plusieurs images dans le mur, une simple inversion la ferait osciller sans jamais en sortir.

### Rebond sur la raquette

Si la balle rebondit toujours de la même façon, le joueur ne peut pas la diriger. On calcule donc l'angle de renvoi selon l'endroit touché : au centre, la balle repart tout droit ; sur les bords, elle repart en biais (jusqu'à 60°).

```python
position = (balle.x - raquette.centerx) / (largeur_raquette / 2)    # entre -1 et 1
angle = radians(position * 60)
vx = vitesse * sin(angle)
vy = -vitesse * cos(angle)
```

### Rebond sur une brique

Quand la balle chevauche une brique, il faut décider si le choc est **latéral** (on inverse `vx`) ou **vertical** (on inverse `vy`). Une méthode simple : calculer de combien la balle est entrée dans la brique horizontalement (`dx`) et verticalement (`dy`) ; le rebond se fait sur l'axe où la pénétration est **la plus faible**.

### La boucle de jeu

```python
while en_cours :
    dt = horloge.tick(FPS) / 1000
    en_cours = gerer_evenements()
    mettre_a_jour(dt)
    afficher()
```

## Pistes d'organisation du code

### Constantes

Dimensions de la fenêtre, de la raquette, des briques, vitesses, nombre de lignes et de colonnes de briques, nombre de vies, couleurs.

### Classe `Raquette`

| Élément | Rôle |
|---|---|
| `rect` | rectangle utilisé pour l'affichage et les collisions |
| `x` | position décimale |
| `deplacer(direction, dt)` | déplace la raquette (`-1`, `0` ou `1`) en la gardant dans la fenêtre |
| `afficher(surface)` | dessine la raquette |

### Classe `Balle`

| Élément | Rôle |
|---|---|
| `x`, `y`, `vx`, `vy` | position et vitesse |
| `collee` | `True` tant que la balle est posée sur la raquette |
| `lancer()` | donne sa vitesse à la balle |
| `deplacer(dt)` | fait avancer la balle |
| `rebondir_murs()` | rebonds sur les trois murs |
| `rebondir_raquette(raquette)` | rebond avec calcul de l'angle |
| `rebondir_brique(brique)` | rebond sur l'axe de moindre pénétration |
| `est_perdue()` | `True` si la balle est sortie par le bas |

### Classe `Brique`

* un `rect`, une couleur et une valeur en points ;
* `afficher(surface)`.

Une fonction `creer_briques()` construit la grille de briques avec deux boucles imbriquées.

### Classe `Jeu`

Elle possède la fenêtre, l'horloge, la raquette, la balle, la liste des briques, le score, les vies et un **état** (`"jeu"`, `"perdu"` ou `"gagne"`). Ses méthodes : `reinitialiser()`, `gerer_evenements()`, `mettre_a_jour(dt)`, `gerer_briques()`, `afficher()` et `lancer()`.



## Pour aller plus loin

* plusieurs niveaux avec des dispositions de briques différentes (un tableau de chaînes de caractères pour décrire chaque niveau) ;
* briques qui demandent plusieurs coups ;
* bonus qui tombent des briques (raquette plus large, balles multiples, vie supplémentaire) ;
* contrôle à la souris ;
* meilleur score sauvegardé, sons, images.
