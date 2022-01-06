# Listes et compréhensions de listes en Python, introduction à la notion de coût en temps


## Les tableaux
!!! abstract "Tableaux"
	En informatique, un tableau est une structure de données représentant une séquence finie d'éléments auxquels on peut accéder efficacement par leur position, ou indice, dans la séquence. C'est un type de conteneur que l'on retrouve dans un grand nombre de langages de programmation. On parle aussi de tableau indexé.

	Dans les langages à **typage statique** (comme C, Java et OCaml), tous les éléments d'un tableau doivent être du même type. Certains langages à **typage dynamique**, tels que Python, permettent des tableaux hétérogènes (donc avec des données de natures différentes).

!!! abstract "Les tableaux en Python"
	En Python, un tableau est représenté par un objet de type `list`. Les principales différences entre les types `list` et `tuple` sont :
	
	* un objet de type `list` est une séquence **entre crochets** :
	
		```` python
		>>> mon_tab = [45, 24, -35, -12]
		>>> type(mon_tab)
		<class 'list'>
		````
	* un objet de type `list` est {==**mutable**==}, ce qui n'est pas le cas d'un `tuple` :

		=== "Code"
			```` python
			>>> mon_tab = [45, 24, -35, -12]
			>>> mon_tab[2]  = 1000
			>>> mon_tab
			[45, 24, 1000, -12]
			>>> mon_tuple=(45, 24, -35, -12)
			>>> mon_tuple[2] = 1000
			Traceback (most recent call last):
			  File "<pyshell>", line 1, in <module>
			TypeError: 'tuple' object does not support item assignment
			````
		=== "Python Tutor"
		
			<iframe width="800" height="500" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=mon_tab%20%3D%20%5B45,%2024,%20-35,%20-12%5D%0Amon_tab%5B2%5D%20%20%3D%201000%0Aprint%28mon_tab%29%0Amon_tuple%3D%2845,%2024,%20-35,%20-12%29%0Amon_tuple%5B2%5D%20%3D%201000&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>
			
	Les types `list` et `tuple` partagent sinon les mêmes propriétés : indices, accès aux éléments, longueur avec `len()`, parcours séquentiel avec `for`...
	
	En particulier les algorithmes vus précédemment sont aussi valable pour un tableau.


!!! question "Algorithme de recherche séquentiel"

	=== "Enoncé"
		On veut construire une fonction `chercheElement(elem, monTab)` qui renvoie :

		* l'indice de *la première occurrence* de `elem` si `elem` est présent dans le tableau `monTab` ;
		* la longueur du tableau si l'élément `elem` n'est pas présent dans le tableau `monTab`.
		
		1. Décrire en pseudo-code un algorithme définissant cette fonction.
		2. Proposer une implémentation de ce pseudo-code en Python.
		3. Quel est le {==**coût en temps**==} de cet algorithme ? (*à faire avec le professeur.*)

	=== "Solution"
		
		A venir !

!!! info "Méthode *built-in* `index` en Python"
	La fonction précédente est déjà implémentée en Python, avec une différence : elle renvoie une erreur si l'élément cherché n'est pas dans le tableau.
	
	```` python
	>>> mon_tab =  [45, 24, -35, -12, 24]
	>>> mon_tab.index(24)
	1
	>>> mon_tab.index(36)
	Traceback (most recent call last):
	File "<pyshell>", line 1, in <module>
	ValueError: 36 is not in list
	````
	
## Spécificité des listes en Python

!!! abstract "Méthodes et pratiques des listes"

	1. "Construire une liste vide :"
\begin{lstlisting}
>>> monTab = [ ] # ou bien
>>> monTab = list()
 \end{lstlisting}
\item \textbf{Ajouter un élément à la fin d'une liste :}
 \begin{lstlisting}
>>> monTab.append(3)
>>> monTab
[3]
>>> monTab.append(5)
>>> monTab.append(7)
>>> monTab
[3, 5, 7]
 \end{lstlisting}
 \item \textbf{Supprimer et récupérer le dernier élément du tableau :}
 \begin{lstlisting}
>>> dernier = monTab.pop()
>>> dernier 
7
>>> monTab
[3, 5]
 \end{lstlisting}
La méthode \texttt{pop} possède d'autres propriétés que je vous laisse rechercher.
  \item \textbf{Convertir un tableau en tuple :}
 \begin{lstlisting}
>>> monTuple = tuple(monTab)
>>> monTuple
(3, 5)
 \end{lstlisting}
  \item \textbf{Convertir un tuple en tableau :}
 \begin{lstlisting}
>>> monTab = list(monTuple)
>>> monTab
[3, 5]
 \end{lstlisting}
   \item \textbf{Extraire des parties d'un tableau grâce aux \texttt{slices} :}
 \begin{lstlisting}
>>> monTab = [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
>>> monTab[ :4]
[35, 36, 37, 38]
>>> monTab[7: ]
[42, 43, 44, 45, 46, 47]
>>> monTab[4:7]
[39, 40, 41]
 \end{lstlisting}
   \item \textbf{Concaténer des tableaux:}
 \begin{lstlisting}
>>> [1, 2, 3] + [7, 8, 9]
[1, 2, 3, 7, 8, 9]
 \end{lstlisting}
 
\end{itemize}
\end{propriete}
\begin{Exercice}
En utilisant les méthodes présentées ci-dessus :
\begin{enumerate}
\item Écrire une fonction \texttt{carre(n)} qui renvoie le tableau des carrés des nombres entiers compris entre $0$ et $n-1$ (\texttt{carre(4)} doit renvoyer \texttt{[0, 1, 4, 9]}).
\item Écrire une fonction \texttt{imagesf(deb,fin)} qui renvoie le tableau  des images des nombres entiers compris entre \texttt{deb} et \texttt{fin} par la fonction $f :x \mapsto 3x^2-2x+1$ (\texttt{imagef(-2,3)} doit renvoyer \texttt{[17, 6, 1, 2, 9, 22]}).
\item Écrire une fonction \texttt{genereListe(n)} qui renvoie un tableau de $n$ nombres aléatoires compris entre $1$ et $n^2$. ( On pourra importer une fois le module \texttt{random} et utiliser la fonction\texttt{random.randint(a,b}) qui renvoie un nombre aléatoire entre $a$ et $b$ inclus).
\item Ecrire une fonction \texttt{insere(monTab, val, i)} qui insère dans le tableau \texttt{monTab} l'élément \texttt{val} à l'indice \texttt{i},en supposant que $i<len(monTab)$ (\texttt{insere([1, 2, 3, 4],5,2)} doit renvoyer \texttt{[1, 2, 5, 3, 4]})
\item Écrire une fonction \texttt{compter(monTab,val)} permettant de compter le nombre d'occurrences de \texttt{val} dans \texttt{monTab} (\texttt{compter([4, 6, 8, 6, 7, 6, 9]▒, 6)} doit renvoyer $3$, et \texttt{compter([2, 4, 6],3)} doit renvoyer $0$).
\item Écrire une fonction \texttt{compterIndices(monTab,val)} permettant de renvoyer un tableau des occurrences de \texttt{val} dans \texttt{monTab} (\texttt{compter([4, 6, 8, 6, 7, 6, 9]▒, 6)} doit renvoyer $[1, 3, 5]$, et \texttt{compter([2, 4, 6],3)} doit renvoyer $[~]$).
\item Écrire une fonction \texttt{separer(monTab,val)}  permettant, à partir d'une liste de nombres \texttt{monTab} d'obtenir deux listes. La première comporte les nombres inférieurs ou égaux à un nombre donné, la seconde les nombre qui lui sont strictement supérieurs.
\texttt{separer([45, 21, 56 ,12, 1, 8, 30, 22, 6, 33], 30)}  doit renvoyer :
\texttt{[21, 12, 1, 8, 30, 22, 6], [45, 56, 33]}
\item Écrire une fonction \texttt{plusProche(monTab,val)}  permettant de rechercher la plus proche valeur d'un nombre dans une liste.
\texttt{plusProche([45, 21, 56 ,12, 1, 8, 30, 22, 6, 33], 20)}  doit renvoyer 21.
\end{enumerate}
\end{Exercice}
\section{Construction de listes par compréhension}
\begin{info}{Compréhensions de listes}
\noindent Une des spécificités de Python est la capacité à construire des listes (et des tuples) par compréhension. Cette capacité est partagée avec d'autres langages, comme \texttt{Haskell}.
\end{info}
\begin{Application}{premières compréhensions}
\begin{enumerate}
\item Quel est le tableau associé à \texttt{monTab} ?
\begin{lstlisting}
monTab = [4*nb for nb in range(100)]
\end{lstlisting}
\item Quel est le tableau associé à \texttt{monTab} ? Pourquoi ?
\begin{lstlisting}
monTab = [3*nb for nb in range(100) if nb%2==0]
\end{lstlisting}
\item Quel est le tableau associé à \texttt{monTab} ?
\begin{lstlisting}
monTab = [let for let in 'Abracadabra']
\end{lstlisting}
\item Quel est le tableau associé à \texttt{monTab} ? Pourquoi ?
\begin{lstlisting}
monTab = [let for let in 'Abracadabra' if let.upper()!='A']
\end{lstlisting}
\item Quel est le tableau associé à \texttt{monTab} ? Pourquoi ?
\begin{lstlisting}
monTab = [ord(let) for let in 'Abracadabra']
\end{lstlisting}
\end{enumerate}
\end{Application}
\begin{ExerciceNomme}{Réduire le code}
\noindent Comme vous avez pu le constater, les compréhensions sont rapides à écrire. Et certaines fonctions de l'exercice n°2 peuvent être considérablement réduites : les fonctions \texttt{carre}, \texttt{imagef} et \texttt{genereListe}. \\
Utilisez les compréhensions pour réduire leur taille.
\end{ExerciceNomme}
\end{document}
