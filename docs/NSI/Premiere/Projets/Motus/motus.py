# -*- coding: utf-8 -*-


from random import choice
import doctest


def choix_mots(adresse_fichier, longueur_mot = 6) :
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractère
    et renvoyant une liste de mots non accentués et sans autres signes
"""
    with open(adresse_fichier,'r', encoding='utf8') as file :
        mot = [m.replace('\n', '').strip() for m in file.readlines()]
        mot = [m.upper() for m in mot if len(m) == longueur_mot]
    return mot

LISTE_MOTS = choix_mots('liste_francais_modifiee.txt', 6)


####


def demande_mot(first_letter : str, length :int = 6) -> str:
    assert type(first_letter) == str and len(first_letter) == 1 and first_letter.isupper()
    assert type(length) == int and length>1
    while True :
        mot = input(f"Entrez un mot commençant par {first_letter} de {length} lettres : ").upper().strip()
        if  len(mot)== length and mot.upper() in LISTE_MOTS:
            return mot
        print("Mot incompatible, veuillez recommencer")
        
def teste_mot (mot : str, cible : str) -> str :
    sortie = ""
    dec_cible = [l for l in cible.upper()]
    for i in range(len(mot)) :
        if mot[i].upper() == cible[i].upper() :
            sortie += mot[i].upper()
            dec_cible.remove(mot[i].upper())
        elif mot[i].upper() in dec_cible :
            sortie += mot[i].lower()
            dec_cible.remove(mot[i].upper())
        else :
            sortie += "."
    return sortie

def main() :
    a_trouver = choice(LISTE_MOTS)
    victoire = False
    nb_essais = 0
    print(f"---> {a_trouver[0]}.....")
    while not(victoire) and nb_essais <7 :
        nb_essais += 1
        proposition = demande_mot(a_trouver[0])
        if proposition == a_trouver :
            victoire = True
            print(f"Bravo !!!! Vous avez trouvé en {nb_essais} !")
        else :
            print(f"Essai {nb_essais} ---> {teste_mot(proposition, a_trouver)}")
    if not(victoire) :
        print(f"Il fallait trouver le mot ---> {a_trouver} !")
        
if __name__ == "__main__" :
    doctest.testmod()
    while True :
        main()
        encore = input("Voulez-vous rejouer ?")
        if encore not in ['o', 'oui', 'y', 'yes'] :
            break
    
    
    
    ure