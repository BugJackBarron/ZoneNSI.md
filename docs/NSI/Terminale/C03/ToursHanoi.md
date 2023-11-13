# TP : Tour de Hanoï

## Présentation du jeu 

**Les tours de Hanoï** est un jeu de réflexion imaginé par le mathématicien français [Édouard Lucas](https://fr.wikipedia.org/wiki/Édouard_Lucas){:target = "_blank"}.

Il consiste à déplacer des disques de différents diamètres d'une « tour de départ » à une « tour d'arrivée » en passant par une « tour intermédiaire », et ce en un minimum de coups, en respectant les deux règles suivantes :

* on ne peut déplacer qu'un disque à la fois ;
* on ne peut pas placer un disque sur un disque de diamètre inférieur.

![Tour_Hanoi_1.png](Tour_Hanoi_1.png){: style="width:50%; margin:auto;display:block;background-color: #d2dce0;"}

On souhaite écrire un programme python non-récursif qui utilise la classe `Pile` définie dans le cours précédent (avec les listes chainées), et qui devra :

1. Permettre de saisir un nombre `n` de disques.
2. Afficher à l'écran les différentes étapes pour résoudre le problème avec `n` disques, en précisant à chaque fois le nombre d'étapes nécessaires.

## Algorithme de résolution non-récursif

Si on observe de près le jeu pour un nombre de disques supérieur à 1, on s'aperçoit qu'il n'y a que 1 ou 2 déplacements possibles :

* le petit disque peut **toujours** se déplacer sur les deux autres tours.
* si un disque différent du plus petit peut-être déplacé, il n'y a qu'une seule possibilité, c'est-à-dire sur la tour **où n'est pas le petit disque**.

Un algorithme itératif est donc le suivant :

```
Tant qu'il reste un disque sur la tour de départ ou sur la tour intermédiaire :
    Déplacer le petit disque d'une tour dans le sens D->F->I->D
    Si on peut déplacer un disque autre que le plus petit, alors le déplacer
```

!!! example "Exemple avec 3 disques"

    === "Etape 0"

        ![Etape_0.png](Etape_0.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        Les trois disques sont sur la tour de départ.

    === "Etape 1"

        ![Etape_1.png](Etape_1.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le petit disque sur la tour finale (`D->F`).

    === "Etape 2"

        ![Etape_2.png](Etape_2.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le disque moyen sur la tour intermédiaire.

    === "Etape 3"

        ![Etape_3.png](Etape_3.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le petit disque sur la tour intermédiaire (`F->I`).

    === "Etape 4"

        ![Etape_4.png](Etape_4.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le grand disque sur la tour finale.

    === "Etape 5"

        ![Etape_5.png](Etape_5.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le petit disque sur la tour de départ (`I->D`).

    === "Etape 6"

        ![Etape_6.png](Etape_6.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le disque moyen sur la tour finale.

    === "Etape 7"

        ![Etape_7.png](Etape_7.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

        On déplace le petit disque sur la tour finale (`D->F`). L'algorithme s'arrête.