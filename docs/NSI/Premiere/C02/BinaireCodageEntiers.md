# Binaire et représentation des entiers

## L'information binaire

### Le bit

L'histoire de l'informatique est intrinsèquement dépendante de l'histoire de la maîtrise de l'électricité. Fondamentalement, tout ordinateur est construit à partir de circuits électroniques qui:

* soit ne laissent pas passer le courant électrique (*Off*);
* soit laissent passer le courant électrique (*In*).


!!! example "Exemple"

	Un circuit contenant un unique interrupteur admet donc {==**deux états**==}, il est {==**binaire**==} dans ce sens.

!!! abstract "Définition : bit"
	Un bit est l'unité élémentaire d'information pouvant prendre deux valeurs distinctes, notées 0 et 1 (binaire). Le mot &#171; {==**bit**==} &#187; vient de l'anglais &#171; **Bi**nary Digi**t** &#187;, soit littéralement *chiffre binaire*.
	
	La notation internationale pour le bit est $b$. On parlera alors de $kb$, $Mb$, $Gb$.

### Compter en binaire

Pour compter en binaire, on applique le même algorithme qu'en décimal : on ajoute 1 jusqu'à épuiser les chiffres disponibles, et quand on a terminé, on ajoute un chiffre supplémentaire au nombre. En, binaire, cela donne :


| Nombre en binaire | Nombre en décimal |
| ---: | ---: |
| 0 | 0 |
| 1 | 1 |
| 10 | 2 |
| 11 | 3 |
| 100 | 4 |
| 101 | 5 | 
| 110 | 6 | 
| 111 | 7 |
| 1000 | 8 |
| ... | ... | 

### Grouper les bits

Une information binaire est donc une suite de $0$ et de $1$. Cette information peut-être de différente nature, tout dépend de la {==**norme d'encodage**==} utilisée. En soit, la même suite binaire peut signifier des choses totalement différentes comme :

* un nombre entier ;
* un nombre flottant ;
* un caractère ;
* une note de musique ;
* ...




!!! example "Exemple"
	L'écriture binaire $101010$ signifie :
	
	* $42$ dans les nombres entiers non signés (c'est-à-dire positifs) ;
		``` python
		>>> int('101010',2)
		42
		```
	* Le caractère \* en UTF-8 :
		``` python
		>>> chr(int('101010',2))
		'*'
		```
	
!!! abstract "Bits et quantités d'informations"
	
	Avec un unique bit, on ne peux stocker que deux informations (deux nombres, deux caractères, deux notes de musiques,...). La quantité d'information différentes pouvant être représentées dépend donc du nombre de bits utilisés :
	
	=== "Avec $2$ bits :"
		??? done 
			On peux représenter $2 \times 2 = 2^2 = 4$ informations différentes. Par exemple, avec des caractères :

			| Mot | Caractère |
			| :--: | :--: | 
			| 00 | A |
			| 01 | B |
			| 10 | C |
			| 11 | D |



	=== "Avec $3$ bits :"
		??? done 
			On peux représenter $2 \times 2 \times 2= 2^3 = 8$ informations différentes. Par exemple, avec des caractères :
			
			| Mot | Caractère |
			| :--: | :--: | 
			| 000 | A |
			| 001 | B |
			| 010 | C |
			| 011 | D |
			| 100 | E |
			| 101 | F |
			| 110 | G |
			| 111 | H |

	=== "Avec $4$ bits :"
		??? done 
			On peux représenter $2 \times 2 \times 2 \times 2= 2^4 = 16$ informations différentes. Par exemple, avec des caractères, on pourra représenter jusqu'à `P`, qui sera représenté par le mot binaire `1111`
	
	
	 Avec un système à $n$ bits, on peut représenter $2^n$ informations différentes.

### Octets


!!! abstract "Octets"
	Pour quantifier les informations binaires, on utilise souvent le mot {==**octet**==} (abusivement appelé aussi [*byte*](https://fr.wikipedia.org/wiki/Byte){:target = "_blank"} dans le monde anglo-saxon).
	
	Un octet est un groupement de $8$ bits. Il permet de représenter $2^8 = 256$ informations différentes.
	
	La notation internationale pour l'octet est $o$. On parlera alors de $ko$ ( $1~ko = 1000 o$ ), $Mo$ ( $1~Mo = 10^3~ko = 10^6~o$ ), $Go$ ( $1~Go = 10^3~Mo = 10^9~o$ ), etc, mais aussi de $ko/s$, $Mo/s$, etc...
	
!!! info "Remarque"
  
	Les préfixes *kilo*, *Mega*, *Giga* ..., sont bien ceux du système international, c'est-à-dire ceux pour $10^3$, $10^6$, $10^9$... On verra dans la partie suivante qu'ils sont parfois confondus avec les préfixes binaires ( *kibi*, *Mibi*, *Gibi*...), pour lesquels le facteur de changement d'unité n'est pas $10^3$ mais $2^10 = 1024$. Ainsi $1 Mibi = 1024 kibi$.
  
 

## Ecritures en d'autres bases 

### Les entiers en base décimale

!!! abstract "Rappels : Base décimale "
	Un nombre entier écrit dans une base décimale ( base $10$ ) vérifie les conditions suivantes :
	
	* il est écrit avec les dix chiffres arabes : $0,1,2,3,4,5,6,7,8,9$ ;
	* chaque chiffre possède un poids, représentant une puissance de $10$, le poids augmentant de la droite vers la gauche en partant d'un exposant $0$.
		
!!! question "Exercice"

	=== "Enoncé"
	
		1. $14~763 = 1 \times 10^{\dots} + 4 \times 10^{\dots} + 7 \times 10^{\dots}+ 6\times 10^{\dots} + 3\times 10^{\dots}$
		2. $100~042 = 1 \times 10^{\dots} + 4 \times 10^{\dots} + 2 \times 10^{\dots}$
 
	=== "Solution"
	
		1. $14~763 = 1 \times 10^{4} + 4 \times 10^{3} + 7 \times 10^{2}+ 6\times 10^{1} + 3\times 10^{0}$
		2. $100~042 = 1 \times 10^{\dots} + 4 \times 10^{\dots} + 2 \times 10^{\dots}$


### La base 2 (système binaire)

!!! abstract "Système binaire"
	Un nombre entier écrit dans le système binaire vérifie les conditions suivantes :
	
	* il est écrit avec les deux chiffres : $0$ et $1$.
	* chaque chiffre possède un poids représentant une puissance de $2$, le poids augmentant de la droite vers la gauche en partant d'un exposant $0$.


!!! info "Remarques et notations"
	L'écriture $101$ possède aussi bien un sens en binaire (un-zéro-un) qu'en décimal ( cent-un ). Pour lever l'ambiguïté , on écrira :
	
	* $(101)_{10}$ ou simplement $101$ pour le nombre en base $10$ ;
	* $(101)_2$ pour le nombre en base $2$.


!!! question "Exercice"
	=== "Enoncé"

		Considérons le nombre $(101010)_2$. Convertissez ce nombre binaire en décimal :
		
	=== "Solution"
	
		
		$$
		\begin{array}{cccccccc}
		(101010)_2&=& 1 \times 2^{5}&+ 0 \times 2^{4}&+ 1 \times 2^{3}&+ 0 \times 2^{2}&+ 1 \times 2^{1}&+ 0 \times 2^{0}\\
		& = & 1 \times 32 & + 0 \times 16& + 1 \times 8& + 0 \times 4& + 1 \times 2& + 0 \times 1\\
		&=& 42 &&&&&\\
		\end{array}
		$$
		
 

!!! question "Exercice : Conversions de la base $2$ vers la base $10$"

	=== "Enoncé"
		Ecrire les nombres suivants en base $10$ :
		
		1. $(101)_2$
		2. $(11111111)_2$
		3. $(10010011)_2$

	=== "Solution"
	
		A venir !

!!! question "Exercice : Un peu de Python"
	
	=== "Enoncé"
		Compléter la fonction suivante, **sans utiliser `int(x,2)`**, afin qu'elle renvoie en base 10 le nombre $x$ passé en argument en base $2$, sous la forme d'une chaine de caractères. *Vous pouvez cependant utiliser la fonction built-in `int` afin de convertir une chaine de caratère en un entier.*
			``` python
			def bin2dec(x) :
				"""fonction convertissant le nombre (x)_2 en base 10
			>>> bin2dec('0')
			0
			>>> bin2dec('1')
			1
			>>> bin2dec('11')
			3
			>>> bin2dec('1000')
			8
			>>> bin2dec('11111111')
			255
				"""
			```

### Conversions de la base $10$ vers la base $2$


!!! tips "Méthode : Algorithme de conversion du nombre $(n)_{10}$ en base $2$"
	
	=== "En langage naturel"
		```
		fonction dec2bin(n) :
			base2 <- chaine de caractère vide
			Tant que n!=0 :
				base2 <- caractere(n%2)+base2
				n <- n//2
			Renvoyer base2 
		```
	
	=== "Sous forme de diagramme"
		
		``` mermaid
		
		flowchart TB
		A(Nombre n positif en décimal) --> B(base2 chaine de caractère vide)
		B --> C{n != 0}
		C --> |Non| F(base2 est la représentation de n en binaire)
		subgraph Z["Boucle principale"]
			direction LR
			C -->|oui| D[Ajouter n%2 au début de base2];
			D --> E[n prend la valeur n//2]
			E --> C 
		end
		
		
		```
	
!!! example "Exemple : Conversion de $(135)_{10}$ en base $2$"
	
	A venir !
	
	
!!! question "Conversions manuelles"

	=== "Enoncé"
		Convertir les nombres suivants en base $2$ :

		1. $(26)_{10}$
		2. $(104)_{10}$
		3. $(256)_{10}$
		4. $(42)_{10}$
		
	=== "Solution"
	
		A venir !
		
!!! question "Exercice : De l'algorithme au programme"

	=== "Enoncé"
		Compléter la fonction suivante en Python, qui renvoie la chaine de caractères correspondant à l'écriture de $n$ en base $2$.
			``` python
			def dec2bin(n) :
			"""fonction convertissant le nombre n en base 2,
			et renvoyant la chaine de caractères correspondante
			>>> dec2bin(0)
			'0'
			>>> dec2bin(1)
			'1'
			>>> dec2bin(3)
			'11'
			>>> dec2bin(8)
			'1000'
			>>> dec2bin(255)
			'11111111'
			"""
			```
	=== "Solution"
	
		A venir !


!!! abstract "Nombre de bits nécessaires"
	Soit $(x)_{10}$ un nombre écrit en base $10$.
	
	Si $n$ est l'entier tel que $2^{n-1} \leqslant x <2^n$, alors le nombre $x$ nécessitera $n$ bits pour être représenté en binaire.
	
!!! question "Exercice : Nombre de bits nécessaires"
	=== "Enoncé"
		Déterminer pour chacun des nombres ci-dessous le nombre de bits minimal qui seront nécessaire dans l'écriture binaire de ce nombre :

		1. $12$
		2. $123$
		3. $999$
		4. $1927$

	=== "Solution"
	
		A venir !



### Une autre base utile : l'hexadécimal

Outre que la lecture des nombres en écriture binaire par un humain est très compliquée, il faut remarquer que,
 de par la construction de ces nombres, la quantité de symboles utilisés en base $2$ est largement supérieur à
 celui utilisé en base $10$ - **$3,2$ fois plus grand** en moyenne sur les $100~000$ premiers entiers.

Il peut donc être utile de trouver un compromis entre la base $2$, utile pour l'ordinateur, et la base $10$, plus compréhensible par un être humain.

Ce compromis peut-être trouvé avec le système {==**hexadécimal**==}, c'est-à-dire un système de **base 16**.


!!! tips "Clé WIFI"
 	Typiquement, une clé de sécurité WIFI est un nombre binaire à 128 bits (ou 256 bits). Lorsque vous vous connectez à un nouveau réseau WIFI, vous devez taper la clé sur votre ordinateur/smartphone (on élimine ici la possibilité d'un FlashCode), mais celle ci est présentée souvent sous la forme `38326f53685c2c256164712838`, déjà particulièrement pénible à taper, et les erreurs de recopiages sont faciles à  faire et difficiles à retrouver.
	
	Ce nombre, sous sa forme binaire est celui-ci : 
	
	`111000001100100110111101010011011010000101110000101100001001010110000101100100011100010010100000111000`
	
	 De quoi faire encore plus d'erreurs en le recopiant...

!!! abstract "Base hexadécimale"
	Un nombre entier écrit dans une base hexadécimale ( base $16$ ) vérifie les conditions suivantes :

	* il est écrit avec les seize chiffres hexadécimaux : $0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F$ ;
	* chaque chiffre possède un poids représentant une puissance de $16$, le poids augmentant de la droite vers la gauche en partant d'un exposant $0$.

!!! example "Exemple"
	Le nombre hexadécimal $(5B6)_{16}$ correspond donc en décimal à :

	=== "A compléter"
	
		$$
		\begin{array}{ccccc}
		(5B6)_{16}&=& \dots \times 16^{\dots}&+ \dots \times 16^{\dots}&+ \dots \times 16^{\dots}\\
		&=& \dots \times \dots&+ \dots \times \dots&+ \dots \times \dots\\
		&=&&&\\
		\end{array}
		$$
		
	=== "Solution"
	
		$$
		\begin{array}{ccccc}
		(5B6)_{16}&=& 5 \times 16^{2}&+ 11 \times 16^{1}&+ 6 \times 16^{0}\\
		&=& 5 \times 256&+ 11 \times 16&+ 6 \times 1\\
		&=&1~462&&\\
		\end{array}
		$$

!!! question "Exercice"
	=== "Enoncé"
		Convertir de l'hexadécimal vers le décimal :

		* $(FF)_{16}$
		* $(6E)_{16}$
		* $(245A)_{16}$



!!! tips "Méthode : Convertir vers l'hexadécimal depuis le décimal"

	Pour convertir vers l'hexadécimal depuis le décimal, on utilise la même méthode 
	qu'en binaire mais en divisant par $16$.

!!! example "Exemple"

	=== "Enoncé"
		Convertir le nombre $244$ en hexadécimal.
		
	=== "Solution"
		A venir !


!!! info "Remarques"

	* A un chiffre dans la base $16$, correspond exactement $4$ chiffres dans la base $2$.
	* Cela signifie que pour écrire un octet en hexadécimal, **deux chiffres hexadécimaux suffisent**. C'est pour cette raison que les 
	octets écrits en base deux sont **groupés par 4 chiffres** :
	
	$$
	(189)_{10} = (BD)_{16} = (1011~1101)_2
	$$
	
	* Ce système de notation est très pratique pour noter les codes des couleurs (par exemple en RGB : `#7455BA` signifie que l'octet représentant le canal rouge
	a pour valeur `74`, celui du canal vert `55`, et celui du canal bleu `BA`), pour les clés de chiffrement (code Wifi par exemple), ...


??? info "Roue numérique"
	
	<link href="../Roue_Binaire.css" rel="stylesheet">
	<div class="container">
	<div class="texte">Ecriture décimale</div>
	</div>
	<div class="container" id="roue_dec">		

	<span class="digit" id ="dec_centaines">0</span>
	<span class="digit" id ="dec_dizaines">0</span>
	<span class="digit" id="dec_unites">0</span>
		
	</div>
	<div class="container">
	<span class="roll" id="rolldown">
		-
	</span>
	
	<span>
	<div id="set">
	<input type="number" id="setSpeed" name="setSpeed"
	min="0" max="300" value="100" step ="10"/>
	</div>
	<div id="reset">
	Reset
	</div>
	</span>
	<span class="roll" id="rollup">
	+
	</span>
	</div>
	<div class="container">
	<div class="texte" id="bintxt">Ecriture binaire</div>
	</div>
	<div class="container" id="roue_bin">	

	<span class="digit" id ="bin_7">0</span>
	<span class="digit" id ="bin_6">0</span>
	<span class="digit" id ="bin_5">0</span>
	<span class="digit" id ="bin_4">0</span>
	<span class="digit" id ="bin_3">0</span>
	<span class="digit" id ="bin_2">0</span>
	<span class="digit" id ="bin_1">0</span>
	<span class="digit" id ="bin_0">0</span>

	</div>
	<div class="container">
	<div class="texte" id="hexatxt">Ecriture hexadécimale</div>
	</div>
	<div class="container" id="roue_hexa">
	
	<span class="digit" id ="hexa_1">0</span>
	<span class="digit" id ="hexa_0">0</span>

	</div>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="../Roue_binaire.js"></script>
	
	Accès au fichier de base : [ici](Roue_binaire.html)


## Opérations élémentaires sur les nombres binaires
###Sommes de nombres binaires
!!! tips "Méthode : Additionner deux nombres entiers en base 2"

	La technique d'addition de deux nombres binaire est la même que pour des nombres en écriture décimale :
	
	=== "En décimal"
	
		$$
		\begin{array}{cccc}
		&1&4&9\\
		+&&7&8\\\hline
		&&&\\
		\end{array}
		$$ 
	
	=== "En binaire"
	
		$$
		\begin{array}{*{9}{c}}
		&1&0&0&1&0&1&0&1\\
		+&&1&0&0&1&1&1&0\\\hline
		&&&&&&&&\\
		\end{array}
		$$
	
### Produits de nombres binaires

!!! tips "Méthode : Multiplier deux nombres entiers en base 2"
	La technique de multiplication de deux nombres binaire est la même que pour des nombres en écriture décimale - mais la retenue peut se propager parfois plus loin que le rang immédiatement supérieur :

	=== "En décimal"
	
		$$
		\begin{array}{cccc}
		&&2&7\\
		\times&&1&3\\\hline
		&&&\\
		+&&&\\\hline
		&&&\\
		\end{array}
		$$
	
	=== "En binaire"
	
		$$
		\begin{array}{*{10}{c}}
		&&&&&1&1&0&1&1\\
		\times&&&&&&1&1&0&1\\\hline
		&&&&&&&&&\\
		+&&&&&&&&&\\
		+&&&&&&&&&\\
		+&&&&&&&&&\\\hline
		&&&&&&&&&\\
		\end{array}
		$$