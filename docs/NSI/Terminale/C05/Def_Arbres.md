# Arbres Binaires : définitions et propriétés

Les listes, piles et files que nous avons croisé jusqu'ici sont utilisées pour représenter de structures pouvant être énumérées séquentiellement. Elle sont particulièrement efficcaces lorsqu'il s'agit d'accéder au premier élément (ou au dernier selon l'implémentation). Elles ne le sont pas contre pas quand il s'agit **d'accéder à une élément à une position arbitraire** dans la structure, car il faut parcourir toute la liste/pile/file jusqu'à la position recherchée, ce qui donne un temps d'accès proportionnel à la taille de la structure (donc en $\mathbb{O}(n)$).

## Structures arborescentes

Les {==**structures arborescentes**==}, c'est-à-dire sous forme d'arbre, sont une autre forme de **structures chaînées** dans laquel l'accès à un élément se fait potentiellement bien plus rapidement qu'avec les listes chaînées.

Ces types de structures arborescentes sont omniprésentes en informatiques, ne serait-ce que par l'organisation du système de fichier :

![Arbre Système de Fichier](CM1_Arbre.png){: style="width:50%;"}

!!! abstract "Structure arorescente"
	Une {==**structure arborescente**==} est une structure chaînéee construite à partir d'un point de départ qui se scinde en plusieurs branches à chaque étapes.


## Arbres Binaires

### Définitions et vocabulaire

!!! abstract "définition : Arbre Binaire"
	Un {==**arbre binaire**==} est un cas particulier de structure arborescente ou chaque position ouvre sur exaactement deux branches.
	Plus précisemment, un {==**arbre binaire**==} est un ensemble fini de {==**noeuds**==} correspondant à l'un des deux cas suivants :
	
	* Soit l'arbre est vide, c'est-à-dire qu'il ne contient aucun **noeud**.
	* Soit l'arbre n'est pas vide, et ses **noeuds** sont structurés de la façon suivante :
		* un noeud est appelé {==**la racine**==} de l'arbre ;
		* les noeuds restants sont séparés en deux sous-ensembles qui forment récursivement {==**deux sous-arbres binaires**==} appelés respectivemment **sous-arbre gauche** et **sous-arbre droit** ;
		* la racine est reliée à chacune des racines de ces sous-arbres gauches et droits (àconditions su'ils ne soient pas vides).
		
	
		
!!! example "Exemples et contre-exemples d'arbres binaires"

	<p align="center">
	![Extrait Wikipedia](https://upload.wikimedia.org/wikipedia/commons/0/02/Nary_to_binary_tree_conversion.png){:	style="width:30%; background-color: #546d78;"}
	</p>
	
	L'arbre de gauche n'est pas un arbre binaire : 6 sous-arbres sont-rattachés à $A$, les sous-arbres de racines $B,C,D,E,F,G$.
	
	L'arbre de droite est bien un arbre binaire, de chaque noeud partent deux sous-arbres, éventuellement vides.
	
		
!!! abstract "Vocabulaire des arbres"

	On considère l'arbre binaire ci-dessous :
	
	<p align="center">
	![Arbre 4 Noeuds](P1_Arbre1.png){: style="width:30%; background-color: #546d78;"}
	</p>
	
	* La {==**taille de l'arbre**==} est $4$, c'est le nombre de noeuds qui le compose.
	* Le noeud {==**racine**==} est le noeud $1$.
	* Le sous-arbre gauche à partir de $1$ contient deux noeuds ($2$ et $3$), le sous-arbre droit un seul ($4$).
	* le noeud $1$ possède deux {==**fils**==} : son {==**fils gauche**==} est $2$ et son {==**fils droit**==} est $3$.
	* Le sous-arbre gauche à partir de $2$ n'est pas vide (il contient le noeud $3$), le sous-arbre droit lui l'est.
	* Le noeud {==**parent**==} du noeud $3$ est le noeud $2$.
	* Les deux sous-arbres à partir de $3$ sont vides, touts comme ceux de $4$. On dira que les noeuds $3$ et $4$ sont des {==**feuilles**==} de l'arbre.
	
!!! tips "Remarques"

	Les arbres binaires sont utilisés pour traiter des données. Chaque noeud peut donc être représenté par la donnée qu'il contient. Ainsi, dans les arbres ci-dessus :

	* un contient des valeurs numériques ($1$, $2$, $3$ et $4$) ;
	* l'autre contient des caractères ($A$ à $L$).
	
	

!!! question "Exercice"
	Pour chacun des arbres binaires ci-dessous, préciser sa taille, sa racine ainsi que les noeuds feuilles :
	
	=== "Enoncé"
	
		<div class="container">
		<div class="column2">
		<h6>Arbre 1</h6>
		
		
		![Exo arbre 1](P1_Arbre2.png){: style="width:90%; background-color: #546d78;"}
			
		</div>
		<div class="column2">
		<h6>Arbre 2</h6>
		
		![Exo arbre 2](P1_Arbre3.png){: style="width:90%; background-color: #546d78;"}
			
		</div>		 
		</div>
		
	=== "Solution"
	
		A venir !
		
		
	
	