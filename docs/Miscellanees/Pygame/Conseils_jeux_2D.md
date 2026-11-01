# Conseils pour créer un jeu vidéo 2D avec Pygame-ce

Cette fiche rassemble des conseils généraux pour structurer un jeu 2D, accompagnés de vidéos présentant les concepts principaux. Les exemples de code sont écrits pour `pygame-ce` (`pip install pygame-ce`, puis `import pygame`).

!!! info "À propos des vidéos"
    Toutes les vidéos proposées sont en **anglais** (sous-titres automatiques disponibles sur YouTube). Les liens ont été vérifiés lors de la rédaction de cette fiche, mais une vidéo peut disparaître ou changer d'adresse : en cas de lien mort, chercher le titre indiqué.

## Démarrer avec Pygame-ce

Pour une première vue d'ensemble (fenêtre, images, texte, collisions, sons, états du jeu) en construisant un petit jeu complet :

* 🎬 [The ultimate introduction to Pygame](https://www.youtube.com/watch?v=AY9MnQ4x3zk) – *Clear Code*

## La boucle de jeu

Tout jeu vidéo répète indéfiniment trois étapes :

```python
while en_cours :
    gerer_evenements()    # clavier, souris, fermeture de la fenêtre
    mettre_a_jour(dt)     # déplacements, collisions, score, règles du jeu
    afficher()            # dessin de l'image complète
```

**Conseils**

* Séparer nettement ces trois étapes : on ne dessine **pas** pendant qu'on calcule, et on ne calcule pas pendant qu'on dessine.
* Appeler `pygame.display.flip()` (ou `update()`) **une seule fois** par tour de boucle, à la fin de l'affichage.
* Effacer l'écran (`fill` ou nouveau fond) au début de chaque affichage, sinon les images successives se superposent.
* Gérer proprement la sortie : tester `pygame.QUIT` et une touche comme Échap, puis appeler `pygame.quit()` en fin de programme.

## Le temps : FPS et delta time

`Clock.tick(60)` limite le jeu à 60 images par seconde et **renvoie le temps écoulé en millisecondes** depuis l'appel précédent.

```python
horloge = pygame.time.Clock()
dt = horloge.tick(60) / 1000     # secondes écoulées depuis la dernière image
x += vitesse * dt                # vitesse en pixels par seconde
```

* Exprimer les vitesses en **pixels par seconde** et les multiplier par `dt` : le jeu va à la même vitesse sur tous les ordinateurs.
* Pour un mouvement par cases (Snake, Tetris), accumuler `dt` et ne déplacer qu'à l'expiration d'un délai.
* Conserver les positions dans des variables `float` : un `Rect` ne contient que des entiers, ce qui fausse les petites vitesses.

* 🎬 [Understanding framerate independence and deltatime](https://www.youtube.com/watch?v=rWtfClpWSb8) – *Clear Code*
* 🎬 [Pygame Framerate Independence Tutorial: Delta Time Movement](https://www.youtube.com/watch?v=XuyrHE6GIsc) – *CDcodes*

## Rectangles, images et sprites

* Chaque image (`Surface`) possède un `get_rect()` : c'est lui qui sert à **positionner** (`rect.center`, `rect.midbottom`, `rect.topleft`…) et à **détecter les collisions**.
* Charger les images et les polices **une seule fois**, avant la boucle, jamais à chaque image. Appeler `convert()` ou `convert_alpha()` après `pygame.image.load()` accélère nettement l'affichage.
* Dès que plusieurs objets se ressemblent (ennemis, projectiles, briques), les regrouper dans des classes, et si besoin dans `pygame.sprite.Sprite` et `pygame.sprite.Group`, qui permettent de les mettre à jour et de les dessiner d'un seul appel.

* 🎬 [Pygame Sprites And Groups Explained!](https://www.youtube.com/watch?v=4TfZjhw0J-8) – *Coding With Russ*

## Les collisions

* **Rectangles** : `rect_a.colliderect(rect_b)` suffit dans la grande majorité des jeux. Réduire un peu le rectangle de collision (`rect.inflate(-10, -10)`) donne souvent un jeu plus « juste » pour le joueur.
* **Point dans un rectangle** : `rect.collidepoint(pos)`, par exemple pour un clic sur un bouton.
* **Cercles** : comparer la distance entre les centres à la somme des rayons.
* **Groupes** : `pygame.sprite.spritecollide` et `groupcollide`.
* **Réaction** : détecter une collision ne suffit pas, il faut décider quoi faire (rebond, dégâts, ramassage…). Pour un rebond, inverser la composante de vitesse de l'axe touché, et replacer l'objet **hors** de l'obstacle pour éviter qu'il reste collé.
* **Objets rapides** : un objet qui avance de plus que l'épaisseur d'un obstacle en une image peut le traverser. Limiter la vitesse ou découper le déplacement en plusieurs petits pas.

* 🎬 [Collisions in Pygame - Beginner Tutorial](https://www.youtube.com/watch?v=BHr9jxKithk) – *Coding With Russ*

## Organiser son code

* **Un objet du jeu = une classe**, avec ses données (position, vitesse, vie) et ses méthodes (`mettre_a_jour`, `afficher`).
* **Une classe `Jeu`** qui possède la fenêtre, l'horloge, les objets et la boucle principale. Cela évite les variables globales.
* **Pas de « nombres magiques »** : définir en tête de fichier des constantes nommées (`LARGEUR`, `VITESSE_BALLE`, `COULEUR_FOND`…).
* **Machine à états** : une variable `etat` (`"menu"`, `"jeu"`, `"pause"`, `"perdu"`) et un comportement différent dans chaque méthode selon sa valeur.
* **Un fichier par grande responsabilité** dès que le projet grossit (`joueur.py`, `ennemis.py`, `niveaux.py`…), importés dans un `main.py`.
* Avancer **par petites étapes jouables** : fenêtre → un objet qui bouge → clavier → un obstacle → collisions → score → écran de fin. Tester après chaque étape.


## Le « game feel » : rendre le jeu agréable

Un jeu qui fonctionne n'est pas forcément un jeu agréable. Beaucoup de petits détails, peu coûteux à programmer, changent complètement le ressenti :

* secousse de l'écran à l'impact ;
* particules, traînées, étincelles ;
* petites animations (grossissement d'un objet qui disparaît, clignotement lors d'un dégât) ;
* sons pour chaque action (`pygame.mixer`) ;
* légers temps d'arrêt au moment d'un choc ;
* réponse immédiate aux touches.

* 🎬 [Juice it or lose it](https://www.youtube.com/watch?v=Fy0aCDmgnxg) – *Martin Jonasson & Petri Purho* : on part d'un casse-briques minimal et on l'améliore pas à pas.
* 🎬 [Secrets of Game Feel and Juice](https://www.youtube.com/watch?v=216_5nu4aVQ) – *Game Maker's Toolkit*
* 🎬 [The art of screenshake](https://www.youtube.com/watch?v=AJdEqssNZ-U) – *Jan Willem Nijman (Vlambeer)*

## Bonnes habitudes de développement

* **Utiliser un gestionnaire de versions** (`git`) pour pouvoir revenir en arrière.
* **Afficher les informations de débogage** à l'écran (FPS avec `horloge.get_fps()`, positions, état) plutôt que de multiplier les `print`.
* **Dessiner les rectangles de collision** (`pygame.draw.rect(ecran, (255, 0, 0), rect, 1)`) pour comprendre un bug de collision.
* **Séparer les données du code** : décrire un niveau dans un tableau ou un fichier texte plutôt qu'en dur dans les instructions.
* **Ne pas viser trop grand** : finir un petit jeu complet est plus formateur que d'en commencer un très ambitieux.
* **Faire tester le jeu à quelqu'un d'autre** : on ne voit plus les défauts de son propre jeu.
