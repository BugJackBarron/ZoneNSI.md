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

def table_gain(chaine) :
    """ Espérance de gain = 37.5"""
    if chaine == "777" :
        return 2000
    elif chaine == "ΩΩΩ" :
        return 1000
    elif chaine in ['♠'*3, '♥'*3, '♦'*3, '♣'*3] :
        return 500
    elif '7' in chaine and presence_symboles_identiques_multiples('Ω', chaine) :
        return 300
    elif '7' in chaine and presence_symboles_identiques_multiples('♠♥♦♣', chaine) :
        return 100
    elif not presence_symboles_identiques_multiples('♠♥♦♣7Ω', chaine) :
        return 50
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


def main_game() :
    pot = 500
    continuer = True 
    while continuer :
        print("\n"*50)
        mise = saisir_mise(pot)
        pot = pot - mise
        resultat = fabriquer_chaine(symboles)
        gain = table_gain(resultat)
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
    
    
    
