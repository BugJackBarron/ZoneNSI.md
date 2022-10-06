#### PROJET MACHINE A SOUS

import random

symboles = '♠♥♦♣7Ω'


def choisir_symbole(symboles : str) -> str :
    assert type(symboles) == str and len(symboles)>0, "Bad argument"
    return random.choice(symboles)

def fabriquer_chaine(symboles : str, taille : int = 3) -> str :
    assert type(symboles) == str and len(symboles)>0, "Bad argument"
    assert type(taille) == int and taille>0, 'Bad argument taille'
    chaine = ""
    for _ in range(taille) :
        chaine += choisir_symbole(symboles)
    return chaine

def compte_symboles_identiques(s : str, chaine: str) -> int :
    compteur = 0
    for c in chaine  :
        if c == s :
            compteur += 1
    return compteur

def presence_symboles_identiques_multiples(symboles : str, chaine : str) -> bool :
    for s in symboles :
        if compte_symboles_identiques(s, chaine)>1 :
            return True
    return False

def table_gain(chaine, mise) :
    """
renvoie les gains

>>> table_gain('777', 20)
2000
>>> table_gain('ΩΩΩ', 20)
1000
>>> table_gain('♥♥♥', 10)
500
>>> table_gain('Ω7Ω', 15)
300
>>> table_gain('♠♠7', 10)
100
>>> table_gain('7♠♠', 10)
100
>>> table_gain('♠7♣', 25)
50
>>> table_gain('♠77', 50)
0
"""
    if chaine == "777" :
        return 100*mise
    elif chaine == "ΩΩΩ" :
        return 50*mise
    elif chaine in ['♠'*3, '♥'*3, '♦'*3, '♣'*3] :
        return 20*mise
    elif '7' in chaine and presence_symboles_identiques_multiples('Ω', chaine) :
        return 10*mise
    elif '7' in chaine and presence_symboles_identiques_multiples('♠♥♦♣', chaine) :
        return 5*mise
    elif not presence_symboles_identiques_multiples('♠♥♦♣7Ω', chaine) :
        return 2*mise
    else :
        return 0
    
def saisir_mise(pot : int) -> int :
    while True :
        mise = input(f"Entrez une mise entre 10 et {pot} :")
        try :
            mise = int(mise)
        except ValueError :
            print("Votre saisie est incorrecte, recommencez")
        else :
            if 10 <= mise <= pot :
                return mise
            else :
                print(f"Votre mise n'est pas entre 10 et {pot} !")
                
def demander_continuer() ->  bool :
    while True :
        reponse = input(f"Voulez-vous rejouer ? O/N")
        if reponse.lower() in ['y', 'o', 'yes', 'oui', 'da']  :
            return True
        elif reponse.lower() in ['n', 'non', 'no', 'niet'] :
            return False
        else :
            print(f"Je ne comprends pas \"{reponse}\" !!!")

                
def afficher_bandit(chaine, gain) :
    
    print(f"""
-------------
|   |   |   |    o
| {chaine[0]} | {chaine[1]} | {chaine[2]} |   //
|   |   |   |  //
------------- //

Vous gagnez {gain} €
""")
    
    
def demande_nom() -> str :
    while True :
        nom = input("Entrez votre nom : ")
        if len(nom)<15 and len(nom)>0 :
            return nom
        print("Veuillez recommencer et saisir un nom de taille comprise entre 1 et 14")
    
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


def main_game() :
    presentation()
    pot = 500
    continuer = True 
    while continuer :
        print("\n"*50)
        mise = saisir_mise(pot)
        pot = pot - mise
        resultat = fabriquer_chaine(symboles)
        gain = table_gain(resultat, mise)
        pot += gain
        afficher_bandit(resultat, gain)
        print(f"Votre pot actuel est de {pot} €")
        if pot != 0 :
            continuer = demander_continuer()
            if pot<500 :
                print(f"Merci de votre visite ! Vous repartez avec {500-pot} € de moins")
            elif pot == 500 :
                print("Merci de votre visite ! Vous n'avez ni gagné ni perdu !")
            else :
                print(f"Merci de votre visite ! Vous avez gagné {pot-500} € !")
            
        else :
            continuer = False
            print("Vous ne pouvez plus jouer ! Le casino vous dit merci !")
    if pot>0 :
        sauve_score(demande_nom(), pot)
    print(get_score())
            
    
    
def sauve_score(nom_j, score_j):
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
                    
def get_score() :
    liçnes =""
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
                

if __name__ == "__main__" :
    import doctest
    doctest.testmod()
    main_game()
            
        
        
            
        
        