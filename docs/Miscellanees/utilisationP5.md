# Petits introduction à l'utilisation du module P5 Python

!!! warning "Différents P5"

	Il existe différentes implémentations du module `P5` pour lesquelles les méthodes sont légèrement différentes dans leur écriture. Par exemple, pour créer une zone de dessin  de dimension $300 \times 200$ :
	
	* dans l'implémentation disponible sur Capytale, il faut utiliser `createCanvas(300,200)` ;
	* dans l'implémentation importée par Python 3.10, il faut utiliser `size(300,200)`.
	
	Dans tous les cas, pour connaître la liste exacte des méthodes disponibles :
	```` python
	import p5
	help(p5)
	````

## Le principe

### Un premier exemple

Un exemple d'utilisation de `p5` est donné dans la [documentation](https://github.com/p5py/p5) (en anglais). Je le donne et l'explicite ici :

```` python linenums="1"
from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    background(204)

def draw():
    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(255, 15)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

run()

````

### Description des fonctions

Dans la première ligne, on importe la totalité du module `p5`.

Le module `p5` utilise obligatoirement deux fonctions :

* la fonction `setup`, exécutée une seule fois, et permettant de régler un certain nombre de paramètres graphiques ;
* la fonction `draw`, exécutée à intervalle réguliers (par défaut tous les 60èmes de secondes), et qui à chaque appel trace sur le précédent canevas

Les fonctions `setup` et `draw` sont exécutées à l'appel de la fonction `run` (ligne 21). Il est possible de changer le paramètre `frame_rate` (par défaut 60), qui correspond au nombre d'appels de la fonction `draw` par secondes.

La fonction `key_pressed` est une fonction spcifique traitant les évènements liés au clavier, et est appelée dès qu'un évènement (touche pressée ou relâchée) est détecté.

### La fonction `setup`

```` python linenums="3"
def setup():
    size(640, 360)
    no_stroke()
    background(204)
````
Cette fonction **n'est exécutée qu'une seule fois** au déclenchement du programme.

* la fonction `size(640, 360)` fixe la taille de la fenêtre graphique (du canevas, ou du *sketch* en anglais) à une largeur de 640 pixels et une hauteur de 360 pixels.
* la fonction `no_stroke()` désactive le tracé des bordures de tous les objets suivants.