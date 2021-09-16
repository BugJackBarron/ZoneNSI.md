# Bases de Pygame

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

3. **Importation complète avec import des constantes drectement dans l'espace de nommage (conseillé)** :
  
    import pygame
    from pygame.locals import *
    
   Dans ce cas, pour utiliser la 
## Création d'une fenêtre graphique

## Ajout d'image de Fond

## Ajout d'un sprite

## Rafraichissement de l'écran et boucle d'évènements

## 
