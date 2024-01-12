# Projet Jeu d'aventure textuel

## Principe du projet 

Le principe est de réaliser un jeu d'aventure textuel, basé sur le principe des « Livres dont vous êtes le héro » : dans **une unique page html**, on progressera à travers une aventure où le/la joueur×euse devra effectuer divers choix qui influenceront la suite de l'aventure. 

La page devra contenir une zone dans laquelle le texte évoluera en fonction de choix effectués par le/la joueur×euse. Les actions seront représentées sous la forme de boutons. Par ailleurs, selon les actions, certaines caractéristiques chiffrées du personnage principal de l'histoire (Points de vie, niveau, etc.) varieront, et ces caractéristiques seront affichées à l'écran.

## Un exemple de début de jeu : Dungeon of death

Vous trouverez [ici](Dungeon.html){:target="_blank"} un début d'exemple de ce que peut donner le projet. Vous avez ainsi accès non seulement aux codes HTML et CSS, mais aussi à un exemple de code Javascript.

!!! warning "Attention !"
    Vous n'êtes pas tenus d'avoir une illustration graphique de votre histoire ! Cependant, si vous le souhaitez je vous déconseille d'utiliser la même technique que celle que j'ai utilisée, car à la fois trop complexe et peu adaptée pour certaines histoires.

    Une idée plus intéressante serait de charger une image différente à chaque étape de votre histoire.

## Quelques tutoriels utiles

### Utiliser des boutons pour modifier des variables en Javascript

<iframe src="//video.toutatice.fr/video_priv/42307/5ef957d286d04577914706139960bfbe9862f06a6baae1a313bf622579dc0b44/?is_iframe=true&size=720" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

Les fichiers d'exemples sont visibles sur Capytale par le code [f7fa-2705601](https://capytale2.ac-paris.fr/web/c/f7fa-2705601){:target="_blank"}

### Création et modification d'objets ayant plusieurs caractéristiques en Javascript

#### Première partie : création d'un objet, utilisation d'un champ input

<iframe src="//video.toutatice.fr/video_priv/42308/bea3e767f39f58a446429787be70920d35ceaf09651e30b4ab1d1052a4b76a26/?is_iframe=true&size=720" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

#### Deuxième partie : utiliser l'aléatoire

<iframe src="//video.toutatice.fr/video_priv/42309/ea5b1de2f726d0372250ca0ccf012cf8d4098429ff17dd8d8e72fcfcba32861f/?is_iframe=true&size=720" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

Les fichiers d'exemples pour les deux parties sont visibles sur Capytale par le code [4764-2707919](https://capytale2.ac-paris.fr/web/c/4764-2707919){:target="_blank"}


### Utilisation d'objets partageant des descripteurs communs

#### Partie 1 : les bases

<iframe src="//video.toutatice.fr/video_priv/42310/f47e0fa6373b3d2ba3bcace6a14cecfd9d8ca5948de8fa6be93b18c65c8612e8/?is_iframe=true&size=720" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

Les fichiers d'exemples sont visibles sur Capytale par le code [8702-2709067](https://capytale2.ac-paris.fr/web/c/8702-2709067){: target="_blank"}

#### Partie 2 : utilisation avancée (facultative)

<iframe src="//video.toutatice.fr/video_priv/42311/1056fed77a7464c2f0bdc500d8bb61744766f29003447d390df0b041259724ea/?is_iframe=true&size=720" width="640" height="360" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>

Les fichiers d'exemples sont visibles sur Capytale par le code [331d-2710811](https://capytale2.ac-paris.fr/web/c/331d-2710811){: target="_blank"}


## Grille de notation


| intitulé | barême | Détails |
| :---: | :---: | :--- |
| Jeu fonctionnel | 5 pts | L'histoire peut être suivie et se termine (en bien ou en mal) |
| Code HTML | 3 pts | Code HTML correct ne renvoyant pas d'erreurs sur [W3C Validator](https://validator.w3.org/#validate_by_upload){: target="_blank"}|
| Code CSS | 2 pts | Code correct ne renvoyant pas d'erreurs sur [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_upload){: target = "_blank"} |
| Code Javascript | 5 pts | Le code doit être lisible et commenté. |
| Passage d'étapes | 2 pts | Passage d'étapes sans erreurs (bonne utilisation de boutons) |
| Caractéristiques évolutives | 3 pts | Des caractéristiques (variables numériques) évoluent en fonction des actions et influencent l'histoire |
