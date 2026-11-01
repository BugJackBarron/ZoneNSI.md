# -*- coding: utf-8 -*-


#### PROJET MOTUS (corrigé)
### 1ère NSI

from random import choice

LONGUEUR_MOT = 6    ## Nombre de lettres des mots à trouver
NB_ESSAIS_MAX = 6   ## Nombre maximal de propositions par manche


def charge_mots(adresse_fichier : str, longueur_mot : int = LONGUEUR_MOT) -> list :
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractères
    et renvoyant la liste des mots (en majuscules) de ce fichier
    qui ne contiennent que des lettres et qui ont la longueur demandée.
"""
    with open(adresse_fichier, 'r', encoding='utf8') as file :
        mots = [m.replace('\n', '').strip().upper() for m in file.readlines()]
    return [m for m in mots if len(m) == longueur_mot and m.isalpha()]


def choisir_mot(mots : list) -> str :
    """ fonction renvoyant un mot choisi au hasard dans la liste mots.

>>> choisir_mot(['BANANE'])
'BANANE'
>>> choisir_mot(['BANANE', 'CARTES', 'BANDES']) in ['BANANE', 'CARTES', 'BANDES']
True
"""
    assert type(mots) == list and len(mots) > 0, "mots must be a non-empty list"
    return choice(mots)


def mot_valide(proposition : str, premiere_lettre : str, longueur : int, mots : list) -> bool :
    """ fonction renvoyant True si la proposition (en majuscules) est une proposition
recevable, c'est-à-dire si elle vérifie les trois conditions suivantes :
* elle a la longueur demandée ;
* elle commence par la lettre premiere_lettre ;
* elle fait partie de la liste de mots mots.
Renvoie False sinon.

>>> liste = ['BANANE', 'BANDES', 'CARTES']
>>> mot_valide('BANDES', 'B', 6, liste)
True
>>> mot_valide('CARTES', 'B', 6, liste)
False
>>> mot_valide('BANANES', 'B', 6, liste)
False
>>> mot_valide('BANANO', 'B', 6, liste)
False
>>> mot_valide('', 'B', 6, liste)
False
"""
    return (len(proposition) == longueur
            and proposition[0] == premiere_lettre
            and proposition in mots)


def demande_proposition(premiere_lettre : str, longueur : int, mots : list) -> str :
    """ fonction demandant au joueur / à la joueuse un mot, et le redemandant tant
que la proposition n'est pas recevable (voir fonction mot_valide).
Le mot saisi peut l'être en minuscules, mais il est renvoyé en majuscules.
Un message d'erreur doit expliquer pourquoi la proposition est refusée.
Ne peut pas être testée par doctest.
"""
    while True :
        proposition = input(f"Entrez un mot de {longueur} lettres commençant par {premiere_lettre} : ").upper().strip()
        if len(proposition) != longueur :
            print(f"Mauvaise longueur ({longueur} lettres attendues)")
        elif proposition[0] != premiere_lettre :
            print(f"Le mot doit commencer par {premiere_lettre}")
        elif not mot_valide(proposition, premiere_lettre, longueur, mots) :
            print("Mot inconnu")
        else :
            return proposition


def teste_mot(proposition : str, cible : str) -> str :
    """ fonction comparant une proposition au mot à trouver (tous deux en majuscules,
et de même longueur) et renvoyant une chaine de caractères de même longueur dans laquelle :
* une lettre bien placée est écrite en MAJUSCULE ;
* une lettre présente dans le mot mais mal placée est écrite en minuscule ;
* une lettre absente du mot est remplacée par un point.

Attention : une lettre de la cible ne peut "servir" qu'une seule fois !
Une lettre bien placée est prioritaire sur une lettre mal placée.

>>> teste_mot('BANANE', 'BANANE')
'BANANE'
>>> teste_mot('CHIENS', 'BANANE')
'...eN.'
>>> teste_mot('BRAVOS', 'BANANE')
'B.a...'
>>> teste_mot('ALLONS', 'BALLES')
'alL..S'
>>> teste_mot('LLLLLL', 'BALLES')
'..LL..'
>>> teste_mot('AAAAAA', 'BANANE')
'.A.A..'
"""
    assert len(proposition) == len(cible), "proposition and cible must have the same length"
    sortie = ["."] * len(cible)
    lettres_restantes = []   # lettres de la cible qui n'ont pas été trouvées à la bonne place
    # 1er passage : les lettres bien placées sont prioritaires
    for i in range(len(cible)) :
        if proposition[i] == cible[i] :
            sortie[i] = proposition[i]
        else :
            lettres_restantes.append(cible[i])
    # 2e passage : les lettres mal placées, dans la limite des lettres restantes
    for i in range(len(cible)) :
        if sortie[i] == "." and proposition[i] in lettres_restantes :
            sortie[i] = proposition[i].lower()
            lettres_restantes.remove(proposition[i])   # une lettre ne sert qu'une fois
    return "".join(sortie)


def affiche_essais(resultats : list, premiere_lettre : str, nb_essais_max : int, longueur : int) -> None :
    """ fonction affichant dans la console la grille de jeu :
* une ligne par essai déjà effectué, qui contient le résultat renvoyé par teste_mot ;
* puis une ligne pour chaque essai restant, qui ne contient que la première lettre
du mot suivie de points.
Les caractères de chaque ligne sont séparés par des espaces.
Ne peut pas être testée par doctest.

Par exemple, après deux essais, pour un jeu de 6 essais maximum avec des mots de 6 lettres :

B . a . . .
B A N D . .
B . . . . .
B . . . . .
B . . . . .
B . . . . .
"""
    for resultat in resultats :
        print(" ".join(resultat))
    for _ in range(nb_essais_max - len(resultats)) :
        print(" ".join(premiere_lettre + "." * (longueur - 1)))


def calcule_score(nb_essais : int, victoire : bool) -> int :
    """ fonction renvoyant le score obtenu à l'issue d'une manche :
* 0 point si le mot n'a pas été trouvé ;
* sinon 100 points par essai non utilisé, plus 100 points (donc 600 points
pour un mot trouvé du premier coup avec 6 essais maximum, et 100 points
pour un mot trouvé au dernier essai).

>>> calcule_score(1, True)
600
>>> calcule_score(4, True)
300
>>> calcule_score(6, True)
100
>>> calcule_score(6, False)
0
"""
    if not victoire :
        return 0
    return 100 * (NB_ESSAIS_MAX - nb_essais + 1)


def une_manche(mots : list) -> int :
    """ fonction déclenchant une manche de jeu. On entend par manche de jeu :
* le choix d'un mot dans la liste mots ;
* l'affichage de la première lettre de ce mot (et JAMAIS du mot complet !) ;
* puis la répétition de :
    * la demande d'une proposition au joueur / à la joueuse ;
    * l'ajout du résultat de teste_mot à la liste des essais ;
    * la mise à jour de l'affichage (fonction affiche_essais) ;
jusqu'à ce que soit le mot ait été trouvé, soit que le nombre maximal
d'essais NB_ESSAIS_MAX soit atteint.
La fonction affiche un message de victoire ou de défaite (en donnant le mot
à trouver), et renvoie le score de la manche (voir fonction calcule_score).
Ne peut pas être testée par doctest.
"""
    cible = choisir_mot(mots)
    resultats = []
    victoire = False
    print(f"Le mot commence par {cible[0]}")
    while not victoire and len(resultats) < NB_ESSAIS_MAX :
        proposition = demande_proposition(cible[0], len(cible), mots)
        resultats.append(teste_mot(proposition, cible))
        victoire = (proposition == cible)
        affiche_essais(resultats, cible[0], NB_ESSAIS_MAX, len(cible))
    if victoire :
        print(f"Bravo !!!! Vous avez trouvé en {len(resultats)} essai(s) !")
    else :
        print(f"Perdu ! Il fallait trouver le mot ---> {cible} !")
    return calcule_score(len(resultats), victoire)


def presentation() -> None :
    """ fonction affichant uniquement la présentation"""
    print("""
##############################################
#                                            #
#                   MOTUS                    #
#                                            #
# 1ère NSI                                   #
##############################################
""")
    print("Trouvez le mot de 6 lettres en 6 essais !")
    print("  * LETTRE MAJUSCULE : la lettre est bien placée ;")
    print("  * lettre minuscule : la lettre est dans le mot, mais mal placée ;")
    print("  * point            : la lettre n'est pas dans le mot.")
    print()


def sauve_score(nom_j : str, score_j : int) -> None :
    """ Fonction sauvant le nom du joueur/de la joueuse, ainsi que son score, dans un fichier texte
nommé HighScore.txt, situé dans le même dossier que ce fichier python.
Seuls les 10 meilleurs scores sont conservés. Le fichier est créé s'il n'existe pas.
"""
    hs = []
    try :
        with open('HighScore.txt', "r", encoding="utf-8") as f :
            for ligne in f :
                if ligne.strip() == "" :
                    continue
                nom, score = ligne.rsplit(" / ", 1)
                try :
                    hs.append({"nom" : nom, "score" : int(score)})
                except ValueError :
                    hs.append({"nom" : nom, "score" : 0})
    except FileNotFoundError :
        pass
    hs.append({"nom" : nom_j, "score" : score_j})
    hs.sort(key=lambda d : d['score'], reverse=True)  # tri stable : à égalité, l'ancien score reste devant
    with open("HighScore.txt", "w", encoding="utf-8") as f :
        for d in hs[:10] :
            f.write(f"{d['nom']} / {d['score']}\n")


def get_score() -> str :
    """ Fonction récupérant les HighScore sauvegardés depuis un fichier HighScore.txt
(créé s'il n'existe pas), et qui renvoie une chaine de caractères correctement formatée pour la console.
"""
    try :
        with open('HighScore.txt', "r", encoding="utf-8") as f :
            lines = [l for l in f.readlines() if l.strip() != ""]
    except FileNotFoundError :
        with open('HighScore.txt', "w", encoding="utf-8") as f :
            pass  # création d'un fichier vide
        lines = ["Inconnu / 0\n"]*10
    final = ""
    for i, line in enumerate(lines) :
        nom, score = line.rsplit(" / ", 1)
        final += f"{i+1} {nom:>15} : {score.strip():>10} points\n"
    return final


def main() -> None :
    """ fonction principale du jeu, permettant d'effectuer plusieurs manches
    et de cumuler les scores de ces manches"""
    presentation()
    mots = charge_mots('liste_francais_modifiee.txt', LONGUEUR_MOT)
    score_total = 0
    while True :
        score_total += une_manche(mots)
        print(f"Votre score total est de {score_total} points.")
        rep = input("Voulez-vous rejouer ? (o/n) ")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")

    # Partie facultative : sauvegarde du High Score
    if input("Voulez-vous sauvegarder votre score ? (o/n) ").lower() in ['o', 'oui', 'y', 'yes'] :
        nom = ""
        while nom == "" or " / " in nom :
            nom = input("Votre nom : ").strip()
        sauve_score(nom, score_total)
        print(get_score())


## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
    main()
