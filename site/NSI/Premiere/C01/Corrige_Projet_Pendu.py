from random import choice


def choixMot(fichier) :
    """ fonction ouvrant un fichier texte et renvoyant une chaine de caractère
aléatoire en minuscule issue d'une ligne quelconque du fichier"""
    with open(fichier,'r', encoding='utf8') as file :
        mot = choice([m for m in file.readlines()]).lower().replace('\n', '')        
    return mot

def formateMot(mot) :
    """ fonction transformant une chaine de caractères accentués
en une chaine de caractère latin strict (sans accents ni signes diacritiques).
La chaine renvoyée est en majuscule.

>>> formateMot('tRuC')
'TRUC'
>>> formateMot('Abécédaire')
'ABECEDAIRE'
>>> formateMot('')
''
>>> formateMot('où')
'OU'
>>> formateMot('garçONs')
'GARCONS'
>>> formateMot('àâäéèêëîïôöûùüç')
'AAAEEEEIIOOUUUC'
>>> formateMot('œil')
'OEIL'
"""
    motFinal = ''
    for l in mot.lower() :
        if l in['é', 'è', 'ê', 'ë'] :
            motFinal += 'e'
        elif l in ['à', 'â', 'ä'] :
            motFinal += 'a'
        elif l in ['ô', 'ö'] :
            motFinal += 'o'
        elif l in ['î', 'ï'] :
            motFinal += 'i'
        elif l in ['ù', 'û', 'ü'] :
            motFinal += 'u'
        elif l == 'ç' :
            motFinal += 'c'
        elif l =='œ' :
            motFinal += 'oe'
        elif l not in [chr(97+i) for i in range(26)]+["-"] :
            print(l)
            raise ValueError(f'{l} not in latin alphabet')
        else :                           
            motFinal+=l
    return motFinal.upper()
    
def genereTirets(motATrouver,lettresUtilisees) :
    """ fonction renvoyant une chaine de caractère correspondant
au mot à trouver pour lequel :
* les caractères non présents dans la chaine lettreUtilisees
sont remplacés par des _ (underscores) ;
* les tirest hauts "-" sont conservés ;
* tous les caractères sont suivis d'un espace, y compris le dernier.

>>> genereTirets("Bidules", "Ble")
'B _ _ _ l e _ '
>>> genereTirets("toto", "")
'_ _ _ _ '
>>> genereTirets("bananes", "bn")
'b _ n _ n _ _ '
>>> genereTirets("toto", "ot")
't o t o '
>>> genereTirets("pull-over", "plr")
'p _ l l - _ _ _ r '
>>> genereTirets("pull-over", "pulover")
'p u l l - o v e r '
"""
    chaine = ""
    for l in motATrouver :
        if l in lettresUtilisees :
            chaine +=l+" "
        elif l =="-" :
            chaine += "- "
        else :
            chaine += "_ "
    return chaine
    
    
def compteRestantes(motATrouver,lettresUtilisees) :
    """ fonction renvoyant le nombre de lettres non encore trouvées
dans le mot, en connaissant les lettres déjà utilisées.
Un tiret haut "-" ne compte pas dans les lettres à trouver.
La valeur renvoyée est un entier

>>> compteRestantes("bananes","bn")
4
>>> compteRestantes("toto","to")
0
>>> compteRestantes("toto","")
4
>>> compteRestantes("","")
0
>>> compteRestantes("","z")
0
>>> compteRestantes("bidules","bidule")
1
>>> compteRestantes("pull-over", "plr")
4
>>> compteRestantes("pull-over", "pulover")
0

"""
    restantes = 0
    for l in motATrouver :
        if l  not in lettresUtilisees+"-" :
            restantes +=1
    return restantes
        
def affichePendu(motATrouver, lettresUtilisees, nbEchecs) :
    """ fonction affichant à la fois la potence mais aussi le mot
à trouver sous sa forme de tirets"""
    a,b,c,d,e,f = " ", " ", " ", " ", " ", " "
    if nbEchecs>=1 :
        a = "O"
    if nbEchecs>=2 :
        b = "|"
    if nbEchecs>=3 :
        c = "/"
    if nbEchecs>=4 :
        d = "\\"
    if nbEchecs>=5 :
        e = "/"
    if nbEchecs>=6 :
        f = "\\"
    basePendu = f"""
{" "*(2*len(motATrouver))}               _ _ _
{" "*(2*len(motATrouver))}              |     |
{" "*(2*len(motATrouver))}              {a}     |
{" "*(2*len(motATrouver))}            {c} {b} {d}   |
{" "*(2*len(motATrouver))}             {e} {f}    |
{" "*(2*len(motATrouver))}                    |
{genereTirets(motATrouver,lettresUtilisees)}             _______|__ 
"""
    print(basePendu)
    print()
    
def demandeJoueurLettre():
    """ fonction demandant une lettre latine non accentuée au joueur,
et renvoyant cette lettre en majuscule. La fonction redemande au joueur
tant que celui-ci n'a pas fourni une lettre correcte.
La lettre est renvoyée en par la fonction.
"""

    while True :
        lettre = input("Quelle lettre choisissez-vous ? ").upper()
        if len(lettre) == 1 and lettre in [chr(i+65) for i in range(26)] :
            return lettre
        else :
            print("Je ne comprends pas ! Veuillez recommencer !")
    
    
def uneManche() :
    """ fonction déclenchant une manche de jeu. On entend par manche de jeu :
* le choix d'un mot dans le fichier 'liste_francais_modifiee.txt' ;
* le formatage de ce mot ;
* puis la répétitions de :
    * la demande d'une lettre au joueur ;
    * la mise à jour des lettres utilisée le cas échéant ;
    * la mise à jour de l'affichage
    
    jusqu'à ce que soit le mot complet ait été trouvé,
    soit que le dessin du pendu soit terminé (6 étapes).
    """
    motATrouver = choixMot('liste_francais_modifiee.txt')
    motATrouver = formateMot(motATrouver)
    print(f"Un mot de langue française de longueur {len(motATrouver)} a été choisi !")
    lettresUtilisees = ''
    nbEchecs = 0
    continuer = True
    
    while continuer :
        lettreProposee = demandeJoueurLettre()
        if  lettreProposee not in lettresUtilisees :
            lettresUtilisees += lettreProposee
            restantes = compteRestantes(motATrouver, lettresUtilisees)
            if lettreProposee in motATrouver :
                if restantes ==0 :
                    continuer = False
            else :
                nbEchecs +=1
                if nbEchecs >=6 :
                    continuer = False
            affichePendu(motATrouver, lettresUtilisees, nbEchecs)            
        else :
            print()
            print("Lettre déjà proposée !")
    if nbEchecs >=6 :
        print(f"Vous avez échoué ! Le mot à trouver était : {motATrouver}")
        
def presentation() :
    """ fonction affichant uniquement la présentation"""
    print("""
##############################################
#                                            #
#                Jeu du Pendu                #
#                                            #
# 1ère NSI 2021-2022                         #
##############################################
""")
    
            
def main() :
    """ fonction principale du jeu, permettant d'effectuer plusieurs manches"""
    while True :
        presentation()
        uneManche()
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
            
            
            