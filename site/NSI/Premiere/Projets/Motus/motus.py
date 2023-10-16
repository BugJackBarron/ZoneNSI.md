# -*- coding: utf-8 -*-


from random import choice

def choix_mot(adresse_fichier) :
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractère
    et renvoyant une chaine de caractère issue d'une ligne aléatoire du fichier
"""
    with open(adresse_fichier,'r', encoding='utf8') as file :
        mot = [m.replace('\n', '').strip() for m in file.readlines()]
        mot = [m.upper() for m in mot if len(m) == 6]
    return mot

def demande_mot(first_letter : str, length :int = 6) -> str:
    assert type(first_letter) == str and len(first_letter) == 1 and first_letter.is_upper()
    assert type(length) == int and length>1
    while True :
        mot = input("Entrez un mot commençant par {first_letter} de {length} lettres : ").upper().strip()
        if  len(mot)== length :
            return mot
        print("Mot incompatible, veuillez recommencer")
        

        
    