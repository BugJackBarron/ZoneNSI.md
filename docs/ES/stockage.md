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


### Bits et octets

!!! abstract "Bit"

    Le {==**bit**==} est l'unité d'information la plus simple dans un système de numération, ne pouvant prendre que deux valeurs, représentées par les chiffres 0 et 1. Un bit peut aussi bien représenter une alternative logique (*Vrai* et *Faux*), qu'un chiffre binaire, ou qu'une autre information ne pouvant prendre que deux états (par ex. *Ouvert* ou *fermé*).
    
    En théorie de l'information de ![Shannon](https://fr.wikipedia.org/wiki/Claude_Shannon){: target="_blank"}, le bit est la quantité minimale d'information pouvant être transmise par un message, et constitue à ce titre l'unité de mesure de base de l'information en informatique.

    Un {==**ensemble ordonné de bits**==} permet donc de représenter des informations.

!!! question "Questions II"

    1. Combien d'informations différentes peuvent être représentées par 2 bits ? 4 bits ? 8 bits ? 10 bits ?
    2. Quel est le nombre minimal de bits nécessaire pour représenter l'alphabet latin en majuscule, sans accents et autres signes diacritiques ?
    3. Combien de bits sont nécessaires pour représenter tous les caractères de l'alphabet français, en y incluant les signes de ponctuations et les chiffres ?


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

Comme nous l'avons vu dans la partie précédente, 

### Les cartes perforées

### 