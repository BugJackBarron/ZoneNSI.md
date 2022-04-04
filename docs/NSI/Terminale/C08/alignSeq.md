# Alignement de séquences


## Présentation du sujet 


On dispose de deux chaînes de caractères : $A$, qui vaut `INFORMATIQUE`, et $B$, qui vaut `NUMERIQUE`. On aimerait mettre ces deux chaînes de caractères en correspondance de la manière suivante :

* On place les 2 chaînes l'une en desous de l'autre;
* Si les derniers caractères des deux chaînes coïncident, alors on passe aux caractères suivants;
* Sinon, on va ajouter un trou dans une des deux chaînes, symbolisé par un - et on passe aux caractères suivant.

Voici un exemple d'alignement optimal :

![exempleAlignement.gif](exempleAlignement.gif){: style="width:40%; margin:auto;display:block;background-color: #546d78;"}

Dans cette situation on a besoin de 9 tirets, pas moins.

L'objectif est d'aligner le maximum de lettres (donc de mettre le moins de `-` possible). Ce n'est pas un problème simple, surtout quand les chaînes sont longues, comme pour les séquences d'ADN par exemple :

![sequenceADN.png](sequenceADN.png){: style="width:80%; margin:auto;display:block;background-color: #546d78;"}

## Résolution par une méthode récursive 

Le principe est présenté dans la vidéo suivante :

<iframe src="//video.toutatice.fr/video/28583-alignement-de-sequences-methode-recursive-et-programmation-dynamique/?is_iframe=true" size="240" width="1280" height="720" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>


Pour les mots `GRAS` et `GERS`, l'arbre  obtenu est le suivant :

![ArbreGrasGers.png](ArbreGrasGers.png){: style="width:80%; margin:auto;display:block;background-color: #546d78;"}

Après application d'une méthode dynamique ({==**Top Down**==}) (c'est-à-dire récursive avec mémoïsation), on obtient le graphe suivant :

![GrapheGrasGers.png](GrapheGrasGers.png){: style="width:80%; margin:auto;display:block;background-color: #546d78;"}

## Résolution par une méthode itérative

### Activité débranchée

Considérons les deux chaînes de caractères `GENOME` et `ENORME`. Afin de chercher le nombre minimal d'insertion à effectuer, nous allons compléter le tableau suivant, avec la convention suivante : à l'intersection de la colonne `N` et de la première ligne `E` se trouve le nombre minimal d'insertion nécessaire pour aligner les chaînes `GEN` et `E`, c'est-à-dire 2 tirets. Par convention la première ligne et la première colonne correspondent à une chaîne vide.



!!! question
	=== "Enoncé"
	
		En quoi la méthode ci-dessus est-elle une méthode itérative ({==**Bottom Up**==}) ?
		
	=== "Réponse"
		
		A venir !
### Application en Python

L'activité est disponible sous la forme d'un [notebook capytale](https://capytale2.ac-paris.fr/web/c/ade1-491791){: target = "_blank"}