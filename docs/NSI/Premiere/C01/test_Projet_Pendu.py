from random import choice
['-', ' ', ')', '!', "'", '.']

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
>>> formateMot('où')
'OU'
>>> formateMot('garçONs')
'GARCONS'
>>> formateMot('àâéèêîôûùç')
'AAEEEIOUUC'
>>> formateMot('')
''
"""
    motFinal = ''
    for l in mot.lower() :
        if l in['é', 'è', 'ê', 'ë'] :
            motFinal += 'e'
        elif l in ['à', 'â', 'ä'] :
            motFinal += 'a'
        elif l =='ô' :
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
* tous les caractères sont suivis d'un espace, y compris le dernier.

>>> genereTirets("Bidules", "Ble")
'B _ _ _ l e _ '
>>> genereTirets("toto", "")
'_ _ _ _ '
>>> genereTirets("bananes", "bn")
'b _ n _ n _ _ '
>>> genereTirets("toto", "ot")
't o t o '
"""
    chaine = ""
    for l in motATrouver :
        if l in lettresUtilisees :
            chaine +=l+" "
        else :
            chaine += "_ "
    return chaine
    
    
def compteRestantes(motATrouver,lettresUtilisees) :
    """ fonction renvoyant le nombre de lettres non encore trouvées
dans le mot, en connaissant les lettres déjà utilisées.
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
"""
    restantes = 0
    for l in motATrouver :
        if l  not in lettresUtilisees :
            restantes +=1
    return restantes
        
def affichePendu(motATrouver, lettresUtilisees, nbEchecs) :
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
    while True :
        lettre = input("Quelle lettre choisissez-vous ? ").upper()
        if len(lettre) == 1 and lettre in [ord(i+65) for i in range(26)] :
            return lettre
        else :
            print("Je ne comprends pas ! Veuillez recommencer !")
    
    
def uneManche() :
    motATrouver = choixMot('liste_francais.txt')
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
    print("""
##############################################
#                                            #
#                Jeu du Pendu                #
#                                            #
# 1ère NSI 2021-2022                         #
##############################################
""")
    
            
def main() :
    while True :
        presentation()
        uneManche()
        rep = input("Vouslez-vous rejouer ? (o/n)")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")
    
            
if __name__ == "__main__" :
    #main()
    import doctest
    doctest.testmod()
            
            
            