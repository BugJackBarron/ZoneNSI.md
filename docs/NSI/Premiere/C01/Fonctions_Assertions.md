# Fonctions, assertions et docstring en  ![logo Python](python-logo.png)


## Premiers pas avec les fonctions

### Pourquoi des fonctions ?

Dans la partie précédente, nous avons terminé par un petit programme qu demande à un·e utilisateur·trice de donner un nombre entier entre 1 et 10, et qui vérifie la saisie jusqu'à ce que l'utilisateur·trice ait effectuer une saisie correcte. Voici un exemple simple d'implémentation de ce programme :

{{ IDEv('askIntV1') }}

!!! question "Un blocage ?"

    === "Enoncé"
        Essayez de saisir différentes valeurs **de différents types**. Quel est le problème rencontré ?

    === "Solution"
        Si 'utilisateur·trice saisi quelque chose qui ne peut pas être **transtypé** en `int`, il y a une erreur levée et le programme est totalement interrompu. Ce peut-être parfois complètement bloquant pour le fonctionnement réel d'une application.

        La version ci-dessous est un peu plus *dumbproof*, mais je ne vous demande pas encore de comprendre les blocs `try/except/else`.

        {{ IDEv('askIntV2') }}


!!! questoin "Multiplier les codes"


    === "Enoncé"

        Imaginons maintenant un programme qui demande **trois fois** à l'utilisateur d'entrer un tel nombre, puis qui vérifie si les trois nombres correspondent à une configuration de Pythagore.

        Vous devez vous inspirer du programme précédent pour compléter le programme ci-dessous afin d'obtenir trois nombres entiers `nb1`, `nb2` et `nb3` saisis par l'utilisateur :

    === "Solution"

        Un code pouvant être inséré (avec notre niveau actuel en Python et sans utiliser de structures de listes) est le suivant :

        ```` python
        while True :
            nb1 = input("Entrez un nombre entier entre 1 et 10 : ")
            try :
                nb1 = int(nb1)
            except ValueError :
                print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
            else :
                if 1<= nb1= 10 :
                    break
                else :
                    print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
        while True :
            nb2 = input("Entrez un nombre entier entre 1 et 10 : ")
            try :
                nb2 = int(nb2)
            except ValueError :
                print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
            else :
                if 1<= nb2 <= 10 :
                    break
                else :
                    print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
        while True :
            nb3 = input("Entrez un nombre entier entre 1 et 10 : ")
            try :
                nb3 = int(nb3)
            except ValueError :
                print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
            else :
                if 1<= nb3 <= 10 :
                    break
                else :
                    print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
        ````


    {{ IDEv('ask3Int') }}





!!! warning "Mauvaise pratique"
    Si ce code fait le travail demandé, il n'en est pas moins de *mauvaise qualité* pour plusieurs raisons :

    * Il est long, avec des répétitions. Plus un code est long, plus il prend de place en mémoire, alors qu'on cherche plutôt à minimiser ce facteur.
    * Le copié-collé force quand même à repasser sur chacune des parties pour modifier le nom des variables (sinon les valeurs seraient écrasées). Ainsi toute modification doit être **réécrite à chaque fois** que le morceau de code est appelé. Dans notre exemple, ce n'est que trois fois, le risque d'erreurs est minime, mais pour un plus grand nombre de répétitions, il est très facile d'oublier une modification.
    * Le code n'est plus lisible. Dans le cas d'un travail en équipe, il est impératif d'avoir un code clairement écrit, avec des fonctionnalités clairement définies.

### Première fonction

#### Définition d'une fonction

On va donc améliorer non seulement la lisibilité de notre code, mais aussi son efficacité et sa simplicité, en utilisant une **fonction**.

!!! abstract "Définition : fonction"
    Une {==**fonction**==} est un bloc de code nommé (c'est-à-dire possédant un nom dans l'espace de noms, comme toute autre variable). L'appel par l'interpréteur du nom de la fonction {==**suivi d'une paire de parenthèses**==} exécutera alors l'intégralité du code et renverra une **valeur de retour**.

Pour notre exemple :

{{ IDEv('askIntFctV1') }}

La fonction est introduite par le mot clé `def`, suivi du **nom de la fonction** puis d'un couple de parenthèses `()`, ce qui rend l'objet *callable* ( "appelable"). Le bloc de code est ensuite défini grâce à une indentation en dessous du nom, tout comme on définit des blocs dans des structures conditionnelles ou des boucles.

On fait appel  à cette fonction en appelant le nom `askUserInt()`, ce qui déclenche le bloc de code, puis crée un objet de retour correspondant à la valeur saisie par l'utilisateur.

!!! warning "Oubli des parenthèses"

    Dans le cas d'un oubli des parenthèses lorsqu'on appelle une fonction, on obtient dans le terminal le message suivant :

    ```` python
    >>> askUserInt
    <function askUserInt at 0xe8c1a0>
    ````

    Qui signifie simplement que le nom `askUserInt` fait référence à une fonction dont l'adresse mémoire est donnée sous forme hexadécimale.

    Notez que `askUserInt` est juste un nom, l'objet correspondant est stocké dans l'espace des objets. On peut donc écrire les choses suivantes :

    ```python
    >>> demandeEntier=askUserInt
    >>> demandeEntier()
    ```


#### Utilisation de la valeur de retour

Comme tout objet, la valeur de retour d'une fonction doit elle même être stockée dans une variableafin de ne pas être ramassée par le *garbage collector* :

```python
>>> entier=askUserInt()
>>> print(f'La racine carrée du nombre {entier} est {entier**(1/2)}')
```


#### Factorisation du code de Pythagore

Le code du programme de vérification de Pythagore peut alors être {==**factorisé**==}, et devient alors :


{{ IDEv('askIntFctV2') }}

Ce qui a l'avantage d'être vraiment vraiment plus clair.

### Exercices

!!! question "Exercices"

    === "Enoncé"

        Créer une fonction nommée `table7` qui **renvoie** la table de multiplication de 7 avec un multiplicateur allant de 0 à 10, sous la forme d'une chaîne de caractères comme ci-dessous :

        ``` 
        "7x0=0 \n 7x1=7 \n 7x2=14 ..."
        ```

        **Indication :** le symbole `\n`, insère un saut de ligne dans une chaîne de caractères.

    === "Solution"

        ``` python
        def table7() :
            table = ''
            for i in range(11) :
                table += f'7x{i} = {7*i} \n'
            return table
        ```

<h3><font color="green">c : Augmenter la capacité des fonctions : les arguments obligatoires </font></h3>

L'exemple de la fonction `askUserInt` est assez limité. Dans l'absolu, on pourrait souhaiter que la fonction demande un nombre entier entre 2 valeurs variables.

Pour ce faire, il faut, dans la définition de la fonction, préciser des **arguments** qui seront des noms spécifiques de variables :


```python
def askUserInt(borne_min,borne_max) :
    if not(isinstance(borne_min,int)) or not(isinstance(borne_max,int)) :
        raise ValueError("One or both of the arguments are not of type int")
    if borne_min>borne_max :
        raise ValueError("First argument must be lesser or equal to second argument")
    while True :
        nb = input(f"Entrez un nombre entier entre {borne_min} et {borne_max} : ")
        try :
            nb=int(nb)
        except ValueError :
            print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if borne_min<= nb<= borne_max :
                break
            else :
                print(f"Votre nombre n'est pas compris entre {borne_min} et {borne_max}. Veuillez recommencer !")
    return nb    
```

Une fois la fonction définie, on peut l'appeler en précisant les vaaleurs des deux arguments :


```python
askUserInt(1,100)
```


```python
askUserInt(-10,10)
```

On a aussi un certain nombre d'erreurs qui sont déclenchées. Testez les lignes suivantes :


```python
askUserInt()
```


```python
askUserInt(45)
```


```python
askUserInt(0.5,2.5)
```


```python
askUserInt(30,10)
```

<h4><font color="blue">Application 3 : </font></h4>

Créer une fonction `tableMulti` qui prend un argument entier, le multiplicande, et écrit la table de multiplication de ce nombre, avec un multiplicateur allant de 1 à 10.


```python

```

<h4><font color="blue">Application 4 : </font></h4>

Créer une fonction `trouveChaine`qui prend deux arguments, un `motif` ( une chaine de caractères ) et un `texte` ( une autre chaine de caractères )  et qui renvoie `True` si le `motif` est présent dans la `chaine`, quel que soit la casse du motif ou celle de la chaine, et `False` sinon. Vous pouvez tester avec la cellule suivant votre code :


```python
def trouveChaine(motif,texte) :
    ####ECRIVEZ VOTRE CODE ICI, 
    ## en remplaçant l'expression retuen par votre propre code
    return -1
```


```python
### Cette cellule est une cellule vous permettant de tester votre fonction
assert trouveChaine('Toto', 'Toto va à la plage')==True, 'Meme casse pas trouvée'
assert trouveChaine('Totos', 'Toto va à la plage')==False, 'Chaine non présente trouvée'
assert trouveChaine('TOTO', 'Toto va à la plage')==True, 'Problème de majuscules dans le motif'
assert trouveChaine('toto', 'TOTO va à la plage')==True, 'Problème de minuscules dans le motif'
assert trouveChaine('ToTo', 'OtOtO va à la plage')==True, 'Que dire ?'
```

<h3><font color="green">d : Augmenter la capacité des fonctions : les arguments optionnels </font></h3>

Notre fonction `askUserInt` commence à être intéressante. Mais nous pourrions souhaiter personnaliser le message de la question, sans pour autant avoir envie de le changer systématiquement.
C'est tout à fait possible en Python, grâce aux **arguments optionnels**. Il s'agit d'arguments dont le nom est donné dans la fonction, mais avec **une valeur par défaut**. Ainsi :


```python
def askUserInt(borne_min,borne_max, prenom='Inconnu') :
    if not(isinstance(borne_min,int)) or not(isinstance(borne_max,int)) :
        raise ValueError("One or both of the arguments are not of type int")
    if borne_min>borne_max :
        raise ValueError("First argument must be lesser or equal to second argument")
    while True :
        nb = input(f"{prenom}, entrez un nombre entier entre {borne_min} et {borne_max} : ")
        try :
            nb=int(nb)
        except ValueError :
            print(f"{Inconnu}, vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if borne_min<= nb<= borne_max :
                break
            else :
                print(f"{Inconnu}, votre nombre n'est pas compris entre {borne_min} et {borne_max}. Veuillez recommencer !")
    return nb    
```

Ainsi, la fonction ci-dessus posssède trois arguments :
* deux arguments **obligatoires**, `borne_min` et `borne_max` ;
* un argument **optionnel**, `prenom`.



Il est à noter qu'impérativement les **arguments obligatoires doivent être placés avant les arguments optionnels**.

On peut alors appeller la fonction des différentes manières suivantes :


```python
askUserInt(0,10)
```


```python
askUserInt(0,10,prenom='Toto')
```


```python
askUserInt(0,10,prenom='foo')
```

<h4><font color="blue">Application 5 : </font></h4>

Compléter la fonction `tableMulti` afin qu'elle utilise deux arguments optionnels, la valeur de départ et la valeur d'arrivée du multiplicateur :


```python

```

<h4><font color="blue">Application 6 : </font></h4>

Réécrire la fonction `trouveChaine` afin qu'elle utilise un *argument booléen optionnel* `verifCasse`, afin de déterminer si le `motif` est présent dans le `texte` en vérifiant la casse ou non. Par défaut l'argument sera `False`


```python
def trouveChaine(motif,texte,verifCasse=False) :
    if verifCasse==True :
        if motif in texte :            
            return True
        else :
            return False
    else :
        if  motif.lower() in texte.lower() :
            return True
        else :
            return False
        
```


```python
### Cette cellule est une cellule vous permettant de tester votre fonction
##les assertions suivantes sont les même que précédemment
assert trouveChaine('Toto', 'Toto va à la plage')==True, 'Meme casse pas trouvée'
assert trouveChaine('Totos', 'Toto va à la plage')==False, 'Chaine non présente trouvée'
assert trouveChaine('TOTO', 'Toto va à la plage')==True, 'Problème de majuscules dans le motif'
assert trouveChaine('toto', 'TOTO va à la plage')==True, 'Problème de minuscules dans le motif'
assert trouveChaine('ToTo', 'OtOtO va à la plage')==True, 'Que dire ?'
# Mais on rajoute celles-ci :
assert trouveChaine('Toto', 'Toto va à la plage',verifCasse = True )==True, 'Meme casse pas trouvée'
assert trouveChaine('TOTO', 'TOTO va à la plage',verifCasse = True )==True, 'Meme casse pas trouvée'
assert trouveChaine('Totos', 'Toto va à la plage',verifCasse = True)==False, 'Chaine non présente trouvée'
assert trouveChaine('TOTO', 'Toto va à la plage',verifCasse = True)==False, 'Problème de majuscules dans le motif'
assert trouveChaine('toto', 'TOTO va à la plage',verifCasse = True)==False, 'Problème de minuscules dans le motif'
assert trouveChaine('ToTo', 'OtOtO va à la plage',verifCasse = True)==False, 'Que dire ?'
```

<h2><font color="blue">II : Portée des variables  </font></h2>

Au sein d'un même programme, ou bien d'un même notebook, les variables définies n'ont pas la même **portée**. La **portée d'une variable**, c'est l'espace dans lequel est défini cette variable.

Essayons les deux cellules suivantes :


```python
gvar = 8
def f() :
    print(f"Dans la fonction, la variable gvar vaut {gvar}")

f()
print(f"En dehors de la fonction, la variable gvar vaut {gvar}")
```

    Dans la fonction, la variable gvar vaut 8
    En dehors de la fonction, la variable gvar vaut 8



```python
def f() :
    gvar2 = 8
    print(f"Dans la fonction, la variable gvar2 vaut {gvar2}")

f()
print(f"En dehors de la fonction, la variable gvar2 vaut {gvar2}")
```

    Dans la fonction, la variable gvar2 vaut 8



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-9a775bf5b042> in <module>
          4 
          5 f()
    ----> 6 print(f"En dehors de la fonction, la variable gvar2 vaut {gvar2}")
    

    NameError: name 'gvar2' is not defined


* Dans le premier exemple, la variable `gvar` est définie **en dehors de la fonction**. Sa valeur est cependant accessible **dans la fonction**.
* Dans le deuxième exemple, la variable `gvar2` est définie uniquement **dans la fonction**. sa valeur est **inaccessible en dehors de cette fonction**. On voit une erreur `NameError` apparaître.

Regardons maintenant le code suivant :


```python
gvar= 10
def f() :
    gvar=gvar+2
    print(f"Dans la fonction, la variable gvar vaut {gvar}")

f()
print(f"En dehors de la fonction, la variable gvar vaut {gvar}")
```


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-9-836b31058de9> in <module>
          4     print(f"Dans la fonction, la variable gvar vaut {gvar}")
          5 
    ----> 6 f()
          7 print(f"En dehors de la fonction, la variable gvar vaut {gvar}")


    <ipython-input-9-836b31058de9> in f()
          1 gvar= 10
          2 def f() :
    ----> 3     gvar=gvar+2
          4     print(f"Dans la fonction, la variable gvar vaut {gvar}")
          5 


    UnboundLocalError: local variable 'gvar' referenced before assignment


Le déclenchement de la cellule précédente déclenche une erreur `UnboundLocalError` en ligne 3. Cela signifie que l'interpréteur Python ne peut pas effectuer la ligne `gvar=gvar+2` car il cherche une variable `gvar` qu'il peut modifier. Or une variable définie hors d'une fonction **ne peut pas être modifiée par celle-ci**.
Par contre on peut passer la référence à cette variable par l'intermédiaire d'un argument. Il faudra alors *retourner la valeur changée* pour qu'elle soit effective. Par exemple comparez les deux scripts suivants :


```python
a=10
print(f"Avant la fonction, a={a}")
def f(a) :
    #print(f"Dans la fonction, avant modification, a={a}")
    a=a*2
    print(f"Dans la fonction, après modification, a={a}")
f(a)
print(f"Après la fonction, a={a}")
```

    Avant la fonction, a=10
    Dans la fonction, après modification, a=20
    Après la fonction, a=10


Ici on constate qu'en fait il y a deux variables `a` :
* une en dehors de la fonction, qui n'est pas modifiée. C'est une variable **globale**.
* une à l'intérieur de la fonction, qui peut être modifiée, mais qui ne change pas la variable globale. C'est une variable **locale** à la fonction.


```python
a=10
print(f"Avant la fonction, a={a}")
def f(x) :
    print(f"Dans la fonction, avant modification, x={x}")
    x=x*2
    print(f"Dans la fonction, après modification, x={x}")
    return x
a=f(a)
print(f"Après la fonction, a={a}")
```

    Avant la fonction, a=10
    Dans la fonction, avant modification, x=10
    Dans la fonction, après modification, x=20
    Après la fonction, a=20



```python
x=12
x=f(x)
x
```

    Dans la fonction, avant modification, x=12
    Dans la fonction, après modification, x=24





    24



Ici on a rajouté deux lignes :
* `return a` qui permet à la fonction de renvoyer la valeur modifiée ;
* `a=f(a)` La valeur renvoyée par l'appel `f(a)` est affecté au nom de variable `a`. L'opération effectuée à l'intérieur de la fonction se retrouve répercutée à l'extérieur.


<h2><font color="blue">III : Prototypage des fonctions : les tests unitaires  </font></h2>

<h3><font color="green">a : Réfléchir avant d'agir : ecrire les tests avant la fonction </font></h3>

Lorqsu'on écrit une fonction, il est très important d'avoir une idée précise de ce que la fonction doit renvoyer, y compris dans les *cas tordus* ou limites.
Par exemple, on pourrait considérer une fonction `coefficientDirecteur` qui donne le coefficient directeur d'une droite quand on lui passe en argument les coordonnées de deux points $A$ et $B$.
Je rappelle que le calcul du coefficient directeur de la droite $(AB)$ se fait par l'intermédiare de la formule :
$$m = \frac{y_B-y_A}{x_B-x_A}$$

Ainsi nous aimerions que la fonction travaille avec 4 arguments : `xA,yA,xB,yB`, qu'elle renvoie le coefficient directeur de $(AB)$ quand il y en a un, et qu'elle renvoie `None` quand il n'y en a pas ( dans quels cas n'y-a-t'il pas de coefficient directeur ? )


```python
def coeffDirecteur(xA,yA,xB,yB) :
    return (yB-yA)/(xB-xA)
```


```python
coeffDirecteur(3,6,3,6)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-22-fc283e5e9829> in <module>
    ----> 1 coeffDirecteur(3,6,3,6)
    

    <ipython-input-17-7e9f03d0af29> in coeffDirecteur(xA, yA, xB, yB)
          1 def coeffDirecteur(xA,yA,xB,yB) :
    ----> 2     return (yB-yA)/(xB-xA)
    

    ZeroDivisionError: division by zero


On peut donc **prévoir en avance** différents cas, et on aimerai vérifier que les calculs faits correspondent à ces cas - sans pour autant avoir à tout retaper en permanence.

Pyhton étant *user friendly*, il permet au programmeur de tester automatiquement ces différents cas, grâce au module `doctest`.


C'est pourquoi il est **fortement conseillé** d'utiliser le module `doctest` de Python

<h3><font color="green">b : La docstring d'une fonction</font></h3>

A chaque fonction, on peut associer une **docstring**, littéralement *chaine de documentation*, qui est une chaine de caractères présentant l'utilisation de la fonction, ses paramètres obligatoires, ses paramètres optionnels :


```python
def somme(a,b) :
    """ fonction qui renvoie la somme des arguments a et b, 
    en vérifiant si a et b sont bien du même type, 
    et qui renvoie None sinon"""
    if type(a) == type(b) :
        return a+b
    else :
        return None
```


```python
print(somme(4,"toto"))
```

    None


La fonction `somme` contient donc une **docstring** - introduite par trois guillemets ( pour permettre les sauts de lignes ). Celle-ci décrit l'effet de la fonction, de manière exacte.

On peut accéder à la **docstring** d'une fonction en utilisant la fonction *built-in* `help` :


```python
help(somme)
```

    Help on function somme in module __main__:
    
    somme(a, b)
        fonction qui renvoie la somme des arguments a et b, 
        en vérifiant si a et b sont bien du même type, 
        et qui renvoie None sinon
    


On peut aussi l'appeler sur des fonctions *built-in* :


```python
help(int)
```

    Help on class int in module builtins:
    
    class int(object)
     |  int([x]) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(self, format_spec, /)
     |      Default object formatter.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(self, /)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(self, /)
     |      Returns size in memory, in bytes.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  bit_length(self, /)
     |      Number of bits necessary to represent self in binary.
     |      
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  to_bytes(self, /, length, byteorder, *, signed=False)
     |      Return an array of bytes representing an integer.
     |      
     |      length
     |        Length of bytes object to use.  An OverflowError is raised if the
     |        integer is not representable with the given number of bytes.
     |      byteorder
     |        The byte order used to represent the integer.  If byteorder is 'big',
     |        the most significant byte is at the beginning of the byte array.  If
     |        byteorder is 'little', the most significant byte is at the end of the
     |        byte array.  To request the native byte order of the host system, use
     |        `sys.byteorder' as the byte order value.
     |      signed
     |        Determines whether two's complement is used to represent the integer.
     |        If signed is False and a negative integer is given, an OverflowError
     |        is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  from_bytes(bytes, byteorder, *, signed=False) from builtins.type
     |      Return the integer represented by the given array of bytes.
     |      
     |      bytes
     |        Holds the array of bytes to convert.  The argument must either
     |        support the buffer protocol or be an iterable object producing bytes.
     |        Bytes and bytearray are examples of built-in objects that support the
     |        buffer protocol.
     |      byteorder
     |        The byte order used to represent the integer.  If byteorder is 'big',
     |        the most significant byte is at the beginning of the byte array.  If
     |        byteorder is 'little', the most significant byte is at the end of the
     |        byte array.  To request the native byte order of the host system, use
     |        `sys.byteorder' as the byte order value.
     |      signed
     |        Indicates whether two's complement is used to represent the integer.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    


Voir sur elle-même...


```python
help(help)
```

    Help on _Helper in module _sitebuiltins object:
    
    class _Helper(builtins.object)
     |  Define the builtin 'help'.
     |  
     |  This is a wrapper around pydoc.help that provides a helpful message
     |  when 'help' is typed at the Python interactive prompt.
     |  
     |  Calling help() at the Python prompt starts an interactive help session.
     |  Calling help(thing) prints help for the python object 'thing'.
     |  
     |  Methods defined here:
     |  
     |  __call__(self, *args, **kwds)
     |      Call self as a function.
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    


**Une docstring est essentielle pour comprendre l'utilité d'une fonction ! Vous devrez en utiliser le plus souvent possible !**

<h3><font color="green">c : Le module doctest</font></h3>

Un module Python est un fichier ( ou un ensemble de fichiers ) qui comportent des objets et des fonctions qui peuvent être ajoutées aux fonctionnalité de base de Python. Il en existe un très grand nombre, tous étant spécialisés dans un domaine. On trouve par exemple :
* le module *math*, qui contient beaucoup de fonctions mathématiques ;
* le module *turtle*, qui permet de dessiner géométriquement ;
* le module *pygame*, qui est un module permettant de gérer les différents éléments d'un jeu vidéo ;
* le module *panda*, qui est utilisé pour faire du traitement de données ;
* le module *flask*, qui permet de créer une application web
* ...

Le module *doctest*, lui, permet d'intégrer à la **docstring** un ensemble de tests qui sont vérifiés par l'appel de la fonction **testmod** du module *doctest*.
Par exemple :


```python
import doctest # On charge en mémoire le module doctest( à faire une seule fois par programme, ou par notebook )
def times2(n) :
    """
    Fonction qui multiplie par 2
>>> times2(4)
8
>>> times2(5)
10
>>> times2('a')
'aa'
"""
    return 2*n

doctest.testmod()

```




    TestResults(failed=0, attempted=3)



L'appel à la fonction `doctest.testmod()` déclenche les trois tests présents dans la doctsring, et vérifie que les résultats de la fonctions correspondent à ceux fournit dans la docstring.


```python
def times3(n) :
    """
    Fonction qui multiplie par 3
>>> times3(10)
30
>>> times3(5)
15
>>> times3('a')
'aaa'
"""
    return 3*n



doctest.testmod()
```




    TestResults(failed=0, attempted=6)



L'appel à la fonction `doctest.testmod()` re-teste une nouvelle fois toutes les docstring des fonctions. Icic il y a 6 tests, 3 pour `times2` et 3 pour `times3`, dont un à échoué : celui pour `times3(5)` qui ne donne pas le résultat attendu ( à savoir 12 ).

Un échec des tests amène donc deux problèmes :
* soit la fonction ne fonctionne pas comme voulue ;
* soit les exemples proposés sont faux.

dans tous les cas, **seule la constitution d'un ensemble d'exemples bien choisis** permettra de tester efficacement une fonction - si les tests sont imprécis ou incomplets, la fonction risuqe de poser problème dans certains cas.

**Je me servirai des doctests ou bien des assertions vues plus haut dans ce notebook pour estimer la justesse de vos fonctions et de vos programmes. Une bonne idée serait de TOUJOURS fournir un jeu d'exemple avant de se lancer dans la construction d'une fonction.**

<h2><font color="blue">IV : Exercices  </font></h2>

*Dans tous les exercices suivants, on supposera que l'utilisateur de la fonction fournit des arguments duy bon type*

**Pour tester vos fonctions avec les jeux fournis, n'oubliez pas :**
1. d'importer le module avec `import doctest`.
2. de lancer les tests avec `doctest.testmod()`


1. Ecrire une fonction qui renvoie le maximum de deux nombres donnés :


```python
def maxi(a,b ) :
    """
    Fonction qui renvoie le maximum de deux nombres
>>> maxi(12,3)
12
>>> maxi(-5,9)
9
>>> maxi(6,6)
6
    """
    
```

2. Ecrire une fonction qui renvoie le minimum de deux nombres donnés :



```python
def mini(a,b) :
    """
    Fonction qui renvoie le maximum de deux nombres
>>> mini(12,3)
3
>>> mini(-5,9)
-5
>>> mini(6,6)
6
    """
    
```

3. Ecrire une fonction qui renvoie le maximum de trois nombres donnés :


```python
def maxi3(a,b,c):
    """
     Fonction qui renvoie le maximum de trois nombres
>>> maxi3(5,12,3)
12
>>> maxi3(-5,-7,2)
2
>>> maxi3(6,6,6)
6
>>> maxi3(5,7,7)
7
    """
```

4. Ecrire une fonction qui renvoie le nombre intermédiaire dans trois nombres donnés


```python
def intermediaire(a,b,c) :
      """
    Fonction qui renvoie le nombre intermédiaire deux nombres
>>> intermediaire(12,8,3)
8
>>> intermediaire(-5,0,9)
0
>>> intermediaire(7,7,7)
7
>>> intermediaire(4,7,7)
7
>>> intermediaire(4,4,7)
4
    """
```

5. Erire une fonction qui supprime tous les caractères qui ne sont pas des lettres ( majuscules ou minuscules, sans accents ) d'une chaine de caractères donnée.


```python
def rienQueDesLettres(chaine) :
    """
>>> rienQueDesLettres('  toto  ')
'toto'
>>> rienQueDesLettres('123Toto456')
'Toto'
>>> rienQueDesLettres('Et!C'est Toto ?')
'EtCestToto'
    """
```

7. Ecrire la fonction coefficientDirecteur qui vérifie les conditions ci-dessous 


```python
def coefficientDirecteur(xA,yA,xB,yB) :
    """Fonction renvoyant le coefficient directeur de la droite (AB)
    en connaissant les coordonnées des points A et B, ou None si c'est impossible
>>> coefficientDirecteur(0,0,1,5)
5
>>> coefficientDirecteur(0,0,2,10)
5
>>> coefficientDirecteur(3,4,4,6)
2
>>> coefficientDirecteur(3,4,4,6)
2
>>> coefficientDirecteur(3,4,4,4)
0
>>> coefficientDirecteur(3,4,4,3)
-1
>>> coefficientDirecteur(3,4,3,7)==None
True
>>> coefficientDirecteur(3,4,3,4)==None
True
>>> coefficientDirecteur(4,4,3,4)==None
False
"""
    ###VOTRE CODE ICI
```

8. Ecrire une fonction - et le jeu de test correspondant, qui calcule l'ordonnée à l'origine d'une droite $(AB)$, en prenant en argument les coordonnées des points $A$ et $B$ comme la fonction précédente, et qui renvoie None si c'est impossible.



```python

```

9. Ecrire une fonction - et le jeu de test qui va avec,  qui renvoie l'équation réduite de la droite $(AB)$, en prenant en argument les coordonnées des points $A$ et $B$ comme dans les fonctions précédentes.


```python

```

10. Ecrire une fonction qui donne le discriminant d'un trinome du second degré $ax^2 +bx+c $, en fournissant un jeu d'exemples complets.


```python

```
