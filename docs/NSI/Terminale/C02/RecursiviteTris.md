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
	

## Le tri par Fusion

<p align ="center">
<img src = "https://fr.web.img2.acsta.net/newsv7/19/06/26/17/10/2163592.jpg" style = "width : 25%;" />
</p>

!!! abstract "Principe du Tri par fusion (Merge Sort)"
	
	<p align="center">
	![Merge Sort](https://i.redd.it/rno9aidb3bm01.png){: style="width : 50%";}
	</p>


## Plus vite ! QuickSort !

!!! abstract "Principe du QuickSort"
	
	<p align="center">
	![Kwik Sort](https://i.redd.it/mqdl2t9fyi961.png){: style="width : 50%";}
	</p>