<h1> <font color="red">Débuter avec </font></h1>

![logo Python](python-logo.png)


<h2><font color="blue">I : Types de base </font></h2>

<h3><font color="green">a : Objets et types de base</font></h3>

En Python, tout est objet. par exemple, dans la cellule suivante :


```python
5
"Toto"
True
4.5 # Attention, il s'agit de la notation américaine, donc pas de virgule mais un point...
```




    4.5



on a crée 4 objets différents, présents dans ce qu'on appelle l'**espace des objets**. En déclenchant la cellule précédente ( *CTRL+Entrée*), on obtient cependant que l'affichage de `4.5`. En effet, un mécanisme existant dans tous les langages de programmation, appelé **garbage collector** ( soit *collecteur d'ordure*), nettoie tout objet non utilisé. La mémoire de l'ordinateur étant limitée physiquement, il est nécessaire de nettoyer très régulièrement ( plusieurs centaines de fois par seconde) cette mémoire afin de garantir le bon fonctionnement de la machine. Le garbage collector a donc supprimé les objets `5`, `"Toto"` et `True`.

Regardons plus précisemment ces objets, en demandant à Python grâce aux instructions **built-in** `print()` et `type()` la nature des objets crées (vous pouvez éditer, modifier, compléter à loisir les cellules IPython ci-dessous ):


```python
 print(type("toto"))
```

    <class 'str'>


Les types basiques de Python sont donc les suivants :
* le type `int` : qui permet de manipuler des nombres entiers relatifs, de $-2.10^{9}$ à $+2.10^9$, mais la plage pouvant être étendus ;
* le type `float` : qui permet de manipuler des nombres décimaux à $32$ bits entre $-10^{302}$ et $+10^{302}$;
* le type `str` : qui permet de manipuler des chaînes de caractères ;
* le type `bool` : qui permet de manipuler des valeurs **booléennes**, c'est à dire vraies ou fausses, utilisées par défaut dans les intsructions nécessitant une condition (`if` ou `while` par exemple).

Chacun de ces types possède des opérations qui lui sont propres. Elles sont nombreuses, et largement documentées dans la doc Python 3 officielle, en suivant le lien ci contre : [Doc Python 3.6 en français](https://docs.python.org/fr/3.6/) ( La dernière version de Python est la 3.8, mais les notebooks Jupyter ne fonctionnent ici qu'en Python 3.6. Certaines fonctionnalités de la dernière version de Python ne sont donc pas accessibles, mais pour la majorité des cas nous pourrons travailler correctemnt ).

Il existe aussi des *constantes* spécifiques, c'est-à-dire des objets spéciaux, comme par exemple `None`, qui est une valeur signifiant l'absence de type.

<h3><font color="green">b : Nommage des objets et affectations</font></h3>

Bien entendu, de manière quasi obligatoire, il est nécessaire de conserver des objets et d'éviter que ceux-ci disparaissent avec le **garbage collector**.

Pour cela, on va associer à chaque objet un **nom** dans l'**espace de nom**, grâce à l'opération d'**affectation** `=`.


```python
nombreEntier = 5
leVraiHero = "Dark"
print1 = True
```


```python
print(type(5))
```

    <class 'int'>



```python
5 == 2+2
```




    False



Pour mieux comprendre les mécanismes d'affectation, voici la [vidéo de ce lien](https://video.toutatice.fr/video_priv/23382/4a499fd39c4aeea48eb7fd51a53f853b803e761925f5b7f6e737e3430177f86d/).

Le nom donné à l'objet peut être n'importe lequel, en respectant les règles **impératives** suivantes :
* Un nom de variable est une séquence de lettres, de chiffres, qui ne doit pas commencer par un chiffre.
* La **casse est significative** (les caractères majuscules et minuscules sont distingués). Donc `Joseph`, `joseph`, et `JOSEPH` sont des variables différentes.
* Les **« mots réservés »** du langage sont déjà pris (ex : `print()`). Il s'agit des instructions de bases et des fonctions natives ( voir [ici](https://docs.python.org/fr/3/library/functions.html) ). Si vous nommez une variable comme un de ces mots, vous ne pourrez plus utiliser la fonctionnalité du mot réservé. Pour la liste des mots réservés : 
  
Il faut également noter que les variables dont le nom commence par le caractère `_` ont une signification particulière :
* les noms commençant par un `_` ne sont pas exportés lorsqu'ils se trouvent dans un module ;
* les noms commençant par deux `_` et finissant par deux `_` sont réservés par le langage lui même, notamment pour la programmation orientée objet.

Ces deux points ci-dessus sont juste des indications pour l'instant, ils seront vu dans le futur, en particulier en terminale.

Il existe quelques règles de "bien nommage" des variables :
*  il est recommandé d'écrire les noms de variables avec une minuscule, car l'usage veut qu'on le réserve plutôt la majuscule aux noms de classes ou aux constantes ;
* Si le nom d'une variable doit comporter plusieurs mots, il y a deux possibilités d'écrire le nom de la variable :
    * En **snake_case** (à la C), c'est à dire en séparant les mots par le caractère `_`. Exemple : `marge_brut`.
    * En **camelCase** (à la Java), c'est à dire en séparant les mots par un passage en haut de casse (lettre majuscule). Exemple : `margeBrut`.
* Il convient aussi d'éviter autant que possible l'énumération de variables (`toto1`, `toto2`, `toto3`, ...), cela rend le programme parfaitement incompréhensible et sujet à des erreurs.
* De manière générale, il convient de suivre aussi strictement que possible les règles édictées par la **Python Software Foundation** à travers les normes PEP, dont la dernière en date est disponible ici : [PEP8](https://www.python.org/dev/peps/pep-0008/)

Une fois l'affectation réalisée, les objets sont donc récupérables grâce à leur nom, ils sont protégés du **garbage collector** et on peut effectuer des actions sur ces objets :


```python
nombreEntier**2
```




    25




```python
leVraiHero+"Vador"
```




    'DarkVador'




```python
not(print)
```

<h4><font color="blue">Exercices</font></h4>

1. Ecrire un code qui affecte l'objet `15` de type `int`  à une variable nommé ``valeur``, puis exécuter l'instruction ``valeur*4``.


```python
valeur = 15
valeur * 4
```

2. Ecrire un code qui affecte l'objet `"15"` de type `str`  à une variable nommé ``texte``, puis exécuter l'instruction ``texte*4``.


```python

```

3. Ecrivez un code qui crée 3 variables `A,B` et `C`, et leur affecte les valeurs entières respectives 10, 20, 400.


```python
A,B,C = 10, 20, 400
```

4. Ecrivez un code qui **permute** les contenus des variables `A` et `B` **sans utiliser de valeurs numériques**.


```python

```

5. Ecrivez un code qui **permute** les contenus des variables `A`, `B` et `C` ( le contenu de `A` est affecté à `B`, le contenu de `B` est affecté à `C` et le contenu de `C` est affecté à `A`) **sans utiliser de valeurs numériques**.


```python
D = C
C = B
B = A
A = D
```


```python
print(A, B, C)
```

    20 400 10


<h3><font color="green">c : Types numériques et opérations</font></h3>

Pour les types numériques, `int` et `float` (et pour le type `complex`, mais qui n'est pas vu en maths avant la terminale ), on trouve toutes les opérations classiques :


```python
5 + 2 #Addition entière
```




    7




```python
5.6 + 3.4 # Addition flottante ( Quel est le type du résultat ?)
```




    9.0




```python
5 + 3.4 # Addition entre un entier et un flottant ( Quel est le type du résultat ?)
```




    8.4




```python
0.1+0.2 == 0.3
```




    False




```python
3.2-4 #Soustraction ( A tester de la même manière)
```




    -0.7999999999999998




```python
4*8.5 #Multiplication ( idem)
```




    34.0




```python
1/3 #Division
```




    0.3333333333333333



Attention ! Au résultat ci-dessus, le type obtenu est `float`, même si le dividende et le diviseur dont entiers et que résultat "tombe juste"... (A tester...)


```python
72//5 #Quotient de la division euclidienne
```




    14



Ici par contre le résultat est bien de type `int` (A tester aussi...)


```python
72%5 #reste de la division euclidienne ( ou modulo).
```




    2




```python
23%2 == 0 # Pour savoir si un nombre est pair par exemple
```




    False




```python
10**7 #Puissance
```




    10000000



<h3><font color="green">d : Types `str` ( chaines de caractères ) et opérations</font></h3>

Chaque caractère d'une chaîne est repéré par son **index**, c'est-à-dire par un **numéro donnant sa position**. Attention toutefois,en informatique, les index commencent à 0 dans quasiment tous les langages !
Ainsi :
    ![image stanford](https://web.stanford.edu/class/archive/cs/cs106a/cs106a.1204/handouts/python-str-index.png)
    
Dans la chaïne précédente, ``P`` à pour indice 0, ``y`` a pour indice 1 et ``n`` a pour indice 5.
La longueur de la chaîne ``Python`` est par contre bien de 6, et on peut y accéder grâce à la fonction **built-in** ``len()``.



```python
"Abcdefg"[10]#Accès direct à un caractère par son index.
```

    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    IndexError: string index out of range



```python
len("aeiouy")
```




    6



Le type `str` possède lui aussi ses propres opérations ( ou **méthodes**) qui permettent de transformer ou modifier une chaine de caractère. Parmi celles-ci, en voici quelques une utiles :


```python
"Toto"+"Tata" #Concaténation
```




    'TotoTata'




```python
"Toto"*5
```




    'TotoTotoTotoTotoToto'




```python
"Toto".replace("o","&&&12") #Substitution, en utilisant le point (.) pour accéder aux méthodes de classe.
```




    'T&&&12t&&&12'




```python
"Toto".lower() #mise en minuscule, appel encore une fois à une méthode de classe.
```




    'toto'




```python
"Toto".upper() #mise en majuscule, idem
```




    'TOTO'




```python
"une phrase SANS QUEUE ni tÊte.".capitalize()
#Met en majuscule le premier caractère de la chaine, et en minuscule les autres, idem
```




    'Une phrase sans queue ni tête.'




```python
"              Des Blancs            ".strip()
# Supprime les espaces inutiles devant et après une chaine de caractères
```




    'Des Blancs'




```python
"Une phrase est faite avec des mots".split("est")
#Sépare  une chaine de caractère en, fonction d'un caractère passé en argument ( ici le caractère espace " ")
# renvoie une liste
```




    ['Une phrase ', ' faite avec des mots']




```python
#On peut aussi passer un autre caractère, par exemple :
"12:34:45:78".split(":")
```




    ['12', '34', '45', '78']



Il existe aussi la fonction **built-in** `len()` qui donne la longueur de la chaîne de caractères.

<h2><font color="blue">II : Interactions avec l'utilisateur, transtypage des données, notions de formatage des chaines de caractères</font></h2>

Pour demander une saise clavier à un utilisateur, on utilise la fonction **built-in** `input()`, prenant éventuellement en **argument**  une chaîne de caractères. Celle-ci interrompt le programme et attend une saise clavier de l'utilisateur, et retourne cette saisie sous la forme d'une chaîne de caractère.

Pour afficher le contenu d'une variable, ou une chaîne de caractère, on utilise la fonction **built-in** `print()`.


```python
a=input("Entrez votre nom :")
print(a)
```

    Entrez votre nom :tutu
    tutu


Il faut cependant être attentif à ce qui est réalisé par la  fonction `input()`. En effet, le **retour** effectué par cette fonction est renvoyé sous la forme de chaîne de caractères, ce qui peut poser un problème, comme par exemple dans la situation ci-dessous :


```python
nb = input("Entrez un nombre entier :")
print(type(nb))
print(2*nb)
```

    Entrez un nombre entier :dfghlqjkdghlkqfghqd
    <class 'str'>
    dfghlqjkdghlkqfghqddfghlqjkdghlkqfghqd


Pour lever cette ambiguïté, nous sommes parfois obligés d'effectuer un **transtypage** des données, avec l'aide des fonctions **built-in** suivantes :
* `str()`
* `int()`
* `float()`
* ...

En modifiant l'exemple ci-dessus :



```python
 A = "15"
```


```python
type(A)
```




    <class 'str'>




```python
B = float(A)
```


```python
type(B)
```




    <class 'float'>




```python
B
```




    15.0




```python
str(-15.2).split(".")
```




    ['-15', '2']




```python
nb=input("Entrez un nombre entier :")
print(2*float(nb))
type (nb)
```

on a forcé ici dans la deuxième ligne Python à considérer le contenu de la variable `nb` comme étant un nombre entier.
Ceci ne lève cependant pas tous les problèmes, puisque si l'utilisateur saisis une chaîne de caractères ne pouvant être transtypée en nombre entier, le programme renverra une erreur.

Il est à noter qu'une solution plus élégante serait  de transtyper dès la saisie :


```python
nb=float(input("Entrez un nombre entier :"))
print(nb)
type(nb)
```

    Entrez un nombre entier :157
    157.0





    <class 'float'>



Essayez le code suivant :


```python
nom=input("Saisissez votre nom :")
prenom=input("Saisissez votre nom :")
print("Votre nom de famille est {a} et votre prénom est {b}".format(a=nom.upper(),b=prenom.capitalize()))
```

    Saisissez votre nom :toto
    Saisissez votre nom :TATA
    Votre nom de famille est TOTO et votre prénom est Tata


Dans la chaïne de caractère `"Votre nom..."`, on a inséré **entre accolades** deux variables `a` et `b`, qui ont été substituées grâce à la **méthode** `format()`, spécifique aux chaînes de caractères. Cette méthode est très utile pour obtenir des messages clairs pour les utilisateurs.

La méthode précédente peut-être améliorée grâce aux **f-string** depuis Python 3.6 :


```python
nom=input("Saisissez votre nom :")
prenom=input("Saisissez votre nom :")
print(f"Votre nom de famille est {nom.upper()} et votre prénom est {prenom.capitalize()}")
```

<h4><font color="blue">Exercice</font></h4>

Ecrire dans la cellule suivante un code python qui :
* demande deux nombres à l'utilisateur ;
* donne le produit des deux nombres, ainsi que le type du résultat, sous la forme d'une chaine de caractères dy type `3x4 = 12 Le résultat est de type int`.                                                                                                                             


```python

```
