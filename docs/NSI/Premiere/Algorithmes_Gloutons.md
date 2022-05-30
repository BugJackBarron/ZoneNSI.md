# Algorithmes Gloutons


*D'après [pixees.fr](pixees.fr){: target="_blank"}*

\section{Problèmes d'optimisations}
\subsection{Le problème}
\begin{Activite}{Le problème du sac à dos}
\noindent Un cambrioleur possède un sac à dos d'une contenance maximum de 30 Kg. Au cours d'un de ses cambriolages, il a la possibilité de dérober 4 objets A, B, C et D. Voici un tableau qui résume les caractéristiques de ces objets : 
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline 
Objet & A & B & C & D \\ 
\hline 
Masse & 13 Kg & 12 Kg & 8 Kg & 10 Kg \\ 
\hline 
Valeur & 700 € & 400 € & 300  € & 300 € \\ 
\hline 
\end{tabular} 
\end{center}
\begin{enumerate}
\item Déterminez les objets que le cambrioleur aura intérêt à dérober, sachant que :
 \trianglenoir
\begin{itemize}
\item tous les objets dérobés devront tenir dans le sac à dos (30 Kg maxi) ;
\item le cambrioleur cherche à obtenir un gain maximum.
\end{itemize}
\caserep{\linewidth}{2}
\item Existe-t-il d'autres solutions ?
\caserep{\linewidth}{2}
\end{enumerate}
\end{Activite}
\begin{definition}{Optimisation}
Ce genre de problème est un grand classique en informatique, on parle de \textbf{problème d'optimisation}. Il existe toujours plusieurs solutions possibles à un problème d'optimisation, mais toutes ne sont pas équivalentes.Mais on cherche une \textbf{solution dite optimale} (dans notre exemple on cherche le plus grand gain possible). Souvent, dans les problèmes d'optimisation, il n'existe pas une solution optimale, mais plusieurs solutions optimales, et  résoudre un problème d'optimisation c'est donc trouver une des solutions optimales. 
\end{definition}
\begin{info}{Solution naïve}
En apparence, la solution la plus simple dans le cas du sac à dos serait d'écrire un algorithme qui teste toutes les combinaisons d'objets possibles et qui retient les solutions qui offrent un gain maximum. Dans notre cas précis, avec seulement 4 objets, cette solution pourrait être envisagée, mais avec un plus grand nombre d'objets, le temps de calculs, même pour un ordinateur très puissant, deviendrait trop important. En effet l'algorithme qui testerait toutes les combinaisons possibles aurait une complexité en temps en $\mathrm{O}(a^n)$ avec $a$ une constante et $n$ le nombre d'objets. On parle dans ce cas d'une \textbf{complexité exponentielle}. Les algorithmes à complexité exponentielle ne sont pas efficaces pour résoudre des problèmes, le temps de calcul devient beaucoup trop important quand $n$ devient très grand. 
\end{info}

\subsection{Une solution \og gloutonne\fg}

\begin{info}{Solution \og Gloutonne \fg}
\noindent La résolution d'un problème d'optimisation se fait généralement par étapes : à chaque étape on doit \textbf{faire un choix}. Par exemple, dans le problème du sac à dos, nous ajoutons les objets un par un, chaque ajout d'un objet constitue une étape : à chaque étape on doit \textbf{choisir} un objet à mettre dans le sac. Le principe de la méthode \textbf{gloutonne}(\emph{greedy} en anglais) est de, à chaque étape de la résolution du problème, faire le choix qui semble \emph{le plus pertinent} sur le moment, avec l'espoir qu'au bout du compte, cela nous conduira vers une solution optimale du problème à résoudre. Autrement dit, on fait des \textbf{choix localement optimaux}(ici, cela signifie à chaque étape on fait le choix qui semble le plus pertinent) dans l'espoir que ces choix mèneront à une solution globalement optimale. 
\end{info}
\begin{Activite}{Méthode gloutonne}
Comme on cherche à optimiser au maximum le gain, on va s'intéresser à la \og valeur massique\fg de chaque objet.
\begin{enumerate}
\item Compléter le tableau suivant :
\begin{center}
\begin{tabular}{|c|c|c|c|c|}
\hline 
Objet & A & B & C & D \\ 
\hline 
Valeur Massique (en €/Kg)\rule{0cm}{1cm} & \rule{1cm}{0cm} & \rule{1cm}{0cm} & \rule{1cm}{0cm} & \rule{1cm}{0cm}   \\\hline
\end{tabular} 
\end{center}
\item Trier le tableau par valeur décroissante de la valeur massique.
\item Enfin, on remplit le sac en prenant les objets dans l'ordre et en s'arrêtant dès que la masse limite est atteinte.\\
\item Quelle est la composition du sac ?
\caserep{\linewidth}{1}
\item Est-elle optimale ?
\caserep{\linewidth}{1}
\end{enumerate}
\end{Activite}
\begin{Exercice}
La liste des objets et leur poids est donné par un dictionnaire nom : (masse; valeur).
\begin{enumerate}
\item Ecrire une fonction Python qui renvoie un taleau de tuples (nom ; valeur massique) à partir du dictionnaire passé en argument.
\item Trier ce tableau par ordre décroissant des valeurs massiques.
\item Ecrire une fonction Python qui finalise l'algorithme glouton.
\end{enumerate}
\end{Exercice}
\section{Problème du rendu de monnaie}
\subsection{La situation}
\begin{info}{Le problème du rendu de monnaie}
\noindent Nous sommes des commerçants, nous avons à notre disposition un nombre illimité de pièces de : 
\coche
\begin{itemize}
\item 1 centime
\item 2 centimes
\item 5 centimes
\item 10 centimes
\item 20 centimes
\item 50 centimes
\item 1 euro
\item 2 euros
\end{itemize}
Nous devons rendre la monnaie à un client à l'aide de ces pièces. La contrainte est d'utiliser le moins de pièces possible. 
\end{info}
\begin{Activite}{L'algorithme}
\begin{enumerate}
\item Trouvez une méthode gloutonne permettant d'effectuer un rendu de monnaie (en utilisant le moins possible de pièces).
\caserep{\linewidth}{7}

\item Vous devez rendre la somme de 2,63 €, appliquez la méthode que vous venez de mettre au point.
\caserep{\linewidth}{3}
\item Combien de pièces avez-vous utilisées ? 
\caserep{\linewidth}{1}
\item La solution trouvée est-elle optimale ?
\caserep{\linewidth}{1}
\end{enumerate}
\end{Activite}
\subsection{Le code}
À partir de la méthode gloutonne que vous avez élaborée ci-dessus, écrivez un algorithme glouton qui permettra de déterminer le nombre minimal de pièces à utiliser pour une somme donnée. Vous proposerez ensuite une implémentation en Python de votre algorithme. Vous testerez votre programme avec une somme à rendre de 2 euros et 63 centimes. 
\end{document}
