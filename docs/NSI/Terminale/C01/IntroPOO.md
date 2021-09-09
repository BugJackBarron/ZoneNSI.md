# Introduction à la promgrammation orientée objet

## Un premier exemple issu de Scratch

Observons ce jeu assez minable en Scratch (non, mais vraiment, allez-voir sur le site...).
<p align="center">
<iframe src="https://scratch.mit.edu/projects/568504906/embed" allowtransparency="true" width="485" height="402" frameborder="0" scrolling="no" allowfullscreen></iframe>
</p>

Ce jeu sommaire est construit autour de trois éléments :

* la chauve-souris ;
* l'éclair ;
* le chat.

Chacun de ces trois éléments possède : 

* sa propre zone de script;
* ses propres caractéristiques (nom, taille, costumes, position de départ, orientation...).

Et ces trois éléments réagissent en fonction {==**d'événements**==} liés soit à l'action du joueur, soit à leurs propres interactions.

L'éclair et le chat ont la possibilité d'exister sous la forme de {==**clones**==}, chacun des clones ayant {==**ses propres caractéristiques**==} bien que {==**partageant le même comportement**==}.

Aussi simpliste que Scratch paraisse, il n'en est néanmoins pas un **véritable langage de programmation**, qui plus est {==**multiparadigme**==} : il est en effet conçu pour gérer la programmation {==**impérative**==}, la programmation {==**orientée objet**==} ainsi que la programmation {==**événementielle**==}.

!!! tips "Paradigmes de programmation"

	Un paradigme est * "une représentation du monde, une manière de voir les choses, un modèle cohérent du monde qui repose sur un fondement défini" *.[Wkipedia](https://fr.wikipedia.org/wiki/Paradigme#Paradigme_en_linguistique).
	
	En programmation, plus précisemment, on parle de {==**paradigmes de programmation**==} pour exprimer lma mabière dont sont conçu et envisagés les programmes.
	On distingue entre autres :
	
	* le paradigme de la {==**programmation impérative**==}, qui est celui que nous avons utilisé jusqu'ici : on décrit les opérations en séquences d'instructions exécutées par l'ordinateur dans un ordre précis (que le langage soit compilé ou interprété). C'est le paradigme classique, celui auquel tout le monde pense quand on parle de programme informatique.
	* le paradigme de la {==**programmation orienté objet**==}, qui "consiste en la définition et l'interaction de briques logicielles appelées objets ; un objet représente un concept, une idée ou toute entité du monde physique, comme une voiture, une personne ou encore une page d'un livre. Il possède une structure interne et un comportement, et il sait interagir avec ses pairs. Il s'agit donc de représenter ces objets et leurs relation[...]". [Wikipedia](https://fr.wikipedia.org/wiki/Programmation_orient%C3%A9e_objet).	
	* le paradigme de la {==**programmation fonctionnelle**==}, qui considère le calcul en tant qu'évaluation de fonctions mathématiques.
	* le paradigme de la {==**programmation événementielle**==}, qui est fondé sur la notion d'événements. Le programme sera principalement défini par ses réactions aux différents événements qui peuvent se produire, c'est-à-dire des changements d'état de variable, par exemple l'incrémentation d'une liste, un déplacement ou un click de souris, une saisie au clavier... 
	* et [bien d'autres](https://fr.wikipedia.org/wiki/Paradigme_(programmation))...
	
Les différents langages de programmation peuvent être plus ou moins spécialisé selon un certain nombre de paradigmes. Quasimùent tous respectent le {==**paradigme originel impératif**==}. Certains langages ne dépassent pas ce paradigme (assembleur, Fortran, Algol, BASIC,... ). D'autres sont spécialisés sur un paradigme spécifique ( comme Lisp, ML, OCaml en programmation fonctionnelle, Ada, Smalltalk, C++, Ruby, C# Swift... en POO). Mais en général tous les langages cités possèdent des composantes {==**multiparadigmes**==}.

C'est le cas de Python, qui supporte la programmation :

* impérative ;
* fonctionnelle ;
* procédurale ;
* orientée objet ;
* et en partie événementielle.


## Principes	
	
	
	