# Stockage et transferts de données

!!! abstract "Science informatique"

    La science informatique est définie comme la **«science du traitement automatisé de l'information»**.

Avant de traiter des informations, encore faut-il les organiser et les stocker de manière efficace. Nous verrons dans ce TP comment sont structurées et stockées des données de tous types.

## Unités d'informations

### La notation binaire pour les entiers

Historiquement, on trouve des utilisations de symboles binaires depuis les antiquités chinoises et indiennes: on trouve des utilisations dans les hexagrammes du *Yi Jing* en Chine (-750), et le mathématicien indien Pingala présente une table représentant les nombres 0 à 7 en binaire (troisième ou deuxième siècle av J.C.). Mais c'est à Leibniz au XVIII^e, qui montre la compatibilité du système binaire avec les quatre opérations, et surtout au mathématicien George Boole, qui publie en 1847 une algèbre binaire dite depuis {==**booléenne**==}, qu'on doit la théorie liée à l'utilisation de la notation binaire avec uniquement des `0` et des `1`.

!!! abstract "Les chiffres binaires (*binary digits*)"

    Un nombre écrit en binaire est écrit comme une suite de `0` et de `1`, chaque chiffre binaire (en anglais *binary digit*, ou {==**bit**==}), ayant la valeur d'une puissance de 2 selon sa position dans le nombre, tout comme on décompose un nombre selon les puissances de 10 en notation décimale :

    $$
    \begin{align}
    (10~0101)_2 &= 1 \times 2^5 + 0\times 2^4 + 0 \times 2^3 + 1\times 2^2 + 0 \times 2^0 + 1\times 2^0\\
    &=1 \times 32 +0 \times 16 + 0\times 8 + 1 \times 4 + 0\times 2 +1\times 1\\
    &= 32 + 4 + 1\\
    &= 37\\
    \end{align}
    $$

!!! question "Questions I"

    1. Écrire les 10 premiers entiers (de 0 à 9) sous forme binaire.
    2. Déterminer l'écriture décimale de $(10~1010)_2$.
    3. Déterminer l'écriture décimale de $(1111~1111)_2$.
    4. Comment faire pour trouver l'écriture binaire du nombre $164$.

!!! warning "Entiers négatifs et Nombres réels"

    Ici nous avons utilisé le système binaire pour représenter des **entiers naturels**, mais nous n'aborderons pas la représentation des entiers relatifs et des nombres réels.


### Bits

!!! abstract "Bit"

    Le {==**bit**==} est l'unité d'information la plus simple dans un système de numération, ne pouvant prendre que deux valeurs, représentées par les chiffres 0 et 1. Un bit peut aussi bien représenter une alternative logique (*Vrai* et *Faux*), qu'un chiffre binaire, ou qu'une autre information ne pouvant prendre que deux états (par ex. *Ouvert* ou *fermé*).
    
    En théorie de l'information de ![Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon){: target="_blank"}, le bit est la quantité minimale d'information pouvant être transmise par un message, et constitue à ce titre l'unité de mesure de base de l'information en informatique.

    Un {==**ensemble ordonné de bits**==} permet donc de représenter des informations.

!!! question "Questions II"

    1. Combien d'informations différentes peuvent être représentées par 2 bits ? 4 bits ? 8 bits ? 10 bits ?
    2. Quel est le nombre minimal de bits nécessaire pour représenter l'alphabet latin en majuscule, sans accents et autres signes diacritiques ?
    3. Combien de bits sont nécessaires pour représenter tous les caractères de l'alphabet français, en y incluant les signes de ponctuations et les chiffres ?
    4. De manière générale, un nombre entier naturel $N$ nécessitera $n$ bits, où $n$ est l'entier naturel tel que $2^{n-1}\leqslant N < 2^n$. 
        1. Combien de bits sont nécessaire pour représenter en binaire le nombre $500$ ?
        2. Combien de bits sont nécessaires pour représenter en binaire le nombre $10~000$ ?
        3. Quel est le plus grand nombre représentable avec $24$ bits ?
    5. Il est possible d'utiliser la fonction $ln$ (*logarithme népérien*) pour obtenir le nombre $n$ de bits nécessaires pour représenter un nombre entier naturel donné $N$, par la formule 
    
    $$
    n = E\left(\dfrac{\ln(N)}{\ln(2)}\right) +1
    $$
    où $E$ est la fonction renvoyant la partie entière d'un nombre donné.
        1. Combien de bits sont nécessaires pour représenter $10^6$ ?
        2. Combien de bits sont nécessaires pour représenter $10^9$ ?


!!! abstract "Octets"

    Un {==**octet**==} est un *mot binaire* de 8 bits, et permet de représenter 256 informations différentes. Il est devenu l'unité standard de mémorisation des mémoires informatiques. Son symbole dans le système international est **o**, et ses multiples sont :

    | nom | symbole | valeur | 
    | :--- | :---: | ---: |
    | kilooctet | ko | $10^3$ |
    | mégaoctet | Mo | $10^6$ |
    | gigaoctet | Go | $10^9$ |
    | téraoctet | To | $10^{12}$ |
    | pétaoctet | Po | $10^{15}$ |
    | exaoctet | Eo | $10^{18}$ |

    



## Stockage d'informations

Comme nous l'avons vu dans la partie précédente, les informations numériques peuvent être représentées sous la forme binaire, mais elles ne sont pas les seules. Si une {==**convention**==} est adoptée, il est tout à fait possible de représenter d'autres informations, comme du texte, des images ou autres données.

### Les cartes perforées (*punch cards*)

Un des premiers systèmes de stockage de masse utilisé est la carte perforée. En 1884, Herman Hollerith dépose un brevet pour une machine électromécanique utilisant des cartes perforées, et permettant d'accélérer le recensement des états du gouvernement américain. Il lance par la suite une société qui deviendra IBM.

Une carte perforée est un support d'informations exprimées sous la forme binaire : une grille de «cases» est représentée, cases qui peuvent être perforées (1) ou non (0).

Par exemple la carte ci-dessous, modèle standard d'IBM breveté en 1928, possède 80 colonnes et 12 lignes (les lignes numérotées de 0 à 9, plus deux lignes supérieures non numérotées) permettant techniquement d'encoder un mot de 12 bits (mais en pratique seulement 9 bits étaient utilisés, les lignes numérotées 0 à 8, la ligne 9 servant de «bit de contrôle», et les deux lignes supérieures indiquant des opérations spéciales).

![carte IBM](Fortran.jpg){: style="width:95%; margin:auto;display:block;background-color: #d2dce0;"}[^IBM]

[^IBM]: Image Wikipedia, crédit :«Par Arnold Reinhold — I took this picture of an artifact in my possession. The card was created in the late 1960s or early 1970s and has no copyright notice., CC BY-SA 2.5, [https://commons.wikimedia.org/w/index.php?curid=775153](https://commons.wikimedia.org/w/index.php?curid=775153){:target="_blank"}»


Ces cartes étaient stockées par boîtes de 2 000, et le coin tronqué servait de repère pour les insérer dans le bon sens dans un chargeur de cartes ou pour les remettre à l'endroit quand la boîte tombait par terre.

!!! question "Questions III"

    La carte perforée ci-dessus encode l'expression `Z(1) = Y + W(1)`, dans le langage *Fortran*. Il est inutile de comprendre le sens de cette expression pour répondre aux questions suivantes :

    1. Quel est le code utilisé pour la lettre `Z` ?
    2. Quel est le code utilisé pour la lettre `Y` ?
    3. Quel est le code utilisé pour la lettre `W` ?
    4. Quel pourrait alors être le code pour `T`?
    4. Comment sont encodés les espaces ?
    5. Comment sont encodés les parenthèses ouvrantes et fermantes ?

ar la s




### 