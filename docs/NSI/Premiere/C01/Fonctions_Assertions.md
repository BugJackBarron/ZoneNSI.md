# Fonctions, assertions et docstring en  ![logo Python](python-logo.png)


## Premiers pas avec les fonctions

### Pourquoi des fonctions ?

Dans la partie précédente, nous avons terminé par un petit programme qui demande à un·e utilisateur·trice de donner un nombre entier entre 1 et 10, et qui vérifie la saisie jusqu'à ce que l'utilisateur·trice ait effectué une saisie correcte. Voici un exemple simple d'implémentation de ce programme, tel que celui que vous avez proposé :

{{ IDEv('askIntV1') }}

!!! question "Un blocage ?"

    === "Enoncé"
        Quels sont les problèmes pouvant être posé par ce programme ?

    === "Solution"
        * En premier lieu, les lignes 1 et 3 sont des répétitions (des copiés-collés). Or en informatique, on essaye le plus possible de respecter le principe {==**DRY**==} :  *Don't Repeat Yourself*. Une méthode pour corriger ce point pourrait être la suivante :

            ``` python 
            repeter = True
            while repeter :
                saisie = input("Entrez un nombre entre 1 et 10 : ")
                if saisie in [ "1", "2", "3","4", "5", "6", "7", "8", "9", "10" ] :
                    nb = int(saisie)
                    repeter = False
            print(f"Vous avez saisi {nb}")
            ```
        * Dans un second temps, le code fonctionne dans ce cas précis, mais n'est pas adaptable à d'autres situations. En effet, on doit saisir dans la liste **toutes les possibilités pouvant être saisies**, ce qui rend le code peu adaptable à une situation du style « Saisir un nombre entier entre -1000 et 1000 ». Il faut donc modifier complètement la logique de ce programme. Entre autres, il faut découper le code en plusieurs morceaux :
            1. On commencera d'abord à tester si quelque chose a bien été saisi, sinon il faut reposer la question.
            2. Il faut ensuite tester si la suite de caractères saisie correspond bien aux caractères des entiers, et rien qu'à ceux-ci. On pourrait aussi tester si le premier caractère est un signe « - », pour prendre en compte les entiers négatifs.
            3. Enfin, une fois certain que la saisie est bien un entier, on la *trans-type*, puis on regarde si la condition d'encadrement est correcte.

            Le code suivant donne toutes ces étapes :

            ``` python 
            repeter = True # Booléen servant à exécuter la boucle
            while repeter : # Tant que repeter est vrai
                saisie = input("Entrez un nombre entre 1 et 10 : ")
                if saisie != "" : # On ne travaille que si la saisie est une chaine non vide
                    ######## ON TESTE SI LA SAISIE EST CELLE D'UN ENTIER #######
                    est_un_entier = True # On suppose que c'est un entier
                    indice_depart = 0 # et que le premier caractère est un chiffre                    
                    if saisie[0] == "-" :# si le premier caractère est un signe "-",
                        indice_depart = 1# On regardera chaque caractère à partir de l'indice 1
                    for caractere in saisie[indice_depart : len(saisie)] : # Pour chaque caractère
                        if caractere not in "0123456789" : # Si ce n'est pas un chiffre
                            est_un_entier = False # Alors la saisie n'est pas un entier
                    ###### ON TESTE SI IL EST ENTRE 1 et 10 #######
                    if est_un_entier : #
                        nb = int(saisie)# Trans-typage
                        if 1<= nb <= 10 : # Si les conditions sont remplies
                            repeter = False # On arrête la boucle
            print(f"Vous avez saisi {nb}") # Juste là pour montrer la saisie
            ```


!!! question "Application 1 : Multiplier les codes"


    === "Enoncé"

        Imaginons maintenant un programme qui demande **trois fois** à l'utilisateur·trice d'entrer un tel nombre, puis qui vérifie si les trois nombres correspondent à une configuration de Pythagore (c'est-à-dire $a^2 + b^2 = c^2$).

        Vous devez vous inspirer du programme précédent pour compléter le programme ci-dessous afin d'obtenir trois nombres entiers `nb1`, `nb2` et `nb3` saisis par l'utilisateur·trice :

    === "Une solution possible"

        Un programme avec notre niveau actuel en Python pourrait être le suivant :

        ```` python
            repeter = True
            while repeter :
                saisie1 = input("Entrez un nombre entre 1 et 10 : ")
                if saisie1 != "" :
                    est_un_entier = True
                    indice_depart = 0
                    if saisie1[0] == "-" :
                        indice_depart = 1
                    for caractere in saisie1[indice_depart : len(saisie1)] :
                        if caractere not in "0123456789" :
                            est_un_entier = False
                    if est_un_entier :
                        nb1 = int(saisie1)
                        if 1<= nb1 <= 10 :
                            repeter = False
            repeter = True
            while repeter :
                saisie2 = input("Entrez un nombre entre 1 et 10 : ")
                if saisie2 != "" :
                    est_un_entier = True
                    indice_depart = 0
                    if saisie2[0] == "-" :
                        indice_depart = 1
                    for caractere in saisie2[indice_depart : len(saisie2)] :
                        if caractere not in "0123456789" :
                            est_un_entier = False
                    if est_un_entier :
                        nb2 = int(saisie2)
                        if 1<= nb2 <= 10 :
                            repeter = False
            repeter = True
            while repeter :
                saisie3 = input("Entrez un nombre entre 1 et 10 : ")
                if saisie3 != "" :
                    est_un_entier = True
                    indice_depart = 0
                    if saisie3[0] == "-" :
                        indice_depart = 1
                    for caractere in saisie3[indice_depart : len(saisie3)] :
                        if caractere not in "0123456789" :
                            est_un_entier = False
                    if est_un_entier :
                        nb3 = int(saisie3)
                        if 1<= nb3 <= 10 :
                            repeter = False

            if nb1**2 + nb2**2 == nb3**2 or nb2**2 + nb3**2 == nb1**2 or nb3**2 + nb1**2 == nb2**2 :
                print(f"({nb1}, {nb2}, {nb3}) est un triplet de Pythagore")
            else :
                print(f"({nb1}, {nb2}, {nb3}) n'est pas un triplet de Pythagore)
        
        ````

!!! warning "Mauvaise pratique"
    Si ce code fait le travail demandé, il n'en est pas moins de *mauvaise qualité* pour plusieurs raisons :

    * Il est long, avec des répétitions. Plus un code est long, plus il prend de place en mémoire, alors qu'on cherche plutôt à minimiser ce facteur. Et surtout, {==**plus un code est long, moins il est lisible !**==}
    * Le copié-collé force quand même à repasser sur chacune des parties pour modifier le nom des variables (sinon les valeurs seraient écrasées). Ainsi toute modification dans la structure du code doit être **réécrite à chaque fois** que le morceau de code est copié. Dans notre exemple, ce n'est que trois fois, le risque d'erreurs est minime, mais pour un plus grand nombre de répétitions, il est très facile d'oublier une modification.

### Première fonction

#### Définition d'une fonction

On va donc améliorer non seulement la lisibilité de notre code, mais aussi son efficacité et sa simplicité, en utilisant une **fonction**.

!!! abstract "Définition : fonction"
    Une {==**fonction**==} est un {==**bloc de code nommé**==} (c'est-à-dire possédant un nom dans l'espace de noms, comme toute autre variable) et qui :
    
    * **n'est pas exécuté** au moment de sa définition ;
    * mais peut être **appelé** plusieurs fois dans le code par l'intermédiaire de son nom, {==**suivi d'une paire de parenthèses**==}. Ces appels (*call* en anglais) exécuteront alors l'intégralité du code à chaque appel, et renverra une {==**valeur de retour**==}, c'est-à-dire un objet qui pourra être utilisé normalement dans la partie de code ayant appelé la fonction.

!!! example "Pour notre exemple : " 

    {{ IDEv('askIntFctV1') }}


    En regardant la première ligne, qu'on appelle la {==**signature de la fonction**==} :
    ``` python
    def ask_user_int() -> int:
    ```

    * La fonction est introduite par le mot clé `def`, suivi du **nom de la fonction** puis d'un couple de parenthèses `()`, ce qui rend l'objet {==**appelable**==} (*callable* en anglais).
    * la notation `-> int` est un {==**type hint**==}, autrement dit un *indice de type*, qui indique que la valeur renvoyée par la fonction sera de type `int`. Les **type hints** sont *facultatifs en Python*, mais strictement nécessaires dans d'autres langages (`Java`, `C`, `C++`, etc).
    * Les deux points définissent un bloc de code qui est repéré par **une indentation**, tout comme on définit des blocs dans des structures conditionnelles ou des boucles.

    On fait appel à cette fonction en appelant le nom `ask_user_int()`, ce qui déclenche le bloc de code, puis crée un objet de retour correspondant à la valeur saisie par l'utilisateur.

!!! warning "Oubli des parenthèses"

    Dans le cas d'un oubli des parenthèses lorsqu'on appelle une fonction, on obtient dans le terminal le message suivant :

    ```` python
    >>> ask_user_int
    <function ask_user_int at 0xe8c1a0>
    ````

    Qui signifie simplement que le nom `ask_user_int` fait référence à une fonction dont l'adresse dans la mémoire de l'ordinateur est donnée sous forme *hexadécimale*.

??? warning "Pour les cracks"
    Notez que `ask_user_int` est juste un nom, l'objet correspondant est stocké dans l'espace des objets. On peut donc écrire les choses suivantes :

    ```python
    >>> demande_entier=ask_user_int
    >>> demande_entier()
    ```


#### Utilisation de la valeur de retour

Comme tout objet, la valeur de retour d'une fonction doit elle-même être stockée dans une variable afin de ne pas être ramassée par le *garbage collector*.

!!! example "Exemple"

    ```python
    >>> entier = ask_user_int()
    >>> print(f'La racine carrée du nombre {entier} est {entier**(1/2)}')
    ```

    L'interpréteur Python évalue la ligne `entier = ask_user_int()` :

    * Il commence par appeler le code correspondant à La fonction `ask_user_int()`.
    * Le code de la fonction demande une saisie à l'utilisateur, et une fois l'instruction `return` atteinte, l'instruction `ask_user_int()` est remplacée à l'endroit de l'appel par la valeur saisie par l'utilisateur, converti en objet de type int.
    * L'objet est ensuite stocké dans une variable nommée `entier`, et peut alors être utilisé en dehors de la fonction.
    

#### Factorisation du code de Pythagore

Le code du programme de vérification de Pythagore peut alors être {==**factorisé**==} (ce qui signifie globalement qu'on réduit sa taille en évitant les répétitions), afin de respecter le principe DRY :


{{ IDEv('askIntFctV2') }}

Ce qui a l'avantage d'être vraiment plus clair.



### Exercices

!!! question "Application 2"

    === "Enoncé"

        Créer une fonction nommée `table7` qui **renvoie** la table de multiplication de 7 avec un multiplicateur allant de 0 à 10, sous la forme d'une chaîne de caractères comme ci-dessous :

        ``` 
        "7x0=0 \n 7x1=7 \n 7x2=14 ..."
        ```

        **Indication :** le symbole `\n`, insère un saut de ligne dans une chaîne de caractères.

    === "Solution"

        ``` python
        def table7() -> str:
            table = ''
            for i in range(11) : 
                table += f'7x{i} = {7*i} \n'
            return table
        ```

### Augmenter la capacité des fonctions : les paramètres obligatoires 

#### Premiers

L'exemple de la fonction `ask_user_int` est assez limité. Dans l'absolu, on pourrait souhaiter que la fonction demande un nombre entier entre 2 valeurs variables, par exemple entre 1 et 100 ou bien entre -10 et 10.

Pour ce faire, il faut, dans la définition de la fonction, préciser des {==**paramètres**==} qui seront des objets transmis et nommés **initialisés à certaines valeurs lors de l'appel à la fonction** :


!!! example "Exemple :"

    {{ IDEv('askUserIntV3') }}

    La fonction `ask_user_int` utilise maintenant deux paramètres `borne_min` et `borne_max`, dont les **type hints** indiquent que ce doit être deux entiers.

    Une fois la fonction définie, on peut l'appeler en lui passant des {==**arguments==}, c'est-à-dire des valeurs qui seront affectées aux paramètres :

    ```python
    >>> ask_user_int(1,100)
    >>> ask_user_int(-10,10)
    ```

!!! warning "Erreurs d'appels et notion de précondition" 
    Avec le code actuel de la fonction `ask_user_int`, on peut rencontrer un certain nombre de difficultés. Testez les commandes suivantes dans la console

    === "Test 1"

        === "Code"
            ```python
            ask_user_int()
            ```
        === "Problème"
            L'erreur signalée est de type `TypeError`, et le message d'erreur nous dit qu'il manque 2 arguments lors de l'appel, et que ces arguments sont `borne_min` et `borne_max`.

    === "Test 2"

        === "Code"
            ```python
            ask_user_int(45)
            ```

        === "Problème"
            L'erreur signalée est de type `TypeError`, et le message d'erreur nous dit qu'il manque 1 argument lors de l'appel, et que cet argument est `borne_max`. Cela signifie aussi que le nom `borne_min` a bien reçu la valeur `45`.

    === "Test 3"

        === "Code"

            ```python
            ask_user_int(0.5,2.5)
            ```

        === "Problème"

            Aucun véritable erreur n'est levée par Python, bien que les *type hints* demandent des arguments de type `int`. Comme dit précédemment, ces indications sont facultatives (à destination des programmeur·euse·s), et ici les transgresser ne pose pas vraiment de problème.

    === "Test 4"

        === "Code"
            ```python
            ask_user_int(30,10)
            ```

        === "Problème"
            Ici, la fonction tourne en boucle et il est impossible de saisir une réponse qui amènera à l'instruction `return`. En effet, lors de l'appel à la fonction, on a :

            * `borne_inf` initialisé à `30`;
            * `borne_sup` initialisé à `10`;
            * pour atteindre l'instruction `return`, il faudrait que l'utilisateur·trice ait saisi·e un nombre `nb` à la fois supérieur à `30` et inférieur à `10`, ce qui est impossible.

    === "Solution ?"
        On essayera donc le plus possible de créer des tests dans les fonctions permettant de tester des {==**préconditions**==}, c'est-à-dire des tests vérifiant les propriétés nécessaires concernant les arguments, par exemple ici que les arguments sont bien de type entier, et que `borne_inf` est bien inférieur ou égal à `borne_sup`. Ces tests seront vu dans la partie concernant les {==**assertions**==}.


#### Factoriser le code, 2ème saison

On a vu que **factoriser** le code, c'est réduire la taille d'un code en évitant les répétitions (principe DRY). Mais en fait, c'est aussi séparer le code en **fonctions autonomes respectant une certaine logique interne**. Par exemple, dans le code de notre fonction `ask_user_int`, il y a deux parties bien distinctes :

* la première est de vérifier que la saisie est bien celle d'un entier ;
* la seconde est de vérifier les conditions d'encadrement du nombre saisi.

On pourrait alors souhaiter séparer le code en deux fonctions :

* créer une fonction `is_integer`, dont la signature serait :

    ```python
    def is_integer(word : str) -> bool :
    ```
    qui utilise comme paramètre `word`, une chaine de caractère, et qui renvoie un booléen `True` si `word` est transtypable en entier, et `False` sinon.

* puis conserver la fonction `ask_user_int` telle qu'elle est définie actuellement.

On obtiendrait alors le code suivant :

 {{ IDEv('askUserIntV3bis') }}

 Vous noterez que la fonction `is_integer` est utilisée au sein de la fonction `ask_user_int`.

#### Applications


!!! question "Application 3"


    === "Enoncé"
        Créer une fonction `table_multi(m : int)-> str` qui prend un argument entier `m` et écrit la table de multiplication de ce nombre, avec un multiplicateur allant de 1 à 10.

!!! question "Application 4 : motif dans une chaine"

    === "Enoncé"
        Créer une fonction `trouve_chaine(motif : str, texte : str) -> bool`qui prend deux arguments, un `motif` ( une chaine de caractères )  et un `texte` ( une autre chaine de caractères )  et qui renvoie `True` si le `motif` est présent dans la `chaine`, quel que soit la casse du motif ou celle de la chaine, et `False` sinon.  Vous pouvez tester avec les lignes suivantes :

        ```python
        assert trouve_chaine('Toto', 'Toto va à la plage')==True, 'Meme casse pas trouvée'
        assert trouve_chaine('Totos', 'Toto va à la plage')==False, 'Chaine non présente trouvée'
        assert trouve_chaine('TOTO', 'Toto va à la plage')==True, 'Problème de majuscules dans le motif'
        assert trouve_chaine('toto', 'TOTO va à la plage')==True, 'Problème de minuscules dans le motif'
        assert trouve_chaine('ToTo', 'OtOtO va à la plage')==True, 'Que dire ?'
        ```



### Augmenter la capacité des fonctions : les arguments optionnels 

Notre fonction `ask_user_int` commence à être intéressante. Mais nous pourrions souhaiter personnaliser le message de la question, sans pour autant avoir envie de le changer systématiquement.
C'est tout à fait possible en Python, grâce aux **paramètres optionnels**. Il s'agit de paramètres dont le nom est donné dans la **signature**, mais avec **une valeur par défaut**. Ainsi :


{{ IDEv('askUserIntV4') }}

Ainsi, la fonction ci-dessus possède trois paramètres :

* deux paramètres **obligatoires**, `borne_min` et `borne_max`, de type `int` ;
* un paramètre **optionnel**, `prenom`, de type `str`, dont la **valeur par défaut est la chaine `Inconnu`.


Il est à noter qu'impérativement les **paramètres obligatoires doivent être placés avant les paramètres optionnels**.

On peut alors appeler la fonction des différentes manières suivantes (à tester) :

=== "1"

    ```python
    ask_user_int(0, 10)
    ```

=== "2"

    ```python
    ask_user_int(0, 10, nom='Toto')
    ```

=== "3"

    ```python
    ask_user_int(25, 40, nom='foo')
    ```
{{ terminal() }}

!!! question "Application 5 : paramètres optionnels"

    === "Enoncé"
        Compléter la fonction `table_multi` afin qu'elle utilise deux paramètres optionnels, la valeur de départ, fixée à 0 initialement, et la valeur d'arrivée du multiplicateur, fixée à 10 initialement.

    === "Solution"

        ``` python
        def table_multi(nb : int, depart : int = 0, fin : int =10) -> str :
            table = ''
            for i in range(depart, fin+1) :
                table += f'{nb}}x{i} = {nb*i} \n'
            return table
        ```

!!! question "Application 6 : paramètres optionnels"

    === "Enoncé"

        Réécrire la fonction `trouve_chaine` afin qu'elle utilise un *paramètre booléen optionnel* `verif_casse`, afin de déterminer si le `motif` est présent dans le `texte` en vérifiant la casse ou non. Par défaut le paramètre sera `False`. Vous pouvez utiliser les tests ci-dessous :

        ```python
        ### Cette cellule est une cellule vous permettant de tester votre fonction
        ##les assertions suivantes sont les même que précédemment
        assert trouve_chaine('Toto', 'Toto va à la plage')==True, 'Meme casse pas trouvée'
        assert trouve_chaine('Totos', 'Toto va à la plage')==False, 'Chaine non présente trouvée'
        assert trouve_chaine('TOTO', 'Toto va à la plage')==True, 'Problème de majuscules dans le motif'
        assert trouve_chaine('toto', 'TOTO va à la plage')==True, 'Problème de minuscules dans le motif'
        assert trouve_chaine('ToTo', 'OtOtO va à la plage')==True, 'Que dire ?'
        # Mais on rajoute celles-ci :
        assert trouve_chaine('Toto', 'Toto va à la plage',verif_casse = True )==True, 'Meme casse pas trouvée'
        assert trouve_chaine('TOTO', 'TOTO va à la plage',verif_casse = True )==True, 'Meme casse pas trouvée'
        assert trouve_chaine('Totos', 'Toto va à la plage',verif_casse = True)==False, 'Chaine non présente trouvée'
        assert trouve_chaine('TOTO', 'Toto va à la plage',verif_casse = True)==False, 'Problème de majuscules dans le motif'
        assert trouve_chaine('toto', 'TOTO va à la plage',verif_casse = True)==False, 'Problème de minuscules dans le motif'
        assert trouve_chaine('ToTo', 'OtOtO va à la plage',verif_casse = True)==False, 'Que dire ?'
        ```

    === "Solution"

        ```python
        def trouve_chaine(motif : str,texte : str, verif_casse : bool =False) -> bool :
            if verif_casse==True :
                return motif in texte
            else :
                return  motif.lower() in texte.lower() :
        ```


### Commenter son code : les docstrings

!!! tips "Commenter son code"

    Une bonne habitude, à prendre immédiatement, est celle de commenter son code, c'est-à-dire d'expliquer l'implémentation de votre code sous la forme de commentaires, écrits en français (ou mieux, en anglais). Les commentaires sont **des lignes non-lues par l'interpréteur Python**, commençant par le symbole *dièse* `#`.

    Ces explications sont importantes, car vous vous rendrez vite compte que vous serez parfois incapable de comprendre un code que vous avez écrit vous-même quelques semaines voir quelques jours auparavant !

    Alors imaginez celui qui doit lire votre code, mais qui ne l'a pas écrit... 


Les concepteur·trice·s de Python ont créé une fonction spécifique permettant d'obtenir des informations sur les autres objets : la fonction `help`.

Testez par exemple la commande `help(print)` dans la console suivante, puis essayez avec d'autres objets de Python.

{{ terminal() }}

La fonction `help` va chercher dans l'objet passé en argument sa {==**docstring**==}, littéralement *chaine de documentation*, qui est une chaine de caractères crée par le ou la codeur·euse présentant l'utilisation de la fonction, ses paramètres obligatoires, ses paramètres optionnels, etc... Une **docstring** est construite comme une chaine de caractères *non nommée* présentée immédiatement après la déclaration de la fonction, comme dans l'exemple ci-dessous :

{{ IDEv('docstring1') }}


La fonction `somme` contient donc une **docstring** - introduite par trois guillemets (pour permettre les sauts de lignes). Celle-ci décrit l'effet de la fonction, de manière exacte.

On peut alors accéder à la **docstring** d'une fonction en utilisant la fonction *built-in* `help` : testez par exemple `help(somme)`.
  

!!! tips "Les docstrings"
    {==**Une docstring est essentielle pour comprendre l'utilité d'une fonction ! Vous devrez en utiliser le plus souvent possible !**==}

## Notion de portée des variables  

Au sein d'un même programme, les variables définies n'ont pas systématiquement la même **portée**. La **portée d'une variable**, c'est l'espace des objets/noms (on parle aussi de *monde*) dans lequel est défini cette variable.

En utilisant le site [Python Tutor](https://pythontutor.com/){: target="_blank"}, nous allons essayer de comprendre cette notion de portée des variables.

### Variables globales

<iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=gvar%20%3D%208%0Adef%20f%28%29%20%3A%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20la%20variable%20gvar%20vaut%20%7Bgvar%7D%22%29%0A%0Af%28%29%0Aprint%28f%22En%20dehors%20de%20la%20fonction,%20la%20variable%20gvar%20vaut%20%7Bgvar%7D%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Dans l'exemple ci-dessus, la variable `gvar` est définie dans {==**l'espace de nom global**==} (*global frame*). Elle est accessible en lecture depuis l'intérieur de la fonction `f`. On parlera alors de {==**variable globale**==}.

### Variables locales

<iframe width="800" height="300" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=def%20f%28%29%20%3A%0A%20%20%20%20gvar2%20%3D%208%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20la%20variable%20gvar2%20vaut%20%7Bgvar2%7D%22%29%0A%0Af%28%29%0Aprint%28f%22En%20dehors%20de%20la%20fonction,%20la%20variable%20gvar2%20vaut%20%7Bgvar2%7D%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

Dans l'exemple ci-dessus, la variable `gvar2` est définie dans l'espace des noms associé à la fonction `f`, et qui est créé {==**au moment de l'appel à cette fonction**==} (*frame f*). Cet espace est détruit par le *garbage collector* dès que l'exécution de la fonction est terminé (une fois la valeur de `return` renvoyée dans l'espace appelant). Il devient donc impossible d'utiliser la variable `gvar2` puisqu'elle a disparue. `gvar2` est une {==**variable locale**==} à la fonction `f`.

!!! warning "Changer la valeur d'une variable globale"

    Regardons maintenant le code suivant :

    <iframe width="800" height="350" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=gvar%3D%2010%0Adef%20f%28%29%20%3A%0A%20%20%20%20gvar%3Dgvar%2B2%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20la%20variable%20gvar%20vaut%20%7Bgvar%7D%22%29%0A%0Af%28%29%0Aprint%28f%22En%20dehors%20de%20la%20fonction,%20la%20variable%20gvar%20vaut%20%7Bgvar%7D%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

    Le code précédent déclenche une erreur `UnboundLocalError` en ligne 3. Cela signifie que l'interpréteur Python ne peut pas effectuer la ligne `gvar=gvar+2` car il cherche une variable `gvar` qu'il peut modifier. Or {==**une variable définie hors d'une fonction ne peut pas être modifiée par celle-ci**==}.

    Il est par contre possible de travailler sur {==**une copie**==} de la variable souhaitée (*uniquement dans le cas des types primitifs `int`, `float`, `str`...), en utilisant une fonction ayant un argument. Il faudra par conséquent **retourner la valeur changée** pour qu'elle soit effective. Par exemple comparez les deux scripts suivants :


    === "Code incorrect"

        <iframe width="800" height="350" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=a%3D10%0Aprint%28f%22Avant%20la%20fonction,%20a%3D%7Ba%7D%22%29%0Adef%20f%28a%29%20%3A%0A%20%20%20%20%23print%28f%22Dans%20la%20fonction,%20avant%20modification,%20a%3D%7Ba%7D%22%29%0A%20%20%20%20a%3Da*2%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20apr%C3%A8s%20modification,%20a%3D%7Ba%7D%22%29%0Af%28a%29%0Aprint%28f%22Apr%C3%A8s%20la%20fonction,%20a%3D%7Ba%7D%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

        Ici on constate qu'en fait il y a deux variables `a` :

        * une en dehors de la fonction, qui n'est pas modifiée. C'est une variable **globale**.
        * une à l'intérieur de la fonction, qui peut être modifiée, mais qui ne change pas la variable globale. C'est une variable **locale** à la fonction.

        La fonction `f` ne renvoyant aucune donnée, la variable locale `a` est détruite après la fin de la fonction `f`. 

    === "Code correct"

        <iframe width="800" height="350" frameborder="0" src="https://pythontutor.com/iframe-embed.html#code=a%3D10%0Aprint%28f%22Avant%20la%20fonction,%20a%3D%7Ba%7D%22%29%0Adef%20f%28x%29%20%3A%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20avant%20modification,%20x%3D%7Bx%7D%22%29%0A%20%20%20%20x%3Dx*2%0A%20%20%20%20print%28f%22Dans%20la%20fonction,%20apr%C3%A8s%20modification,%20x%3D%7Bx%7D%22%29%0A%20%20%20%20return%20x%0Aa%3Df%28a%29%0Aprint%28f%22Apr%C3%A8s%20la%20fonction,%20a%3D%7Ba%7D%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


        Ici on a rajouté deux lignes :

        * `return a` qui permet à la fonction de renvoyer la valeur modifiée ;
        * `a = f(a)` La valeur renvoyée par l'appel `f(a)` est affecté au nom de variable `a`. L'opération effectuée à l'intérieur de la fonction se retrouve répercutée sur la variable globale `a`.


## Tests, assertions et module Doctest

### Préconditions

Comme nous l'avons vu pour la fonction `ask_user_int`, il est souvent nécessaire de tester des {==**préconditions**==} sur les arguments d'une fonction, pour s'assurer que celle-ci fonctionnera bien selon le schéma voulu.

Une méthode pour tester les préconditions est d'utiliser des {==**assertions**==}. 

L'instruction `assert` de Python fonctionne de la manière suivante :


```` python
 assert trouve_chaine('Toto', 'Toto va à la plage')==True, 'Meme casse pas trouvée'
````

L'instruction `assert` teste un booléen, ici `trouve_chaine('Toto', 'Toto va à la plage')==True`. Il peut alors se produire deux cas :

* soit le booléen est `True`, auquel cas l'interpréteur passe à la ligne suivante (il ne se passe rien de visible) ;
* soit le booléen est `False`, auquel cas l'interpréteur {==**arrête le code**==} en levant une erreur de type `AssertionError` et affiche la chaine de caractère passée en second argument, ici `'Meme casse pas trouvée'`.

!!! example "Correction de la fonction `ask_user_int`"

    ``` python
    def ask_user_int(borne_min : int, borne_max : int, nom : str ='Inconnu' ) -> int :
        """ Fonction demandant un entier compris entre borne_nf et borne_sup.
        personnalisation du message avec le paramètre optionnel nom.
        renvoi un objet de type entier.
        """
        assert type(borne_inf) == int and type(borne_sup) == int, "Erreur de type sur borne_inf et borne_sup"
        assert type(nom) == str, "Erreur de type sur nom"
        assert borne_inf <= borne_sup , "borne_inf n'est pas inférieure à borne_sup"

        repeter = True
        while repeter :
            ...# Le code ici n'est pas changé        
    ```

    Testez maintenant cette fonction avec de mauvaises valeurs pour les arguments.

### Réfléchir avant d'agir : écrire les tests avant la fonction

Lorsqu'on écrit une fonction, il est très important d'avoir une idée précise de ce que la fonction doit renvoyer, y compris dans les *cas extrêmes* ou *cas spécifiques*.

Par exemple, on pourrait considérer une fonction `coefficient_directeur` qui donne le coefficient directeur d'une droite quand on lui passe en argument les coordonnées de deux points $A$ et $B$.
Je rappelle que le calcul du coefficient directeur de la droite $(AB)$ se fait par l'intermédiaire de la formule :

$$m = \frac{y_B-y_A}{x_B-x_A}$$

Ainsi nous aimerions que la fonction travaille avec 4 arguments de type entiers  `xA, yA, xB, yB`, qu'elle renvoie le coefficient directeur de $(AB)$ sous la forme d'un flottant si ce coefficient existe, et qu'elle renvoie `None` quand il n'existe pas. On, définit ici ce qu'on appelle une {==**interface**==} de la fonction :

```python
def coefficient_directeur(xA : int, yA : int, xB : int, yB : int) -> float :
    """ Renvoie le coefficient directeur de la droite (AB) telle que :
        A (xA ; yA) et B(xB ; yB), et les coordonnées de A ety B sont entières.
        Dans le cas ou le coefficient directeur n'existe pas, renvoie None
    """
    ... 
    
```


On souhaite donc **prévoir en avance** différents cas de fonctionnement de la fonction, et on aimerait vérifier que les calculs effectués par la fonction correspondent bien à ces cas.

Par exemple, nous aimerions que la fonction vérifie le test suivant :

```` python
>>> coefficient_directeur(2, 4, 3, 7)
3.0
````



!!! question "Écrire des tests"

    === "Enoncé"

        1. Écrire 5 tests prenant en compte tous les cas possibles d'utilisation de la fonction, en supposant que les types fournis en argument soient bien des entiers.
        2. Compléter la fonction `coefficient_directeur` afin qu'elle remplisse le rôle qui lui est demandé.

    === "Solution"

        A venir !




### Tester avec le module doctest

Pyhton étant *user friendly*, il permet au programmeur de tester automatiquement, grâce au module `doctest`.

Un module Python est un fichier (ou un ensemble de fichiers) qui comporte(nt) des objets et des fonctions qui peuvent être ajoutés aux fonctionnalité de base de Python. Il en existe un très grand nombre, tous étant spécialisés dans un domaine. On trouve par exemple :

* le module *math*, qui contient beaucoup de fonctions mathématiques ;
* le module *turtle*, qui permet de dessiner géométriquement ;
* le module *pygame*, qui est un module permettant de gérer les différents éléments d'un jeu vidéo ;
* le module *panda*, qui est utilisé pour faire du traitement de données ;
* le module *flask*, qui permet de créer une application web
* ...

Un module doit être chargé en mémoire une fois (de préférence au début du code), par l'intermédiaire de la commande :

```` python
import nom_du_module
````

??? warning "Mais non, ca ne se fait pas que comme ça !"
    Oui, vous avez raison, mais ce n'est pas le cas de ce cours, nous verrons l'import de modules plus tard dans l'année...

Le module *doctest*, lui, permet d'intégrer à la **docstring un ensemble de tests** qui sont vérifiés par l'appel de la fonction **testmod** du module *doctest*.

Par exemple, copiez-collez le code suivant dans un fichier :

```python

# Zone d'import des modules
import doctest # On charge en mémoire le module doctest

# Zone de déclaration des fonctions

def times2(n : object) -> object:
    """
    Fonction qui multiplie par 2, selon le type d'objet

>>> times2(4)
8
>>> times2(5.4)
10.8
>>> times2('a')
'aa'
"""
    return 2*n


# Zone du script global

doctest.testmod() # Lance les tests des fonctions déclarées
```



L'appel à la fonction `doctest.testmod()` déclenche les trois tests présents dans la doctsring, et vérifie que les résultats de la fonctions correspondent à ceux fournit dans la docstring.

!!! question "Application 7 : Ajouter une fonction et des tests"

    === "Enoncé"

        Créez une fonction `times3` qui multiplie un objet par 3, en écrivant les tests correspondants.
        
    === "Solution"

        A venir !

**Je me servirai de doctests ou bien d'assertions pour estimer la justesse de vos fonctions et de vos programmes. Une bonne idée serait de TOUJOURS fournir un jeu d'exemple avant de se lancer dans la construction d'une fonction.**

## Exercices  

*Dans tous les exercices suivants, on devra écrire pour chacune des fonction des assertions permettant de tester les préconditions.*

**Pour tester vos fonctions avec les jeux fournis, n'oubliez pas :**

* d'importer le module avec `import doctest` ;
* de lancer les tests avec `doctest.testmod()` ;

Vous pourrez créer un seul fichier contenant l'ensemble des fonctions ci-dessous.


1. Ecrire une fonction qui renvoie le maximum de deux nombres `ìnt` donnés :

    ```python
    def maxi(a : int,b :int) -> int :
        """
        Fonction qui renvoie le maximum de deux nombres de type int.
    >>> maxi(12,3)
    12
    >>> maxi(-5,9)
    9
    >>> maxi(6,6)
    6
        """
        
    ```

2. Écrire une fonction qui renvoie le minimum de deux nombres `int` donnés :


    ```python
    def mini(a : int, b : int ) -> int :
        """
        Fonction qui renvoie le minimum de deux nombres
    >>> mini(12,3)
    3
    >>> mini(-5,9)
    -5
    >>> mini(6,6)
    6
        """
        
    ```

3. Écrire une fonction qui renvoie le maximum de trois nombres `int` donnés :

    ```python
    def maxi3(a : int, b : int, c : int) -> int :
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

4. Écrire une fonction qui renvoie le nombre intermédiaire dans trois nombres `int` donnés

    ```python
    def intermediaire(a : int, b : int, c : int) -> int :
        """
        Fonction qui renvoie le nombre intermédiaire deux nombres
    >>> intermediaire(12,8,3)
    8
    >>> intermediaire(-5,9,0)
    0
    >>> intermediaire(7,7,7)
    7
    >>> intermediaire(7,4,7)
    7
    >>> intermediaire(4,4,7)
    4
        """
    ```

5. Écrire une fonction qui supprime tous les caractères qui ne sont pas des lettres (majuscules ou minuscules, sans accents) d'une chaine de caractères donnée.

    ```python
    def rienQueDesLettres(chaine) :
        """
    >>> rienQueDesLettres('  toto  ')
    'toto'
    >>> rienQueDesLettres('123Toto456')
    'Toto'
    >>> rienQueDesLettres("Et!C'est Toto ?")
    'EtCestToto'
        """
    ```

7. Écrire la fonction coefficient_directeur qui vérifie les conditions ci-dessous 


    ```python
    def coefficient_directeur(xA,yA,xB,yB) :
        """Fonction renvoyant le coefficient directeur de la droite (AB)
    en connaissant les coordonnées des points A et B, ou None si c'est impossible
    >>> coefficient_directeur(0,0,1,5)
    5
    >>> coefficient_directeur(0,0,2,10)
    5
    >>> coefficient_directeur(3,4,4,6)
    2
    >>> coefficient_directeur(3,4,4,6)
    2
    >>> coefficient_directeur(3,4,4,4)
    0
    >>> coefficient_directeur(3,4,4,3)
    -1
    >>> coefficient_directeur(3,4,3,7)==None
    True
    >>> coefficient_directeur(3,4,3,4)==None
    True
    >>> coefficient_directeur(4,4,3,4)==None
    False
        """
    ###VOTRE CODE ICI
    ```

8. Écrire une fonction - et le jeu de test correspondant, qui calcule l'ordonnée à l'origine d'une droite $(AB)$, en prenant en paramètres les coordonnées des points $A$ et $B$ comme la fonction précédente, et qui renvoie None si c'est impossible.

9. Écrire une fonction - et le jeu de test qui va avec, qui renvoie l'équation réduite de la droite $(AB)$, en prenant en paramètres les coordonnées des points $A$ et $B$ comme dans les fonctions précédentes.

10. Écrire une fonction - et le jeu de test qui va avec, qui teste si une chaine de caractère en paramètre est trans-typable en un nombre flottant, puis une fonction `ask_user_float` qui demande à un·e utilisateur·trice de saisir un nombre flottant compris entre deux bornes minimum et maximum flottantes, et ce de manière *dumbproof*.