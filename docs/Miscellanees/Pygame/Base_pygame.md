# Bases de Pygame

Ce cours est très largement et assez honteusement copié sur [celui-ci](http://sdz.tdct.org/sdz/interface-graphique-pygame-pour-python.html#Lesinterfacesgraphiques). Merci à vous ! En cas de soucis de droits, n'hésitez pas à me contacter par le lien  situé en bas de page !

## Importer Pygame et ses constantes

`Pygame` est une bibliothèque, et en tant que telle, elle est construite à partir de plusieurs modules. Les noms de ces modules sont :

* display
* mixer
* draw
* event
* image
* mouse
* time

Il existe alors plusieurs possibilités pour importe `pygame` 

1. **Importation complète** :

		import pygame
    
	La totalité de la bibliothèque est alors importée, et pour utiliser la fonction `update` du module `display` on devra alors utiliser `pygame.display.update()`.

2. **Importation partielle des modules nécessaires** :

		from pygame import display
    
	Seul le module display est alors importé, et pour utiliser la fonction `update` de ce module, on devra alors utiliser `display.update()`. 

3. **Importation complète avec import des constantes directement dans l'espace de nommage (conseillée)** :
  
		import pygame
		from pygame.locals import *
    
	Dans ce cas, pour utiliser la constante représentant la touche espace, au lieu d'utiliser `pygame.locals.K_SPACE`, on utilisera simplement `K_SPACE`.
## Création d'une fenêtre graphique et boucle d'évènements

!!! abstract "Le projet"
	Commençons un petit programme qui nous amènera à déplacer un personnage de gauche à droite sur un fond d'écran, pendant que des balles tombent depuis le haut de l'écran à différentes vitesses. Le jeu consistera à éviter que le personnage entre en collision avec les balles, et s'arrêtera dès qu'une collision aura lieu.

Le premier point est d'afficher une fenêtre graphique d'une dimension donnée : $640 \times 480~ pixels^2$ (oui, en bon prof de maths, je respecte à minima les unités...).

On utilise le script suivant, dans un fichier nommé `dodgeTheBall.py` :
``` python linenums="1"

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
```

!!! abstract "Analysons le code"

	* Dans les deux premières lignes, nous importons `pygame` en totalité ainsi que les constantes spécifiques dans l'espace de nommage courant.
	* En ligne 4, nous initialisons tous les modules de `pygame`.
	* En ligne 6, nous appelons ensuite la fonction `set_mode()` contenue dans le module `display` de `pygame`, qui prend en argument un **tuple** contenant la **largeur et la hauteur de la fenêtre voulue** (attention, c'est bien un tuple ! `pygame.display.set_mode(640, 480)` ne fonctionne pas !).
	
??? bug "Y'a un bug !"

	La fenêtre reste bloquée  et ne se ferme pas sauf si on force l'arrêt du script !
 
	Effectivement, on se retrouve bloqué... Il faut rajouter à notre code une instruction supplémentaire pour que la fenëtre se ferme :
	``` python linenums="1"

	import pygame
	from pygame.locals import *

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))

	pygame.quit()
	```

??? bug "Encore un"
		
	Et oui ! Notre fenêtre s'ouvre mais se ferme immédiatement !
	
	Or nous aimerions qu'elle ne se ferme que sur demande explicite de l'utilisateur, par exemple par un clic sur la croix.
	
C'est là qu'intervient la notion de **boucle d'évènements**. 

Dans un programme classique, en *programmation impérative*, le programme se déroule plus ou moins linéairement de la première ligne à la dernière. Mais lorsqu'on utilise des **interfaces graphiques**, on ne peut prévoir à l'avance le comportement de l'utilisateur, et donc suivre un chemin clairement défini à l'avance. C'est pour cette raison qu'on utilise plutôt le paradigme de la **programmation événementielle**, c'est-à-dire un  paradigme où on prévoira l'action de l'utilisateur, mais pas dans un ordre précis. Chaque action prévue dans la **boucle d'évènements** aura un impact précis.

Dans notre cas, nous souhaiterions que la fenêtre reste ouverte **tant que l'utilisateur** n'a pas exprimé le désir de la fermer, soit par l'intermédiaire de la croix, soit par l'intermédiaire de la combinaison de touches ++alt+f4++.

!!! info "Notion d'évènements"

	Dans la construction d'interfaces graphiques, on utilise souvent la notion d'*évènements*. Un évènement correspond à :
	
	* un déplacement de la souris ;
	* le survol d'une zone spécifique de l'écran par le pointeur de la souris ;
	* un appui sur une ou plusieurs touches du clavier :
	* le relâchement d'une touche de clavier ;
	* un appui ou relâchement d'un bouton de la souris ;
	* un événement spécifique prévu dans le programme ;
	* un changement de luminosité devant un capteur vidéo ;
	* ...
	
	Ces évènements sont stockés à leur apparition dans une **file**(fifo) de **dimension limitée**, nettoyée régulièrement de ses évènements les plus anciens. 
	

Dans `pygame`, les évènements sont des constantes, et celui qui nous intéresse est l'évènement `QUIT`. Nous allons donc parcourir la liste des évènements pour ensuite pouvoir quitter la fenêtre si celui-ci est exprimé :
``` python linenums="1"

import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

for event in pygame.event.get() :
	if event == QUIT :
		pygame.quit()
```

??? bug "L'arnaque : ça ne marche pas !"

	On retombe sur notre problème précédent : la fenêtre ne se ferme plus...
	
	C'est parce que la **file** d'évènements se construit et se nettoie très rapidement ! Nous n'avons pas le temps de cliquer sur la croix que déjà le parcours par la boucle `for` est terminé ! Et donc dans ce cas **on ne passe jamais par l'instruction `pygame.quit()`.**
	
	Il va donc falloir répéter la lecture d'évènements pour pouvoir détecter quand l'utilisateur souhaite fermer sa fenêtre.
	

!!! info "Boucle d'évènements"

	Une boucle d'évènements est une boucle qui se répète tant qu'un évènement précis ne s'est pas produit. A chaque tour de boucle on va lire la totalité des évènements enregistrés dans la file, et on déclenchera la sortie de cette boucle si l'évènement est trouvé.
	<p align="center">
	![event loop](Boucle1.png){width = 10%}
	</p>
	
Pour notre exemple, nous allons créer une boucle `while` dépendant d'une variable `continuer` initialisée à `True`, que nous basculerons à `False` lorsque l'évènement `QUIT` est intercepté :


??? done "Un code fonctionnel"

	``` python linenums="1"
	import pygame
	from pygame.locals import *

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))

	continuer = True
	while continuer :
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = False

	pygame.quit()
	```

	Enfin ! Notre fenêtre fonctionne !


## Ajout d'image de Fond

!!! abstract "Image de fond"
	Notre fond noir est un peu déprimant. Mettons un peu de verdure grâce à l'image suivante :
	<p align="center">
	![background](background.jpg){width = "10%";}
	</p>
	Téléchargez cette image sous le nom `background.jpg` puis ajoutez la ligne suivante en ligne 7 :
	
	``` python linenums="7"
	fond = pygame.image.load("background.jpg").convert()
	```
Bon : mauvaise nouvelle, **ce ne sera pas suffisant !**
	
La variable `fond` n'est qu'une référence à une `Surface` de `pygame`, retournée par la fonction `load()`. Une `Surface` est une classe d'objets définie dans `pygame` qui possède de nombreux attributs et méthodes (cf. [la doc](https://www.pygame.org/docs/ref/surface.html) ). La **méthode** `convert()` des objets `Surface` sert à convertir l'image source au format utilisé par `pygame`.

Le principe d'affichage de la **SDL** (la sous-couche logicielle gérant les images, le son, etc...) est à connaître pour bien afficher ses images : 
`fenetre` est une surface vide, sur laquelle on va "coller", ou "empiler" les autres images. **Le fond doit donc être empilé sur la surface vide de la fenêtre**, grâce à la méthode `blit()`. Cette méthode prend une `Surface` en argument ainsi qu'un *tuple* représentant les **coordonnées du coin supérieur gauche** auquel sera collé la `Surface` argument par rapport à la `Surface` appelante.

!!! info "Système de coordonnées"
	On peut donner comme exemples de *tuple* de coordonnées ceux de l'image suivante :
	<p align="center">
	![coordinates](Screen.png){width = "10%";}
	</p>

On pourrait donc utiliser le code suivant :


``` python linenums="1"
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()

continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

pygame.quit()
``` 

??? bug "Mais pourquoi ça n'affiche rien !"
	
	Parce que quand on `blit` une `Surface`, `pygame` calcule ce qu'il faut mais ne l'exécute pas réellement. Il faut forcer le rafraichissement de l'écran pour y parvenir, par l'intermédiare de la commande `pygame.display.update()`. 
	
	Comme nous comptons bien faire bouger un personnage sur l'écran, et que les mouvements de celui-ci dépendront de la boucle d'évènements, autant mettre immédiatement cette commande en fin de boucle, pour que l'image soit systématiquement mise à jour. :
	
	``` python linenums="1"
	
	import pygame
	from pygame.locals import *

	pygame.init()

	fenetre = pygame.display.set_mode((640, 480))
	fond = pygame.image.load("background.jpg").convert()
	fenetre.blit(fond,(0,0))
	continuer = True
	while continuer :
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = False
		pygame.display.update()
	pygame.quit()
	``` 
	Et voilà ! 15 lignes de code, et nous voilà avec une fenêtre graphique digne de ce nom !


## Ajout du sprite du joueur

## Déplacement du joueur

## Création d'une classe d'objets "Balle"

## Apparition des objets "Balles"

## Gestion des collisions
