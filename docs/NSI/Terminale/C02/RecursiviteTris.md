# Applications de la récursivité :  Tris de tableaux


## Rappels sur les algorithmes de tris vus en classe de première

!!! abstract "Principe du tri par insertion"
	
	Le principe du tri par insertion est le suivant : au moment où on considère un élément du tableau à trier,
	les éléments qui le précèdent sont déjà triés, tandis que les éléments qui le suivent ne sont pas encore triés. 
	
	On peut voir sur l'animation suivante extraite de wikipedia :
	
	<p align = "center">
	![gif insertion](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif){: style ="width:30%;"}
	</p>
	
	La complexité du tri par insertion est $\mathbb{O}(n^2)$ dans le pire cas et en moyenne, et linéaire dans le meilleur cas (tableau presque trié). C'est donc un tri
	dont la vitesse d'exécution dépendra fortement de la situation initiale. 
	

	??? done "Le code en Python"
		``` python linenums="1"
		def tri_insertion(L):
			N = len(L)
			for n in range(1,N):
				cle = L[n]
				j = n-1
				while j>=0 and L[j] > cle:
					L[j+1] = L[j] # decalage
					j = j-1
				L[j+1] = cle
		
		```
	
	
!!! abstract "Principe du tri par sélection"
	
	Sur un tableau de n éléments, le principe du tri par sélection est le suivant :

    * rechercher le plus petit élément du tableau, et l'échanger avec l'élément d'indice 0 ;
    * rechercher le second plus petit élément du tableau, et l'échanger avec l'élément d'indice 1 ;
    * continuer de cette façon jusqu'à ce que le tableau soit entièrement trié.
	
	On peut voir sur l'animation suivante extraite de [wikipedia](https://fr.wikipedia.org/wiki/Tri_par_s%C3%A9lection) :
	
	<p align = "center">
	![gif insertion](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif){: style ="width:30%;"}
	</p>
	
	Cet algorithme de tri, simple à comprendre, est considéré comme mauvais car sa complexité en temps est en $\mathbb{O}(n^2)$, que ce soit
	dans le pire des cas ou bien le meilleur des cas (même pour un tableau déjà trié il faudra faire toutes les comparaisons).
	

## Le tri fusion

<p align ="center">
<img src = "https://fr.web.img2.acsta.net/newsv7/19/06/26/17/10/2163592.jpg" style = "width : 25%;" />
</p>

!!! abstract "Principe du Tri Fusion (Merge Sort)"
	
	Le principe du {==**tri fusion**==}, est de séparer un tableau à trier en **deux sous-tableaux** qu'on triera récursivemment (ou itérativemment 
	mais ce ne sera pas le cas dans ce cours) de nouveau par tri fusion.
	
	Une fois les sous-tableaux triés, il faudra {==**fusionner**==} ces deux sous-tableaux en une seule identité.
		
	<p align="center">
	![Merge Sort](https://i.redd.it/rno9aidb3bm01.png){: style="width : 50%";}
	</p>


## Plus vite ! QuickSort !

!!! abstract "Principe du QuickSort"
	
	<p align="center">
	![Kwik Sort](https://i.redd.it/mqdl2t9fyi961.png){: style="width : 50%";}
	</p>