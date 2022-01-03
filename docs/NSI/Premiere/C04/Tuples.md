%%!TEX encoding = UTF-8 Unicode

\documentclass[a4paper,12pt]{article}
\input{../../preambule.tex}
\input{../../figures.tex}



\lhead{\ccby}
\rhead{\small{ $1^{\text{ère}}$ NSI}}
\chead{\small{ $C05$ Tuples, tableaux et algorithmes de tableaux}}


\lfoot{\tiny{Ann\'ee 2020-2021}}
\cfoot{\textbf{Page \thepage/\pageref{LastPage}}}
%\cfoot{}
\rfoot{\tiny{www.zonensi.fr}}

\begin{document}
\sffamily %Pourutiliser une police sans empatement
\begin{center}
 \large{\textbf{$C05-01$ Tuples et algorithmes de parcours}}
\end{center}
\textit{Largement inspiré du fabuleux site Pixees.fr}

\section*{Introduction : les séquences}

 En informatique, il est possible de \og stocker \fg plusieurs grandeurs dans une même structure, appelée une \textbf{séquence}. De façon plus précise, une séquence est un ensemble \textbf{fini et ordonné} d'éléments, repérés par un \textbf{indice}.\\
 
 Dans de très nombreux langages informatiques, mais pas dans tous, les indices \textbf{démarrent à zéro}.
 
 \begin{exemple}
  La liste des mois de l'année est une séquence, chaque mois étant repéré par son indice (le numéro du mois), qui commence à $1$.
 \end{exemple}

 Nous étudierons deux types de séquences en Python : les tuples et les tableaux (listes).

\section{Définition et utilisation}
\begin{definition}{Tuples}
 En Python, un \textbf{tuple} est une séquence, qui est définie \textbf{entre parenthèses}, et dont les éléments sont séparés par des \textbf{virgules}, et dont les \textbf{indices commencent à $0$}. Les éléments peuvent être de même nature ( \texttt{int}, \texttt{float},\texttt{str} ou \texttt{bool}), ou bien de natures variées.\\
 Un tuple possède une \textbf{longueur}, qui est le nombre d'éléments le composant. Elle est obtenue grâce à la fonction \texttt{len()}.\\
 
\end{definition}
\begin{exemple}
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6)
>>> mon_autre_tuple = ("chien", "chat", "poisson rouge")
>>> un_tuple_bizarre = (2, 3.1, "toto", True)
>>> tuple_vide = ()
 \end{lstlisting}
Dans \texttt{mon\_autre\_tuple} :
\trianglenoir
\begin{itemize}
 \item \texttt{"chien"} est l'élément d'indice $0$ ;
 \item \texttt{"chat"} est l'élément d'indice $1$ ;
 \item \texttt{"poisson rouge"} est l'élément d'indice $2$.
\end{itemize}
 \begin{lstlisting}
>>> len(mon_tuple)
5
>>> len(mon_autre_tuple)
3
>>> len(un_tuple_bizarre)
4
>>> len(tuple_vide)
0
 \end{lstlisting}


\end{exemple}
\begin{propriete}{Accéder aux éléments}
Pour accéder aux élements d'un tuple, on utilise la même notation que pour accéder aux caratères d'une chaines de caractères : le notation \textbf{entre crochets}.
\end{propriete}
\begin{exemple}
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6, 9, 4, 3, 1, 12)
>>> mon_tuple[2]
5	  
 \end{lstlisting}
\end{exemple}
\begin{Exercice}
\begin{enumerate}
\item Que renvoie \texttt{un\_tuple\_bizarre[1]} ?\hfill\caserepsanssaut{5}{0.75}
\item A quelle valeur est associée le nom \texttt{a} après exécution du code suivant ?
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6, 9, 4, 3, 1, 12)
>>> a = mon_tuple[6]	  
 \end{lstlisting}
\caserep{\linewidth}{0.75}
\item Dans le code précédent, que faut-il mettre entre les crochets pour que le nom \texttt{a} soit associé à la valeur $1$ ?
\caserepsanssaut{5}{0.75}
\item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6, 9, 4, 3, 1, 12)
>>> a = mon_tuple[-1]	  
 \end{lstlisting}
 \caserep{\linewidth}{0.75}
 \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6, 9, 4, 3, 1, 12)
>>> a = mon_tuple[10]	  
 \end{lstlisting}
 \caserep{\linewidth}{1.5}
  \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (2, 7, 5, 8, 6, 9, 4, 3, 1, 12)
>>> mon_tuple[5] = 42	  
 \end{lstlisting}
 \caserep{\linewidth}{2.5}
  \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = ("le", "bonjour", "monde")
>>> print(f"{mon_tuple[1].capitalize()} {mon_tuple[0]} {mon_tuple[2]} !")	  
 \end{lstlisting}
  \caserep{\linewidth}{0.75}
    \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> def add(a, b) :
	return (a, b, a+b)
>>> mon_tuple = add(5,8)
>>> print(f"{mon_tuple[0]} + {mon_tuple[1]} = {mon_tuple[2]}")
 \end{lstlisting}
  \caserep{\linewidth}{0.75}
  \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = ("Luke Skywalker", "Mark Hamill", "Jedi", "Dark Vador")
>>> personnage, acteur, metier, pere = mon_tuple
 \end{lstlisting}
  \caserep{\linewidth}{1.5}
 \begin{info}{Tuple unpacking}
 La méthode utilisée ci-dessus s'appelle le \textbf{tuple unpacking}, soit \og désempaquetage \fg de tuple. Elle est très souvent utilisée pour décomposer des tuples renvoyés comme valeur de retour d'une fonction.
  \end{info}
    \item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> def euclide(a, b) :
	return (a,b,a//b,a%b)
>>> res = euclide(20,7)
>>> type(res)		
>>> diviseur, dividende, quotient, reste = res
>>> type(quotient)
 \end{lstlisting}
  \caserep{\linewidth}{0.75}
\end{enumerate}
\end{Exercice}
\section{Parcourir une séquence}
\begin{propriete}{Parcours de séquence}
Le parcours d'une séquence ( tuple ou tableau), se fait par l'intermédiaire d'une boucle \texttt{for}. dans de nombreux langages de programmation, le parcours se fait par l'intermédiaire d'un compteur qui \texttt{itère} jusqu'à atteindre l'indice maximal du tableau.
\end{propriete}
\begin{exemple}
 \begin{lstlisting}
>>> mon_tuple = (1, 3, 5, 7)
>>> for i in range(0,len(mon_tuple)) :
	print(mon_tuple[i])
\end{lstlisting}
\coche
\begin{itemize}
\item Pour rappel, la fonction \texttt{range(a,b)} itère sur les entiers naturels de $a$ inclus à $b$ exclu. Ici, la parcours se fait donc pour $i$ allant de $0$ à \texttt{len(mon\_tuple)}, soit $4$.
\item La valeur de départ de la fonction \texttt{range} étant $0$, on aurait pu l'omettre.
\end{itemize}
\end{exemple}
\begin{propriete}{La spécificité de Python}
Le parcours par indice est possible en Python, et parfois nécessaire. Mais il existe  une possibilité de parcours de la séquence plus directe :
 \begin{lstlisting}
>>> mon_tuple = (1, 3, 5, 7)
>>> for element in mon_tuple :
	print(element)
\end{lstlisting}
A chaque tour de boucle, le nom \texttt{element} va être associé à une valeur du tuple.
\end{propriete}
\begin{remarques}
\coche
\begin{itemize}
\item le nom \texttt{element} n'est qu'un choix de ma part, j'aurais tout aussi bien pu écrire \texttt{toto}.
\item Ce type de boucle existe aussi dans d'autres langages, et porte souvent le nom de boucle \texttt{foreach}.
\item Un inconvénient est que vous n'avez que l'élément, qu'il vous manque son indice. heureusement, une fonction Python (\texttt{enumerate}), peu permettre de combiner les deux types de boucles. Je vous laisserai chercher les informations nécessaires si vous rencontrez une situation où vous avez besoin de l'élément et de son indice.
\end{itemize}
\end{remarques}
\begin{Exercice}
\begin{enumerate}
\item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (12, 15, 34, 23, 11, 15, 36)
>>> for n in mon_tuple :
	if n%2 == 0 :
		print(n)
 \end{lstlisting}
  \caserep{\linewidth}{1.25}
\item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (12, 15, 34, 23, 11, 15, 36)
>>> for i in range(len(mon_tuple)) :
	if mon_tuple[i]%2 == 0 :
		print(mon_tuple[i])
 \end{lstlisting}
  \caserep{\linewidth}{1.25}
\item Essayez et commentez le code suivant :
 \begin{lstlisting}
>>> mon_tuple = (12, 15, 34, 23, 11, 15, 36)
>>> for i in range(len(mon_tuple)) :
	if i%2 == 0 :
		print(mon_tuple[i])
 \end{lstlisting}
  \caserep{\linewidth}{1.25}
 \item Que faut-il écrire pour obtenir les termes impairs du tuple ?
   \caserep{\linewidth}{2.5}
\item Que faut-il écrire pour obtenir les termes de rang impairs du tuple ?
   \caserep{\linewidth}{2.5}
\end{enumerate}
\end{Exercice}
\begin{ExerciceNomme}{Algorithmes de parcours}
\noindent Pour chacun des exercices ci-dessous, je vous demande :
\coche
\begin{itemize}
\item de vous mettre par 2;
\item de chercher d'abord à la main, sur papier ;
\item de décrire l'algorithme demandé en langage naturel;
\item enfin d'en proposer une version Python.
\end{itemize}

\noindent Pour chacun des exercices suivants, on suppose que les tuples donnés sont des tuples de nombres, entiers ou flottants, et que ces tuples sont non vides.

\begin{enumerate}
\item Trouver un algorithme puis écrire une fonction Python \texttt{maximum(t)} qui prend un tuple en entrée et renvoie le plus grand nombre de ce tuple, \emph{sans utiliser la fonction built-in \texttt{max}}.
\item Trouver un algorithme puis écrire une fonction Python \texttt{minimum(t)} qui prend un tuple en entrée et renvoie le plus petit nombre de ce tuple, \emph{sans utiliser la fonction built-in \texttt{min}}.
\item Trouver un algorithme puis écrire une fonction Python \texttt{somme(t)} qui prend un tuple en entrée et renvoie la somme des valeurs de ce tuple, \emph{sans utiliser la fonction built-in \texttt{sum}}.
\item Trouver un algorithme puis écrire une fonction Python \texttt{moyenne(t)} qui prend un tuple en entrée et renvoie la moyenne des valeurs de ce tuple, \emph{sans utiliser la fonction built-in \texttt{sum}}.

\item Trouver un algorithme puis écrire une fonction Python \texttt{palindrome(t)} qui prend un tuple en entrée et renvoie \texttt{True} si le tuple est un palindrome, et \texttt{False} sinon.
\begin{info}{Palindrome}
Un palindrome est une séquence qui peut se lire dans les deux sens sans changer ses valeurs :
\coche
\begin{itemize}
\item $(6, 4, 3, 4, 6)$ est un palindrome;
\item $(2, 4, 4, 2)$ est un palindrome;
\item $(12)$ est un palindrome ;
\item $(3, 4, 5, 3)$ n'est pas un palindrome.
\end{itemize}
Si vous le codez suffisamment bien, votre code devrait aussi fonctionner pour les chaines de caractères comme : \og été \fg, \og kayak \fg, \og Noël a trop par rapport à Léon \fg ou \og Engage le jeu que je le gagne \fg.
\end{info}

\begin{histoire}{Une citation}
\og Les tentatives de création de machines pensantes nous seront d’une grande aide pour découvrir comment nous pensons nous-mêmes. \fg
\begin{flushright}
De Alan Turing / Conférence à la BBC - 15 Mai 1951
\end{flushright}
\end{histoire}

\end{enumerate}

\end{ExerciceNomme}





\end{document}
