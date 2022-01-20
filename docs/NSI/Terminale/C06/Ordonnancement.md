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

Imaginons que le processeur ait à exécuter 4 processus, dont les temps d'exécutions sont différents :

* le processus `A` a besoin de 5 cycles d'horloge ;
* le processus `B` a besoin de 3 cycles d'horloge ;
* le processus `C` a besoin de 2 cycles d'horloge ;
* le processus `D` a besoin de 4 cycles d'horloge ;

![P3_img1.png](P3_img1.png){: style="width:20%; margin:auto;display:block;background-color: #546d78;"}

Ces 4 processus ont été demandés dans l'ordre `A, B, C, D` au processeur, qui était occupé jusque là.

#### Système non-préemptifs : PAPS

Si le système d'exploitation n'est pas préemptif, on pourrait penser au principe d'une file de type &laquo; Premier Arrivé, Premier Servi &raquo; (*FIFO*).

![P3_img2.png](P3_img2.png){: style="width:60%; margin:auto;display:block;background-color: #546d78;"}

Avec ce système, chaque processus sera exécuté du début à la fin, sans interruptions. Il faudra 14 cycles d'horloge pour terminer les 4 processus, 


### Exemple en Python : les Threads

## Les interblocages

### 
