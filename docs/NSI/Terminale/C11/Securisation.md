# Sécurisation des communications

## Rappels : communication sur internet

Que se passe-t-il lorsque nous tapons dans la barre d'adresse de Firefox une URL, telle que `http://www.zonensi.fr/` ? Entre le cours de SNT de seconde, et celui de NSI, nous pouvons décrire l'enchainement des communications ainsi :

1. L'URL est décodée par le navigateur, qui isole :
    * le protocole utilisé : `HTTP`
    * le nom de domaine : `www.zonensi.fr`
    * le chemin vers la ressource : `/`, la racine du site.
2. Le navigateur effectue une résolution de nom, soit en se connectant à un serveur `DNS`, soit dans son propre cache `DNS`, ce qui lui donne l'adresse `IP` de la ressource cherchée.
3. Le navigateur peut établir une connexion `TCP` vers l'adresse `IP`, via un [handshaking en trois temps](https://fr.wikipedia.org/wiki/Three-way_handshake#Fonctionnement){: target="_blank"}, comme montré sur l'image ci-dessous :

    ![TCP Handshake](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Tcp_normal_2.png/800px-Tcp_normal_2.png){: style="width:30%; margin:auto;display:block;background-color: #d2dce0;"}

4. Une fois la connexion établie, client et serveur échangent des données en utilisant le protocole `HTTP`, tout en découpant les données en paquets `TCP`, eux-mêmes encapsulés dans des paquets `IP` (on pourra se rappeler du modèle `OSI`).

    ![Encapsulation](http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/img/arse3_couche_internet.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}

5. Les paquets sont transmis de routeurs en routeurs, en étant à chaque fois désencapsulés pour inscrire l'adresse `IP` du prochain routeur.

    ![Routage](http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/img/arse3_chemin_transmission_fin.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}



!!! warning "Des limites"

    Ce système, en place depuis l'invention de `TCP/IP` dans les années 1970, a vu l'intégration de chaque nouveau protocole (`FTP`, `SMTP`, etc) au sein de la couche application. Mais avec la démocratisation d'Internet, des problèmes sont rapidement apparus : si on utilise tel quel le modèle écrit ci-dessus pour effectuer des opérations bancaires ou échanger des données confidentielles, on se rend compte qu'un grand nombre d'intermédiaires (en particulier les routeurs) sont en possibilité de lire les données transmises.

On souhaite donc sécuriser les connexions afin que seul l'émetteur et le destinataire puissent avoir connaissance du contenu. D'où un questionnement sur trois aspects :

* Comment chiffrer le contenu des communications afin qu'elles ne soient lisibles que par la source et la destination (garantie de {==**confidentialité**==}) ?
* Comment garantir que le serveur auquel on se connecte est bien celui auquel on pense se connecter (garantie d'{==**authenticité**==}) ?
* Comment s'assurer que le message transmis n'a pas été modifié par un tiers (garantie d'{==**intégrité**==}) ?

Le tout devant bien entendu se faire dans le cadre d'une communication en utilisant l'infrastructure d'Internet, à savoir les communications `TCP/IP` ?

## Quelques définitions nécessaires

!!! infos "Coder/Décoder"

    {==** Coder**==}, c'est représenter l'information par un ensemble de signes prédéfinis. {==**Décoder**==}, c'est interpréter un ensemble de signes pour en extraire l'information qu'ils représentent. 

    Coder et décoder s'emploient lorsqu'il n'y a pas de secret. Par exemple on peut coder/décoder des entiers relatifs par une suite de bits par un «codage en complément à deux».

!!! infos "Cryptographie"
    La {==**cryptographie**==} est une discipline veillant à protéger des messages (pour en assurer la confidentialité, l'authenticité et l'intégrité), par l'intermédiaire de {==**clés de chiffrements**==}.

    La cryptographie est utilisée depuis au moins l'antiquité.

    Son pendant est la {==**cryptanalyse**==}, qui est la technique qui consiste à déduire un texte en clair d’un texte chiffré **sans posséder la clé de chiffrement**. Le processus par lequel on tente de comprendre un message en particulier est appelé {==**une attaque**==}.

    {==**Chiffrer**==} un message, c'est rendre une suite de symboles incompréhensible au moyen d'une **clé de chiffrement**.

    {==**Déchiffrer**==} ou {==**décrypter**==}, c'est retrouver la suite de symboles originale à partir du message chiffré. On utilise **déchiffrer** quand on utilise la clé de chiffrement pour récupérer le texte original, et **décrypter** lorsqu'on arrive à retrouver le message original sans connaitre la clé de chiffrement.



## Cryptographie symétrique

!!! abstract "Cryptographie symétrique"

    On parle de {==**cryptographie symétrique**==} lorsque la même clé est utilisée pour chiffrer et déchiffrer un message.

### Code de César

!!! abstract "Le code (ou chiffre) de César : chiffrement par décalage"

    Le chiffre de César est une méthode de chiffrement très simple utilisée par Jules César dans ses correspondances secrètes (ce qui explique le nom « chiffre de César »). 

    Le texte chiffré est obtenu en remplaçant chaque lettre du texte original par une lettre obtenue par un décalage à distance fixe, toujours du même côté, dans l'ordre de l'alphabet. 

    ![Chiffre Cesar](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caesar3.svg/1280px-Caesar3.svg.png){: style="width:60%; margin:auto;display:block;background-color: #d2dce0;"}
    
    On a ainsi, pour un chiffre de César avec un clé de 3, les correspondances suivantes :

    ``` python
    >>> alphabet_clair = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    >>> alphabet_chiff = "DEFGHIJKLMNOPQRSTUVWXYZABC"
    ```

!!! question "Exercice"

    Afin de pouvoir chiffrer un message avec le code de César, il faut avoir un texte ne comportant que des lettres majuscules de l'alphabet latin, donc nettoyer le texte de tous les accents, espaces, signes de ponctuation, etc. 

    1. Créer une fonction `formate_texte(texte : str) -> str` qui prend en argument un texte non formaté, et renvoie le texte sans accents, sans signes de ponctuations ni espaces, et en majuscule
    2. Créer alors une fonction `code_Cesar(texte :str, cle : int) -> texte` qui renvoie le chiffre de César d'un texte qui lui est passé en argument, avec une clé sous la forme d'un entier entre 1 et 26 qui représente le décalage devant être obtenu. On rappelle les éléments suivants :

    ``` python
    >>> ord('A')
    65
    >> chr(66)
    'B'
    >>> chr(((ord('Z')-65)+3)%26+65)
    'C'
    ```

!!! question "Cryptanalyse d'un chiffre de César"

    === "Enoncé"
        Proposer un texte long chiffré au professeur. Combien de temps va-t-il mettre pour décrypter celui-ci ?

    === "Attaque par force brute"

        Une attaque par force brute consiste à attaquer en testant toutes les possibilités. Avec le chiffre de César, il n'existe que 26 clés différentes, la méthode par force brute est donc particulièrement adaptée, même dans le cas d'un texte long.

        ``` python
        def brute_force_Cesar(texte : str) -> str :
            decrypte = []
            for k in range(1,26) :
                decrypte.append(code_Cesar(texte, k))
            return decrypte
        ```

    === "Attaque par analyse de fréquences"

        Une étude des textes écrits en français montre que la lettre la plus fréquemment utilisée est «E» (minuscule ou majuscule). Si on sait que le texte est écrit en français, il est probable que la lettre la plus fréquente dans le code de César soit celle qui remplace le «E». Il est alors possible de tester en premier la clé correspondant à ce décalage.

        ```python
        def get_freq_texte(texte : str) -> dict :
            dico = dict()
            for letter in texte :
                if letter in dico :
                    dico[letter] += 1
                else :
                    dico[letter] = 1
            return dico

        def attaque_Cesar_analyse_frequence(texte : str) -> str:
            dico = get_freq_texte(texte)
            max_dico = []
            maxi = 0
            for letter in dico :
                if dico[letter]> maxi :
                    max_dico=[letter]
                    maxi = dico[letter]
                elif dico[letter] == maxi :
                    max_dico.append(letter)
            possible_keys = [ord(k)-ord('E') for k in max_dico]
            possible_texts = [ f"Clé {k} :\n\n"+code_Cesar(crypto, 26-k) for k in possible_keys]
            return possible_texts

        ```


??? infos "Chiffre de Vigenère"

    Le chiffre de César est donc très facilement déchiffrable, comme tout chiffrement monoalphabétique (où une lettre est toujours remplacée par le même symbole). Il existe d'autres méthodes de chiffrement par substitution, dits polyalphabétiques, pour lesquels la même lettre n'est pas forcément toujours remplacée par le même symbole, tels que le [chiffre de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re){target="_blank"}. Cependant de telles méthodes ne résiste pas forcément à des [attaques par analyse de fréquences](https://ensip.gitlab.io/programmation_e2/PDF/C_P2A_50_crypto_anafreq.pdf){target="_blank"}.

### Chiffrement XOR 

!!! abstract "XOR ( OU exclusif)"
    L'opérateur binaire `XOR`, où *OU Exclusif*, noté $\oplus$, est un opérateur dont la table de vérité est :

    $$\begin{array}{|c|c|c|}
    \hline
    \oplus & 0 & 1\\\hline
    0 & 0 & 1 \\\hline
    1 & 1 & 0 \\\hline
    \end{array}
    $$

    L'opérateur XOR, en plus d'être *commutatitf* ($A\oplus B = B \oplus A$) possède la propriété de {==**réversibilité**==}, ce qui signifie que si $A \oplus B = C$, alors on a les égalités suivantes :

    * $A \oplus C = B$
    * $B \oplus C = A$

!!! abstract "Chiffrement XOR"

    Étant donné un message, par exemple «UN MESSAGE TRÈS SECRET», et une clé de chiffrement, par exemple «NSI», on recopie plusieurs fois la clé sous le message :

    ```
    UN MESSAGE TRÈS SECRET
    NSINSINSINSINSINSINSIN

    ```
    Chaque caractère du message est associé à une valeur numérique entière (par exemple son Unicode) :

    ```
    85 78 32 77 69 83 83 65 71 69 32 84 82 200 83 32 83 69 67 82 69 84
    78 83 73 78 83 73 78 83 73 78 83 73 78  83 73 78 83 73 78 83 73 78
    ```

    On effectue ensuite l'opération $\oplus$ entre chaque nombre du message et de la clé. par exemple pour le premier caractère :

    $$
    \begin{array}{cccccccccr}
      &0&1&0&1&0&1&0&1&&85\\
    \oplus&0&1&0&0&1&1&1&0&&78\\\hline
    &0&0&0&1&1&0&1&1&&27
    \end{array}
    $$

    Le code obtenu dans notre exemple est donc :

    ```
    27 29 105 3 22 26 29 18 14 11 115 29 28 155 26 110 0 12 13 1 12 26
    ```

    L'opérateur $\oplus$ étant réversible, la réitération de l'opération sur le message chiffré rendra le message original.


!!! question "Chiffré/déchiffré"

    1. Créer une fonction `get_unicode(chaine : str) -> list` qui prend en argument une chaine de caractère et renvoie la liste des codes unicode correspondant aux caractères.
    2. Créer une fonction `get_string(liste : list) -> str` qui fait l'opération inverse de la fonction `get_unicode`.
    3. Créer une fonction `chiffre_XOR(texte : list, cle : list) -> list` qui renvoie une liste de valeurs entières correspondant à l'application d'un `XOR` sur chacun des valeurs des deux listes `texte` et `cle`.

        *Indications :*

        * l'opérateur $\oplus$ en python s'écrit de la manière suivante :

            ```python
            >> 85 ^ 78
            27
            ```
        * Il n'est pas nécessaire de créer une liste de la même longueur que le texte avec la clé. Une utilisation judicieuse de l'opération modulo doit vous permettre de vous en sortir.
    
    4. Vérifiez que la fonction `chiffre_XOR` permet bien de chiffrer/déchiffrer un texte avec une clé donnée.

Les caractéristiques de l'opérateur `XOR`, et le fait qu'il puisse être implémenté directement dans le processeur, font qu'il est souvent utilisé dans les algorithmes de chiffrement modernes, comme [AES](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard){taget="_blank"} ou [ChaCha20](https://en.wikipedia.org/wiki/Salsa20#ChaCha_variant){target="_blank"}. Bien sûr ces algorithmes sont nettement plus complexes que la méthode naïve que nous avons utilisée, mais leurs principes reposent sur des fonctionnements similaires.

!!! warning "Cryptanalyse : attention à la longueur de la clé !"

    Une clé trop courte peut compromettre la sécurité des données : dans le c    

## Sources

[http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/a3_encapsulation_tcp_ip.php](http://www.monlyceenumerique.fr/nsi_premiere/archios_arse/a3_encapsulation_tcp_ip.php)

[https://fr.wikipedia.org/wiki/Three-way_handshake](https://fr.wikipedia.org/wiki/Three-way_handshake)