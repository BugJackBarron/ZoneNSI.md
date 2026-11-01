# -*- coding: utf-8 -*-
"""Construit liste_francais_modifiee.txt à partir de liste_francais.txt.

Un mot est conservé s'il ne contient que :
* des lettres latines (non accentuées) ;
* des lettres accentuées ;
* des cédilles ;
* des lettres combinées (œ, æ) ;
* des tirets.
Tous les autres mots (contenant espaces, apostrophes, points, parenthèses,
points d'exclamation, ...) sont supprimés.
"""

LETTRES_AUTORISEES = set("abcdefghijklmnopqrstuvwxyz"
                         "àâäéèêëîïôöûùüÿç"
                         "œæ"
                         "-")

with open('liste_francais.txt', 'r', encoding='utf8') as file :
    mots = [ligne.strip() for ligne in file.readlines()]

# on compare en minuscules pour accepter aussi les majuscules (et les majuscules accentuées)
liste_finale = [mot for mot in mots
                if mot != "" and all(lettre in LETTRES_AUTORISEES for lettre in mot.lower())]

with open('liste_francais_modifiee.txt', 'w', encoding='utf8') as file :
    for mot in liste_finale :
        file.write(mot + "\n")

print(f"{len(liste_finale)} mots conservés sur {len(mots)}.")
