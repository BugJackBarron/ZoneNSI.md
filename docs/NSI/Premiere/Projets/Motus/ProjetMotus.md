# Projet : Motus

!!! warning "Principes du projet"

	* **LA NOTE MAXIMALE DE CE PROJET EST DE 18 SANS LA PARTIE FACULTATIVE !**
	* Vous travaillerez par binômes sur ce projet (ou exceptionnellement par trinômes).
	* Vous rendrez le code complet + votre dossier personnel pour le 11 décembre 2026.
	* Vous aurez un temps en classe pour réaliser le projet, mais ce temps ne sera pas suffisant ! Vous devrez vous coordonner pour arriver à vos fins !

!!! tip "Fiche de suivi enseignant"

    [:material-file-pdf-box: Télécharger la fiche de suivi du projet (PDF)](Fiche_Suivi_Motus.pdf){: download }

## Description du projet

L'objectif est de simuler une partie du jeu télévisé **Motus**.

!!! info "Principe du jeu"

	1. Un mot français de 6 lettres est tiré aléatoirement dans une liste. **Seule sa première lettre est révélée au joueur / à la joueuse.**
	2. Le joueur / la joueuse propose un mot de 6 lettres commençant par la même lettre. Cette proposition doit être un mot de la liste (les mots inventés sont refusés, et ne comptent pas comme un essai).
	3. Le programme compare la proposition au mot à chercher, et affiche pour chaque lettre :
		* la lettre en **MAJUSCULE** si elle est **bien placée** ;
		* la lettre en **minuscule** si elle est **présente dans le mot, mais mal placée** ;
		* un **point** `.` si elle n'est **pas dans le mot**.
	4. On reprend à l'étape 2 tant que :
		* le mot n'a pas été trouvé ;
		* **et** le joueur / la joueuse n'a pas utilisé ses 6 essais.
	5. Un score est attribué à la manche : plus le mot est trouvé rapidement, plus il est élevé. Le joueur / la joueuse peut ensuite rejouer ou arrêter.

!!! example "Exemple de manche"

	Si le mot à trouver est `BANANE` :

	```
	Le mot commence par B
	Mot en 6 lettres commençant par B : bravos
	B . a . . .
	B . . . . .
	B . . . . .
	B . . . . .
	B . . . . .
	Mot en 6 lettres commençant par B : bananes
	Mauvaise longueur (6 lettres attendues)
	Mot en 6 lettres commençant par B : banane
	B . a . . .
	B A N A N E
	B . . . . .
	B . . . . .
	B . . . . .
	Bravo !
	```

!!! tip "Attention aux lettres en double !"

	Une lettre du mot à trouver ne peut "servir" qu'une seule fois, et **une lettre bien placée est prioritaire** sur une lettre mal placée. Par exemple, avec le mot `BALLES`, la proposition `ALLONS` donne `alL..S` : le deuxième `L` est bien placé, il "consomme" l'un des deux `L` du mot. Il en reste donc un seul pour le premier `L` de la proposition, qui est mal placé.

	Avec la proposition `LLLLLL`, on obtient `..LL..` : il n'y a que deux `L` dans `BALLES`, et ils sont tous deux trouvés.

## Les fichiers nécessaires

!!! tip "Fichier de mots"

	Pour mener à bien le projet, vous aurez besoin du fichier
	{==**[liste_francais_modifiee.txt](liste_francais_modifiee.txt)**==}, qui contient des mots français en majuscules, sans accents. Vous le copierez dans votre dossier de travail, à côté du fichier python utilisé.

!!! tip "Base de code Python"

	Je vous donne [ici](./motus_eleve.py) le code qui doit être votre base de travail.

!!! warning "Fonction `charge_mots(adresse_fichier, longueur_mot)`"

	Cette fonction **ne doit pas être modifiée !**

	Elle prend en argument l'adresse **relative** ou **absolue** d'un fichier texte, ainsi qu'une longueur de mot, et renvoie la **liste** des mots de ce fichier qui ont cette longueur (en majuscules).

	Les constantes `LONGUEUR_MOT` (6) et `NB_ESSAIS_MAX` (6) sont définies en début de fichier. Vous devez les utiliser dans votre code plutôt que de réécrire les valeurs `6` « en dur ».

## Plan de travail

1. Vous commencerez par compléter la fonction `choisir_mot(mots)`, qui renvoie un mot choisi au hasard dans la liste `mots`.

2. Vous compléterez ensuite la fonction `mot_valide(proposition, premiere_lettre, longueur, mots)`, qui renvoie un booléen indiquant si la proposition est recevable (bonne longueur, bonne première lettre, mot présent dans la liste). Des **tests unitaires** sont donnés à titre d'exemple. Vous pouvez éventuellement rajouter les vôtres.

3. Vous compléterez la fonction `demande_proposition(premiere_lettre, longueur, mots)` et la rendrez *dumbproof* : cette fonction doit continuer à redemander un mot tant que la proposition n'est pas recevable, **en expliquant à chaque fois pourquoi elle est refusée**. Le mot saisi peut l'être en minuscules, mais est renvoyé en majuscules. Vous réutiliserez la fonction précédente.

4. Vous compléterez la fonction `teste_mot(proposition, cible)`, qui compare la proposition au mot à trouver et renvoie la chaine de caractères décrite plus haut (majuscules, minuscules et points). C'est **la fonction la plus délicate du projet** : pensez aux lettres en double, et au fait que les lettres bien placées sont prioritaires. Des **tests unitaires** sont donnés à titre d'exemple.

	!!! tip "Piste"

		Il est conseillé de parcourir le mot **en deux temps** : une première fois pour repérer les lettres bien placées (et noter les lettres de la cible qui n'ont pas été trouvées), puis une seconde fois pour les lettres mal placées.

5. Vous compléterez la fonction `affiche_essais(resultats, premiere_lettre, nb_essais_max, longueur)`, qui affiche la grille de jeu : une ligne par essai déjà effectué, puis une ligne par essai restant (la première lettre suivie de points). Les caractères sont séparés par des espaces.

6. Vous compléterez la fonction `calcule_score(nb_essais, victoire)`, qui renvoie le score d'une manche : `0` si le mot n'a pas été trouvé, sinon `100` points par essai non utilisé, plus `100`.

7. À partir de toutes les fonctions précédentes, vous finaliserez le jeu en complétant la fonction `une_manche(mots)`, qui renvoie le score de la manche. **Le mot à trouver ne doit jamais être affiché avant la fin de la manche !**

8. Une fois le jeu complété, vous devrez en outre compléter un **dossier personnel** d'une ou deux pages présentant :

	* ce que vous avez réalisé individuellement dans ce projet ;
	* les difficultés rencontrées et/ou les problèmes que vous n'avez pas pu résoudre ;
	* les aides qui vous ont été apportées.

9. Vous pourrez enfin apporter des modifications et/ou améliorations au code, par exemple en :

	* ajoutant un niveau de difficulté (longueur des mots, nombre d'essais) ;
	* donnant en indice, à chaque essai, les lettres déjà trouvées aux bonnes places ;
	* affichant un récapitulatif des lettres déjà utilisées ;
	* etc...

## Question facultative : sauvegarde du High Score

!!! question "Les meilleurs scores"

	Le score d'une manche est ajouté au **score total** de la session de jeu (voir la fonction `main`). Lorsque le joueur / la joueuse décide d'arrêter de jouer, on souhaite lui proposer de sauvegarder son score.

	1. À la fin de la fonction `main`, **proposez** au joueur / à la joueuse de sauvegarder son score total. S'il ou elle accepte, demandez-lui un nom (non vide), puis enregistrez-le grâce à la fonction `sauve_score(nom, score)`.
	2. Affichez ensuite les 10 meilleurs scores enregistrés, grâce à la fonction `get_score()`, qui renvoie une chaine de caractères prête à être affichée avec `print`.
	3. Que se passe-t-il si le nom saisi contient la chaine ` / ` ? Comment pourriez-vous vous en prémunir ?

	!!! warning "Fonctions `get_score` et `sauve_score`"

		Ces fonctions **ne sont pas à modifier**, ni même à comprendre... Elles gèrent un fichier `HighScore.txt`, situé à côté du fichier python, qui est **créé automatiquement** s'il n'existe pas.

## Grille de notation

| intitulé | barème | Détails |
| :---: | :---: | :--- |
| fonction `choisir_mot` | 1 pt | passage de tous les tests unitaires |
| fonction `mot_valide` | 2 pts | passage de tous les tests unitaires |
| fonction `demande_proposition` | 2 pts | *dumbproof*, avec messages d'erreur explicites |
| fonction `teste_mot` | 4 pts | passage de tous les tests unitaires (dont les lettres en double) |
| fonction `affiche_essais` | 2 pts | Affichage correct |
| fonction `calcule_score` | 1 pt | passage de tous les tests unitaires |
| fonction `une_manche` | 3 pts | On attend un jeu a minima fonctionnel |
| Noms des variables clairs | 1 pt | On proscrira les noms de variable d'un seul caractère, sauf compteurs précis |
| Code commenté et clair | 1 pt | Des explications minimales doivent être écrites pour expliquer votre code |
| Améliorations, qualité du code, etc... | 1 pt | |
| Partie facultative (High Score) | 2 pts | Avec un affichage correct et une bonne saisie |
| **Total** | **20 pts** | **18 pts sans la partie facultative** |
