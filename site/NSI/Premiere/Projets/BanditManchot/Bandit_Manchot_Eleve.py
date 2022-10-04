# -*- coding: utf-8 -*-


#### PROJET MACHINE A SOUS
### 1ère NSI Pavie 2022-2023

import random

symboles = '♠♥♦♣7Ω' ## Symboles utilisés dans le bandit-manchot


def choisir_symbole(symboles : str) -> str :
    """
fonction renvoyant un symbole aléatoire parmi une suite de symbole passée en argument
"""
    assert ..., "Bad symbole argument"
    return ...

def fabriquer_chaine(symboles : str, taille : int = 3) -> str :
    """ fonction renvoyant une chaine aléatoire de dimension taille,
à partir de la liste de symbole symboles.
"""
    assert ..., "Bad symbole argument"
    assert ..., 'Bad taille argument'
    ...
    return ...

def compte_symboles_identiques(s : str, chaine: str) -> int :
    """
Fonction renvoyant le nombre d'occurences du symbole s au sein de la chaine chaine
Si le symbole n'est pas présent, renvoie 0

>>> compte_symboles_identiques("a", "abracadabra")
5
>>> compte_symboles_identiques("c", "abracadabra")
1
>>> compte_symboles_identiques("o", "abracadabra")
0
>>> compte_symboles_identiques("a", "")
0
>>> compte_symboles_identiques("", "abracadabra")
0
>>> compte_symboles_identiques("", "")
0
"""
    ...
    return ...

def presence_symboles_identiques_multiples(symboles : str, chaine : str) -> bool :
    """ Fonction renvoyant un booléen True si l'un des symboles présent dans
la chaine symboles est présent plusieurs fois dans la chaine chaine, et False sinon

>>> presence_symboles_identiques_multiples('abc', 'abracadabra')
True
>>> presence_symboles_identiques_multiples('abc', 'abcdef')
False
>>> presence_symboles_identiques_multiples('a', 'aaaa')
True
>>> presence_symboles_identiques_multiples('abc', 'efgh')
False
>>> presence_symboles_identiques_multiples('', 'treytlei')
False
>>> presence_symboles_identiques_multiples('a', '')
False
>>> presence_symboles_identiques_multiples('', '')
False
"""
    ...
    return ...

def table_gain(chaine) :
    """
    Fonction renvoyant le gain selon la chaine passée en argument
    A titre d'information, l'espérance de gain avec la table donnée est de 37.5
>>> table_gain('777')
2000
>>> table_gain('ΩΩΩ')
1000
>>> table_gain('♥♥♥')
500
>>> table_gain('Ω7Ω')
300
>>> table_gain('♠♠7')
100
>>> table_gain('7♠♠')
100
>>> table_gain('♠7♣')
50
>>> table_gain('♠77')
0
    """
    ...
    return ...
    
def saisir_mise(pot : int) -> int :
    """ Fonction récupérant la mise du joueur / de la joueuse,
     qui doit être un nombre entier compris entre 10 et pot.
     Cette fonction ne peut pas être testée par doctest."""
    ...
    return ...
                
def demander_continuer() ->  bool :
    """Fonction demandant au joueur / à la joueuse si il/elle souhaite continuer.
    Le joueur/La joueuse doit pouvoir répondre par oui (ou o) ou par non (ou n),
    et la fonction doit être dumbproof.
    Ne peut pas être testée par doctest.
    """
    ...
    return ...

                
def afficher_bandit(chaine : str, gain : int) -> None:
    """
    Fonction affichant dans la console le bandit-manchot, avec le tirage obtenu.
    Affiche aussi le gain réalisé.
    Renvoie None.
    Ne peut pas être testée par doctest.
    """
    ...


def main_game() -> int :
    """
    Fonction principale du jeu, qui lance une partie, et se poursuiit tant que le joueur /la joueuse
    souhaite ou peut continuer.
    Ne peut pas être testée par doctest.
    """
    presentation()
    ...
    return ...

def presentation() -> None :
    """ fonction affichant la présentation, et donnant les règles du jeu"""
    print("\n"*50)
    print("""
##############################################
#                                            #
#              Bandit Manchot                #
#                                            #
# 1ère NSI 2022-2023                         #
##############################################
""")
    print("\n"*5)
    print("Vous disposez d'un capital de départ de 500 € pour jouer au bandit manchot !")
    print("\n"*2)
    input("(Appuyez sur la touche Entrée...)")


def sauve_score(nom_j : str, score_j: int) -> None :
    """ Fonction sauvant le nom du joueur/de la joueuse, ainsi que son score, dans un fichier texte
nommé HighScore.txt, situé dans le même dossier que ce fichier python
"""
    try :
        with open('HighScore.txt',"r", encoding="utf-8") as f :
            lines = f.readlines()
            hs = [{"nom":"", "score" : 0}]*9
            for i, l in enumerate(lines) :
                nom, score = l.split(" / ")
                try :
                    hs[i] = {"nom" : nom, "score" : int(score)}
                except ValueError :
                    hs[i] = {"nom" : nom, "score" :0}
            is_better_than = len(hs)-1
            while is_better_than>=0 and score_j>hs[is_better_than]['score'] :                    
                if is_better_than != len(hs)-1 :
                    hs[is_better_than+1] = hs[is_better_than]
                hs[is_better_than] = {"nom" : nom_j, "score" : score_j}
                is_better_than -= 1
    except FileNotFoundError :
            hs =[{"nom" : nom_j, "score" : score_j}]
    finally :
        with open("HighScore.txt", "w", encoding="utf8") as f :
            for s in hs :
                if s is not None :
                    f.write(f"{s['nom']} / {s['score']}\n")
                else :
                    f.write(f"Inconnu / 0\n")
                    
def get_score() -> str:
    """ Fonction récupérant les HighScore sauvegardés depuis un fichier HishScore.txt,
et qui renvoie une chaine de caractères correctement formatée pour la console"""
    lines =""
    try :
        with open('HighScore.txt',"r", encoding="utf-8") as f  :
            lines = f.readlines()        
    except FileNotFoundError :
        lines = "Inconnu / 0\n"*9                
    finally :
        HS = [{'nom': line.split(" / ")[0], 'score' : line.split(" / ")[1].replace("\n","")} for line in lines]
    final = ""
    for i,d in enumerate(HS) :
        final +=f"{i+1} {d['nom']:>15} : {d['score']:>10} €\n"
    return final    

## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
    main_game()