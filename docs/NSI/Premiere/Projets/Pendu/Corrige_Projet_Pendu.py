# -*- coding: utf-8 -*-


from random import choice


def choix_mot(adresse_fichier) :
    """ fonction ouvrant un fichier texte dont l'adresse absolue ou relative
    est passée en argument sous la forme d'une chaine de caractères
    et renvoyant une chaine de caractères issue d'une ligne aléatoire du fichier
"""
    with open(adresse_fichier,'r', encoding='utf8') as file :
        mot = choice([m for m in file.readlines()]).replace('\n', '').strip()
    return mot

def formate_mot(mot : str) -> str :
    """ fonction transformant une chaine de caractères accentués
en une chaine de caractères latins stricts (sans accents ni signes diacritiques).
La chaine renvoyée est en majuscule.

>>> formate_mot('tRuC')
'TRUC'
>>> formate_mot('Abécédaire')
'ABECEDAIRE'
>>> formate_mot('')
''
>>> formate_mot('où')
'OU'
>>> formate_mot('garçONs')
'GARCONS'
>>> formate_mot('àâäéèêëîïôöûùüç')
'AAAEEEEIIOOUUUC'
>>> formate_mot('œil')
'OEIL'
>>> formate_mot('Lætitia')
'LAETITIA'
"""
    mot_final = ''
    for lettre in mot.lower() :
        if lettre in ['é', 'è', 'ê', 'ë'] :
            mot_final += 'e'
        elif lettre in ['à', 'â', 'ä'] :
            mot_final += 'a'
        elif lettre in ['ô', 'ö'] :
            mot_final += 'o'
        elif lettre in ['î', 'ï'] :
            mot_final += 'i'
        elif lettre in ['ù', 'û', 'ü'] :
            mot_final += 'u'
        elif lettre == 'ç' :
            mot_final += 'c'
        elif lettre == 'œ' :
            mot_final += 'oe'
        elif lettre == 'æ' :
            mot_final += 'ae'
        elif lettre not in 'abcdefghijklmnopqrstuvwxyz-' :
            raise ValueError(f'{lettre} not in latin alphabet')
        else :
            mot_final += lettre
    return mot_final.upper()

def genere_tirets(mot_a_trouver : str, lettres_utilisees: str ) -> str :
    """ fonction renvoyant une chaine de caractères correspondant
au mot à trouver pour lequel :
* les caractères non présents dans la chaine lettres_utilisees
sont remplacés par des _ (underscores) ;
* les tirets hauts "-" sont conservés ;
* tous les caractères sont suivis d'un espace, y compris le dernier.

>>> genere_tirets("Bidules", "Ble")
'B _ _ _ l e _ '
>>> genere_tirets("toto", "")
'_ _ _ _ '
>>> genere_tirets("bananes", "bn")
'b _ n _ n _ _ '
>>> genere_tirets("toto", "ot")
't o t o '
>>> genere_tirets("pull-over", "plr")
'p _ l l - _ _ _ r '
>>> genere_tirets("pull-over", "pulover")
'p u l l - o v e r '
"""
    chaine = ""
    for lettre in mot_a_trouver :
        if lettre in lettres_utilisees :
            chaine += lettre + " "
        elif lettre == "-" :
            chaine += "- "
        else :
            chaine += "_ "
    return chaine


def compte_restantes(mot_a_trouver : str, lettres_utilisees : str ) -> int :
    """ fonction renvoyant le nombre de lettres non encore trouvées
dans le mot, en connaissant les lettres déjà utilisées.
Un tiret haut "-" ne compte pas dans les lettres à trouver.
La valeur renvoyée est un entier

>>> compte_restantes("bananes","bn")
4
>>> compte_restantes("toto","to")
0
>>> compte_restantes("toto","")
4
>>> compte_restantes("","")
0
>>> compte_restantes("","z")
0
>>> compte_restantes("bidules","bidule")
1
>>> compte_restantes("pull-over", "plr")
4
>>> compte_restantes("pull-over", "pulover")
0

"""
    restantes = 0
    for lettre in mot_a_trouver :
        # le tiret est toujours affiché, il n'est donc jamais "à trouver"
        if lettre not in lettres_utilisees + "-" :
            restantes += 1
    return restantes


def affiche_pendu(mot_a_trouver : str, lettres_utilisees : str, nb_echecs : int) -> None :
    """ fonction affichant à la fois la potence mais aussi le mot
à trouver sous sa forme de tirets
    """
    # chaque partie du corps n'apparait qu'à partir d'un certain nombre d'échecs
    tete = "O" if nb_echecs >= 1 else " "
    torse = "|" if nb_echecs >= 2 else " "
    bras_gauche = "/" if nb_echecs >= 3 else " "
    bras_droit = "\\" if nb_echecs >= 4 else " "
    jambe_gauche = "/" if nb_echecs >= 5 else " "
    jambe_droite = "\\" if nb_echecs >= 6 else " "
    decalage = " " * (2 * len(mot_a_trouver))  # laisse la place au mot à gauche de la potence
    base_pendu = f"""
{decalage}               _ _ _
{decalage}              |     |
{decalage}              {tete}     |
{decalage}            {bras_gauche} {torse} {bras_droit}   |
{decalage}             {jambe_gauche} {jambe_droite}    |
{decalage}                    |
{genere_tirets(mot_a_trouver, lettres_utilisees)}             _______|__
"""
    print(base_pendu)
    print()

def demande_joueur_lettre() -> str:
    """ fonction demandant une lettre latine non accentuée au joueur,
et renvoyant cette lettre en majuscule. La fonction redemande au joueur
tant que celui-ci n'a pas fourni une lettre correcte.
La lettre est renvoyée par la fonction.
"""
    while True :
        lettre = input("Quelle lettre choisissez-vous ? ").upper()
        if len(lettre) == 1 and lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            return lettre
        print("Je ne comprends pas ! Veuillez recommencer !")


def une_manche() -> None :
    """ fonction déclenchant une manche de jeu. On entend par manche de jeu :
* le choix d'un mot dans le fichier 'liste_francais_modifiee.txt' ;
* le formatage de ce mot ;
* puis la répétition de :
    * la demande d'une lettre au joueur ;
    * la mise à jour des lettres utilisées le cas échéant ;
    * la mise à jour de l'affichage
    
    jusqu'à ce que soit le mot complet ait été trouvé,
    soit que le dessin du pendu soit terminé (6 étapes).
    """
    mot_a_trouver = formate_mot(choix_mot('liste_francais_modifiee.txt'))
    print(f"Un mot de langue française de longueur {len(mot_a_trouver)} a été choisi !")
    lettres_utilisees = ''
    nb_echecs = 0
    restantes = len(mot_a_trouver) - mot_a_trouver.count('-')

    # la manche continue tant qu'il reste des lettres ET que le pendu n'est pas terminé
    while restantes > 0 and nb_echecs < 6 :
        lettre_proposee = demande_joueur_lettre()
        if lettre_proposee in lettres_utilisees :
            print()
            print("Lettre déjà proposée !")
        else :
            lettres_utilisees += lettre_proposee
            restantes = compte_restantes(mot_a_trouver, lettres_utilisees)
            if lettre_proposee not in mot_a_trouver :
                nb_echecs += 1
            affiche_pendu(mot_a_trouver, lettres_utilisees, nb_echecs)

    if nb_echecs >= 6 :
        print(f"Vous avez échoué ! Le mot à trouver était : {mot_a_trouver}")
    else :
        print("Bravo, vous avez trouvé le mot !")

def presentation() -> None :
    """ fonction affichant uniquement la présentation"""
    print("""
##############################################
#                                            #
#                Jeu du Pendu                #
#                                            #
# 1ère NSI 2022-2023                         #
##############################################
""")
    
            
def main() -> None:
    """ fonction principale du jeu, permettant d'effectuer plusieurs manches"""
    while True :
        presentation()
        une_manche()
        rep = input("Voulez-vous rejouer ? (o/n)")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")

## La partie ci-dessous n'est effectuée que si vous déclenchez le programme
## en tant que programme principal (notion de modules, vue en terminale)
            
if __name__ == "__main__" :
    
    import doctest
    doctest.testmod()
    main()
