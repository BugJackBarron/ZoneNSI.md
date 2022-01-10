# Premiers algorithmes de tri de tableaux

## Trier de manière naturelle : les algorithmes naïfs

!!! question "Trier à la main"
	On donne une main de 5 cartes d'un jeu de 54 cartes. Trier les cartes par ordre croissant, sans tenir compte des couleurs. Vous devrez marquer dans le tableau suivant l'ensemble des changements de positions des cartes dans votre main :
\begin{center}
\begin{tikzpicture}[scale = 1.5]
\foreach \y in {0,1,2,3,4}{
	\foreach \x in {0,1,2,3,4}{
		\draw (1.2*\x,1.6*\y) rectangle (1.2*\x+1,1.6*\y+1.4);
	}

}

\end{tikzpicture}
\end{center}
Avez-vous tous utilisé la même méthode ?
\caserep{\linewidth}{2}
\end{Activite}
\pagebreak

\section{Le tri par insertion}
\subsection{Exemple}
On veut trier le tableau `[6, 5, 3, 1, 8, 7, 2, 4]}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\foreach \y in {-7,-6,...,0}{
	\pgfmathsetmacro{\z}{int(\y*(-1))}%
	\node () at (-1,2.4*\y+0.5) {$i = \z$};
	\draw (-1.2,2.4*\y-1) rectangle (-0.2,2.4*\y-1+1);
	\foreach \x in {0,1,...,7}{
		\draw (1.2*\x,1.2*\y*2) rectangle (1.2*\x +1, 1.2*\y*2+1);
	}
	
}

\end{tikzpicture}
\end{center}
\subsection{Algorithme en pseudo-code et complexité}
\begin{info}{Tri par insertion}

\vspace{6cm}

\end{info}
\section{Le tri par sélection}
\subsection{Exemple}
On veut trier le tableau `[6, 5, 3, 1, 8, 7, 2, 4]}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\foreach \y in {-7,-6,...,0}{
	\pgfmathsetmacro{\z}{int(\y*(-1))}%
	\node () at (-1,2.4*\y+0.5) {$i = \z$};
	\draw (-1.2,2.4*\y-1) rectangle (-0.2,2.4*\y-1+1);
	\foreach \x in {0,1,...,7}{
		\draw (1.2*\x,1.2*\y*2) rectangle (1.2*\x +1, 1.2*\y*2+1);
	}
	
}

\end{tikzpicture}
\end{center}
\subsection{Algorithme en pseudo-code et complexité}
\begin{info}{Tri par insertion}

\vspace{6cm}

\end{info}
\section{Un autre algorithme de tri : le tri à bulle}
L'algorithme de tri à bulles consiste à trier la liste en n'autorisant qu'à intervertir deux éléments consécutifs de la liste. On peut le décrire comme ceci:
\begin{info}{Tri à bulle}
\begin{enumerate}
\item Parcourir le tableau et comparer les éléments consécutifs. Lorsque deux éléments sont dans le désordre, les inverser.
\item Une fois la fin du tableau, recommencer.
\item S'arrêter dès qu'un parcours du tableau n'a échangé aucun élément.
\end{enumerate}
\end{info}
Effectuer le tri à bulle du tableau `[5, 1, 4, 2, 8]}
\begin{center}
\begin{tikzpicture}[scale=0.7]
\foreach \y in {-10,-9,...,0}{

	\foreach \x in {0,1,...,4}{
		\draw (1.2*\x,1.2*\y*2) rectangle (1.2*\x +1, 1.2*\y*2+1);
	}
	
}

\end{tikzpicture}
\end{center}
\end{document}
