# Les graphes

!!! info "Problème des sept ponts de Königsberg"

	La ville de Königsberg (aujourd'hui Kaliningrad) est construite autour de deux îles situées sur le Pregel et reliées entre elles par un pont. Six autres ponts relient les rives de la rivière à l'une ou l'autre des deux îles, comme représentés sur le plan ci-dessus. 
	
	![Koenigsberg.png](Koenigsberg.png){: style="width:50%; margin:auto;display:block;background-color: #546d78;"}
	
	Le problème consiste à déterminer s'il existe ou non une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de passer une et une seule fois par chaque pont, et de revenir à son point de départ, étant entendu qu'on ne peut traverser le Pregel qu'en passant sur les ponts. 
	
	Le mathématicien [Leonhard Euler](https://fr.wikipedia.org/wiki/Leonhard_Euler){: target="_blank"} donna la solution de ce problème en utilisant les prémices de ce qu'on appelera {==**Théorie des graphes**==}
	


## Définitions et vocabulaire

``` dot 
digraph G {
    rankdir=LR
    Earth [peripheries=2]
    Mars
    Earth -> Mars
}
```






## Modélisation

