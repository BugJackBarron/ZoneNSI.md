# Ordonnancement des Processus et Interblocage

## L'ordonnancement

### Une vision faussée ?

Nous rappelons qu’un {==**exécutable**==} est un fichier (par exemple stocké sur le disque dur) contenant une suite d’instructions en langage machine. C’est donc une suite d’octets  que le processeur est capable de décoder et exécuter. Concrètement,  lorsque l’on exécute un programme (par exemple en cliquant sur l’icône du fichier exécutable ou en renseignant son chemin dans un terminal), le système d’exploitation effectue les actions suivantes :

1. le fichier contenant le programme (l’exécutable) est copié dans la mémoire RAM, à une certaine adresse `a` ;
2. le système d’exploitation écrit la valeur `a` dans le registre `IP` (*Instruction Pointer*).
 
 Au prochain cycle d'horloge du processeur, ce dernier va alors lire l’instruction se trouvant à l’adresse `a` et l’exécuter. Une fois cela fait, il exécutera ensuite la seconde instruction et ainsi de suite. On rappelle que l’exécution d’une instruction se décompose elle-même en plusieurs sous-étapes effectuées au sein du processeur : 
	
* le chargement (récupérer l'instruction en mémoire) ;
* le décodage (déterminer dans la suite d’octets chargés quelle instruction ils encodent) ;
* l’exécution proprement dite.

!!! warning 
	Même si elle semble correcte, la description que nous avons faite de l’exécution d’un programme est incomplète. En effet, si rien de plus n’est fait, alors **la seule chose que l’on peut attendre, c’est que le programme en question s'exécute jusqu’à sa dernière instruction, puis rende la main au système d'exploitation**. Impossible alors de l’interrompre ! Impossible aussi de pouvoir exécuter deux programmes en même temps.


### Les interruptions systèmes
 
Pour pallier ce problème, les systèmes d’exploitation utilisent une fonctionnalité importante des processeurs modernes : la notion d ‘{==**interruption**==}.

!!! asbtract "Interruption"
	Une interruption est un signal envoyé au processeur lorsqu'un événement se produit. Il existe plusieurs types d’interruptions. Certaines sont générées par le matériel (par exemple, un disque dur signale qu’il a fini d'écrire des octets, une carte réseau signale que des paquets de données arrivent, etc.), d'autres par du logiciel.
	
	Lorsque le processeur reçoit une interruption, il interrompt son exécution à la fin de l'instruction courante et exécute un programme se trouvant à une adresse prédéfinie. Ce programme reçoit en argument une copie des valeurs courante des registres, ainsi qu’un code numérique lui permettant de savoir à quel type d’interruption il fait face. Ce programme spécial s'appelle le	{==**gestionnaire d'interruption**==}. Il est installé à une certaine adresse mémoire par le système d'exploitation, très tôt après le démarrage de la machine.


!!! abstract "Interruption d'horloge"
	Parmi les interruptions matérielles, on retrouve les {==**interruptions d’horloge**==}. Le processeur génère de lui-même une interruption matérielle à intervalles de temps fixe. Historiquement, sur processeur *Intel*, cette interruption était levée toutes les 55 ms (environ 18 fois par seconde). Le gestionnaire d'interruption était donc appelé au moins toutes les 55 ms. De nos jours, les processeurs disposent d’horloges de haute précision capables d'émettre des interruptions avec une fréquence de 10 Mhz, donc toutes les 100 ns. Ces interruptions d’horloges, alliées au gestionnaire d'interruption, sont les pièces essentielles permettant d'**exécuter des programmes de façon concurrente.**


### Principe de l'ordonnanceur

Dans un système d'exploitation moderne, plusieurs processus peuvent être présents en mémoire centrale en attente d’exécution. Si plusieurs processus sont prêts, le système d’exploitation doit gérer l’allocation du processeur aux différents processus à exécuter. C’est l’{==**ordonnanceur**==} qui s’acquitte de cette tâche.


!!! abstract  "Notion d’ordonnancement"
	Le système d’exploitation d’un ordinateur peut être vu comme un ensemble de processus dont l’exécution est gérée par un processus particulier : l’{==**ordonnanceur**==} (*scheduler* en anglais). Il s'agit en gros du &laquo; chef d'orchestre &raquo; du système d'exploitation.

Les objectifs d’un ordonnanceur sont, entre autres :

1. s’assurer que chaque processus en attente d’exécution reçoive sa part de temps processeur ;
2. minimiser le temps de réponse ;
3. utiliser le processeur à 100% (ce serait gâcher de la ressource);
4. utiliser d’une manière équilibrée les ressources ;
5. prendre en compte les priorités ;
6. être prédictible (et ce n'est pas une mince affaire...).

Pour répondre à ces objectifs parfois contradictoires, un ordonnanceur fait face à deux problèmes principaux :	

1. Comment choisir quel processus exécuter ?
2. Combien de temps de processeur allouer au processus choisi ?

### Différentes méthodes d'ordonnancement

Imaginons que le processeur ait à exécuter 4 processus, dont les temps d'exécutions sont différents, et qui se sont présentés à différents instants au processeur :

* le processus `A` a besoin de 5 cycles d'horloge, et est arrivé au *tick* 0 ;
* le processus `B` a besoin de 3 cycles d'horloge, et est arrivé au *tick* 1 ;
* le processus `C` a besoin de 2 cycles d'horloge, et est arrivé au *tick* 3 ;
* le processus `D` a besoin de 4 cycles d'horloge, et est arrivé au *tick* 5 ;

![P3_img1.png](P3_img1.png){: style="width:20%; margin:auto;display:block;background-color: #546d78;"}

Le processeur ne pouvant traiter qu'une information à la fois, au vu des chevauchements, il faudra ordonner les différents processus afin qu'ils soient tous exécutés.

#### Système non-préemptifs : PAPS

Si le système d'exploitation **n'est pas préemptif**, on pourrait penser au principe d'une file de type &laquo; Premier Arrivé, Premier Servi &raquo; (*FIFO*).

![P3_img2.png](P3_img2.png){: style="width:60%; margin:auto;display:block;background-color: #546d78;"}

Avec ce système, chaque processus sera exécuté du début à la fin, sans interruptions. Il faudra 14 cycles d'horloge pour terminer les 4 processus. C'est le principe de la file d'attente pour les imprimantes : peu importe le nombre de pages à imprimer, les documents seront imprimés en entier et dans leur ordre d'arrivée.

Regardons le temps de séjour nécessaire à l'exécution de chaque processus, qui correpond à la différence entre le temps de terminanison du processus et le temps d'entrée dans le processeur :

* `A` est terminé au tick 5, et est entré au tick 0 : $t_A = 5-0 = 5$
* `B` est terminé au tick 8, et est entré au tick 1 : $t_B = 8-1 = 7$
* `C` est terminé au tick 10, et est entré au tick 3 : $t_C = 10-3 = 7$
* `D` est terminé au tick 14, et est entré au tick 5 : $t_D = 14-5 = 9$

Le temps de séjour moyen avec cette méthode est donc $\dfrac{5+7+7+9}{4} = \dfrac{28}{4} = 7$.

Le temps d'attente, lui, est le temps de séjour auquel on retranche le temps d'exécution :

* `A` a pour temps d'attente 5 et pour temps d'exécution 5 : $t'_A = 5-5 = 0$
* `B` a pour temps d'attente 7 et pour temps d'exécution 3 : $t'_B = 7-3 = 4$
* `C` a pour temps d'attente 7 et pour temps d'exécution 2 : $t'_C = 7-2 = 5$
* `D` a pour temps d'attente 9 et pour temps d'exécution 4 : $t'_B = 9-4 = 5$

Le temps d'attente moyen avec cette méthode est donc $\dfrac{0+4+5+5}{4} = \dfrac{14}{4} = 3,5$.


#### Système non-préemptif : Short Job First (SJF)

Une autre possibilité est de prioriser dans les processus en attente celui qui sera le plus rapide à terminer.

![P3_img3.png](P3_img3.png){: style="width:60%; margin:auto;display:block;background-color: #546d78;"}

Ainsi :

* au tick 0, on exécute le processus `A`


* `A` est terminé au tick 5, et est entré au tick 0 : $t_A = 5-0 = 5$
* `B` est terminé au tick 10, et est entré au tick 1 : $t_B = 10-1 = 9$
* `C` est terminé au tick 7, et est entré au tick 3 : $t_C = 7-3 = 4$
* `D` est terminé au tick 14, et est entré au tick 5 : $t_D = 14-5 = 9$

Le temps de séjour moyen avec cette méthode est donc $\dfrac{5+9+4+9}{4} = \dfrac{27}{4} = 6,75$.

* `A` a pour temps d'attente 5 et pour temps d'exécution 5 : $t'_A = 5-5 = 0$
* `B` a pour temps d'attente 9 et pour temps d'exécution 3 : $t'_B = 9-3 = 6$
* `C` a pour temps d'attente 4 et pour temps d'exécution 2 : $t'_C = 4-2 = 2$
* `D` a pour temps d'attente 9 et pour temps d'exécution 4 : $t'_B = 9-4 = 5$

Le temps d'attente moyen avec cette méthode est donc $\dfrac{0+6+2+5}{4} = \dfrac{13}{4} = 3,25$.


### Préemptif Shortest Remaining Time (SRT)

* `A` est terminé au tick 10, et est entré au tick 0 : $t_A = 10-0 = 10$
* `B` est terminé au tick 4, et est entré au tick 1 : $t_B = 4-1 = 3$
* `C` est terminé au tick 6, et est entré au tick 3 : $t_C = 6-3 = 3$
* `D` est terminé au tick 14, et est entré au tick 5 : $t_D = 14-5 = 9$

Le temps de séjour moyen avec cette méthode est donc $\dfrac{10+3+3+9}{4} = \dfrac{25}{4} = 6,25$.

* `A` a pour temps d'attente 10 et pour temps d'exécution 5 : $t'_A = 10-5 = 5$
* `B` a pour temps d'attente 3 et pour temps d'exécution 3 : $t'_B = 3-3 = 0$
* `C` a pour temps d'attente 3 et pour temps d'exécution 2 : $t'_C = 3-2 = 1$
* `D` a pour temps d'attente 9 et pour temps d'exécution 4 : $t'_B = 9-4 = 5$

Le temps d'attente moyen avec cette méthode est donc $\dfrac{5+0+1+5}{4} = \dfrac{11}{4} = 2,75$.

### Préemptif Round Robin (RR)

* `A` est terminé au tick 12, et est entré au tick 0 : $t_A = 12-0 = 10$
* `B` est terminé au tick 7, et est entré au tick 1 : $t_B = 7-1 = 6$
* `C` est terminé au tick 8, et est entré au tick 3 : $t_C = 8-3 = 5$
* `D` est terminé au tick 14, et est entré au tick 5 : $t_D = 14-5 = 9$

Le temps de séjour moyen avec cette méthode est donc $\dfrac{10+3+3+9}{4} = \dfrac{30}{4} = 7,5$.

* `A` a pour temps d'attente 10 et pour temps d'exécution 5 : $t'_A = 10-5 = 5$
* `B` a pour temps d'attente 6 et pour temps d'exécution 3 : $t'_B = 6-3 = 3$
* `C` a pour temps d'attente 5 et pour temps d'exécution 2 : $t'_C = 5-2 = 3$
* `D` a pour temps d'attente 9 et pour temps d'exécution 4 : $t'_B = 9-4 = 5$

Le temps d'attente moyen avec cette méthode est donc $\dfrac{0+4+5+5}{4} = \dfrac{16}{4} = 4$.

### Exemple en Python : les Threads

## Les interblocages

### 
