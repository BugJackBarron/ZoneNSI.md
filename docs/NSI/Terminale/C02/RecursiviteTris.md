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
	

	??? quote "Le code en Python"
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
	
	??? quote "Le code en Python"
		``` python
			def tri_selection(tab):
				for i in range(len(tab)):
				  # Trouver le min
				   min = i
				   for j in range(i+1, len(tab)):
					   if tab[min] > tab[j]:
						   min = j
							
				   tmp = tab[i]
				   tab[i] = tab[min]
				   tab[min] = tmp
			   return tab
		```
		
	!!! info "Complexié en temps comparée" 
		

## Le tri fusion

<p align ="center">
<img src = "https://fr.web.img2.acsta.net/newsv7/19/06/26/17/10/2163592.jpg" style = "width : 25%;" />
</p>

!!! abstract "Principe du Tri Fusion (Merge Sort)"
	
	Le principe du {==**tri fusion**==}, est de séparer un tableau à trier en **deux sous-tableaux** qu'on triera récursivemment (ou itérativemment 
	mais ce ne sera pas le cas dans ce cours) de nouveau par tri fusion.
	
	Une fois les sous-tableaux triés, il faudra {==**fusionner**==} ces deux sous-tableaux en une seule identité.
	
	Cet algorithme est  du type {==**diviser pour régner**==} (*Divide and Conquer*) : on sépare la tâche à priori difficile en deux tâches plus simples (ici, il s'agit de diminuer la taille des tableaux). Il a été inventé par {==**John Von Neumann en 1945**==}.
		
	<p align="center">
	![Merge Sort](https://i.redd.it/rno9aidb3bm01.png){: style="width : 50%";}
	</p>


	
	

!!! question "Fonction de fusion"

	=== "Exercice"
		La principale difficulté dans cet algorithme est de créer une fonction fusionnant les deux tableaux triés. 
		
		1. Avant commencer, regardez la vidéo suivante :
		<p align="center">
		<iframe src="//video.toutatice.fr/video/24064-fusion-de-deux-tableaux-tries/?is_iframe=true" size="240" width="1280" height="720" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>
		</p>
		2. De combien de variables compteurs avons nous besoins ?
		3. Quel type de boucle allons nous utiliser ?
		4. Que se passe-t-il dans la idéo quand $j$ atteint la valeur $3$ ?
		5. Rédiger en langage naturel l'algorithme fusionnant deux tableaux triés.
		6. Implémenterune fonction `fusion(t1, t2)` qui prend en argument deux tableaux supposés triés (on ne vérifiera pas), et qui renvoie le tableau trié contenant tous les éléments des deux tableaux `t1` et `t2`.
		On pourra utiliser les tests suivants pour vérifier que la fonction est correcte :
		??? quote "Les tests"
			``` python
			>>> fusion([12,35,45],[4,42,63])
			[4, 12, 35, 42, 45, 63]
			>>> fusion([12,35], [57])
			[12, 35, 57]
			>>> fusion([12,35], [42,57])
			[12, 35, 42, 57]
			>>> fusion([12,35], [])
			[12, 35]
			>>> fusion([], [12,35])
			[12, 35]
			>>> fusion([42,57,67,75], [12,35])
			[12, 35, 42, 57, 67, 75]
			>>> fusion([], [])
			[]
			```
		
	=== "Solution"
		A venir
		
!!! question "Tri Fusion Récursif"
	=== "Exercice"
		Une fois la fonction `fusion` codée, l'algorithme de tri par fusion est simple :
		
		1. Regardez la vidéo suivante :
		<p align="center">
		<iframe src="//video.toutatice.fr/video/24034-tri-fusion-recursif/?is_iframe=true" size="240" width="1280" height="720" style="padding: 0; margin: 0; border:0" allowfullscreen ></iframe>
		</p>
		2. Quel est le cas de base ?
		3. Quel est le cas récursif ?
		4. Implémenter une fonction `triFusion(t1, t2)` qui prend en argument deux tableaux et renvoie le tableau trié contenant les éléments des deux tableaux `t1` et `t2`.
		
	=== "Solution"
		A venir !
		
!!! question "Complexié en temps"
	
	=== "Exercice"
		
		1. Copiez-collez le code ci-dessous permettant d'utiliser le décorateur `@timeit` :
		``` python 
		import time                                                

		def timeit(method):

			def timed(*args, **kw):
				ts = time.time()
				result = method(*args, **kw)
				te = time.time()
				print(f" {method.__name__} ({args},{kw}) {te-ts}" )
				return result

			return timed
		```
		2. Créer une fonction `genereTab(n)` qui crée un tableau de taille $n$ d'entiers aléatoires compris entre $0$ et $n^2$.
		3. Créer à l'aide de toutes les fonctions précédentes une fonction `testeTemps(n)` qui compare les temps d'exécution des différents tris pour $n$ valant $100$, $1~000$, $10~000$. 
		**Attention**, il faudra effectuer à chaque fois les tests sur le même tableau, et donc créer des copies du tableau original avant de le trier (on peut utiliser la fonction 
		`deepcopy` du module `copy`)
		4. Que peut-on en conclure quand à la complexité en temps du tri fusion ?
		
	=== "Solution"
		A venir !
		
!!! info "Complexités du tri fusion"
	La version la plus simple du tri fusion sur les tableaux a une efficacité comparable au tri rapide, mais elle n'opère pas en place : une zone temporaire de données supplémentaire de taille égale à celle de l'entrée est nécessaire (des versions plus complexes peuvent être effectuées sur place mais sont moins rapides).
	La complexité en temps est en $\mathbb{O}(n log(n))$ dans tous les cas, et la complexité en espace est en général en $\mathbb{O}(n)$.

	
## Plus vite ! QuickSort ! (Hors programme)


!!! abstract "Principe du QuickSort"
	
	<p align="center">
	![Kwik Sort](https://i.redd.it/mqdl2t9fyi961.png){: style="width : 50%";}
	</p>