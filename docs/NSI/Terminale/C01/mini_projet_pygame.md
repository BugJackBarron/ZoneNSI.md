# Mini-Projet collaboratif : Space Invaders

*Très largement inspiré d'une production du groupe de production de ressources SNT/NSI de l'académie de Rennes.*

## Présentation

Vous disposez d'un code de départ pour le mythique jeu Space Invaders, utilisant la bibliotèque `pyganme-ce` (Pygame Community Edition). Le jeu est fonctionnel, mais on vous demande d'améliorer le jeu. Votre temps étant limité, votre équipe doit donc se répartir les taches afin de développer de nouvelles fonctionnalités.

## Le code de départ

Les différents fichiers à votre disposition sont :

* [alien.py](Mini_projet_Space_Invaders/alien.py){target="_blank"} : contient la classe `Alien`, représentant les ennemis.
* [missile.py](Mini_projet_Space_Invaders/missile.py){target="_blank"} : contient la classe `Missile`, représentant les missiles du joueur/ de la joueuse.
* [vaisseau.py](Mini_projet_Space_Invaders/vaisseau.py){target="_blank"} : contient la classe `Vaisseau`, représentant le vaisseau du joueur/ de la joueuse.
* [constantes.py](Mini_projet_Space_Invaders/constantes.py){target="_blank"} : contient différentes constantes nécessaires pour le jeu, et partagées dans tous les fichiers.
* [space_invaders.py](Mini_projet_Space_Invaders/space_invaders.py) : fichier principal du jeu, regroupant la boucle de jeu ainsi que les évènements claviers.

## Les objectifs

Par équipes de 3, vous devrez, en 4 séances de 1h :

* comprendre et tester le code existant ;
* concevoir et implémenter **deux fonctionnalités supplémentaires** ;
* préparer une présentation orale avec démonstration de vos nouvelles fonctionnalités.
* présenter vos solutions et répondre aux questions des autres équipes.


La grille de notation sera la suivante :

| Critère | Points |
| :--- | ---: |
| Code fonctionnel | 6 pts |
| Code lisible et récupérable par les autres groupes | 6 pts |
| Présentation orale | 4 pts |
| Implication dans le groupe (partie personnelle) | 4 pts |


## Les fonctionnalités à développer (2 par groupe)

| Groupe | Fonctionnalité | Objectifs techniques |
| :---: | :--- | :--- |
| G1 | Barre de vie du joueur | Ajouter un système de vie, perte de vie si touché par un alien ou si l'alien touche le bas. Affichage graphique des vies restantes |
| G1 | Tirs des Aliens | Implémenter des tirs des aliens avec collision sur le joueur |
| G2 | Niveaux progressifs | Augmenter la vitesse ou le nombre d'ennemis à chaque vague |
| G2 | Système de score | Calcul du score et affichage du score en temps réel. Bonus : Sauvegarde du meilleur score |
| G3 | Mode 2 joueurs | Ajouter un deuxième joueur avec un second jeu de touches |
| G3 | Aliens animés | Changer la couleur, l'apparence ou créer une animation visuelle des ennemis |

## Présentation attendue

* Expliquer la fonctionnalité et sa finalité
* Montrer le fonctionnement dans le jeu
* Afficher et commenter les extraits de code modifiés (bonus si le code de départ n'est pas modifié)
* Répondre aux questions du professeur ou des autres groupes.



