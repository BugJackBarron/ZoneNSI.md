from random import choice


def choixMot(fichier) :
    with open(fichier,'r', encoding='utf8') as file :
        mot = choice([m for m in file.readlines()]).lower().replace('\n', '')        
    return mot

def formateMot(mot) :
    motFinal = ''
    for l in mot :
        if l in['é', 'è', 'ê'] :
            motFinal += 'e'
        elif l in ['à', 'â'] :
            motFinal += 'a'
        elif l =='ô' :
            motFinal += 'o'
        elif l == 'î' :
            motFinal += 'i'
        elif l in ['ù', 'û'] :
            motFinal += 'u'
        elif l == 'ç' :
            motFinal += 'c'
        elif l not in [chr(97+i) for i in range(26)] :
            print(l)
            raise ValueError('not in latin alphabet')
        else :                           
            motFinal+=l
    return motFinal.upper()
    
def afficheMot(motATrouver,lettresUtilisees) :
    for l in motATrouver :
        if l in lettresUtilisees :
            print(l+" ", end="")
        else :
            print("_ ", end="")
    
def compteRestantes(motATrouver,lettresUtilisees) :
    restantes = 0
    for l in motATrouver :
        if l  not in lettresUtilisees :
            restantes +=1
    return restantes
        
def affichePendu(nbEchecs) :
    print(f"Nombre d'echecs : {nbEchecs}")
    
def demandeJoueurLettre():
    return input("Lettre :").upper()
    
def uneManche() :
    motATrouver = choixMot('liste_francais.txt')
    motATrouver = formateMot(motATrouver)    
    lettresUtilisees = ''
    nbEchecs = 0
    continuer = True
    while continuer :
        lettreProposee = demandeJoueurLettre()
        if  lettreProposee not in lettresUtilisees :
            lettresUtilisees += lettreProposee
            afficheMot(motATrouver, lettresUtilisees)
            restantes = compteRestantes(motATrouver, lettresUtilisees)
            if lettreProposee in motATrouver :                
                if restantes ==0 :
                    continuer = False
            else :
                nbEchecs +=1
                affichePendu(nbEchecs)
                if nbEchecs >10 :
                    continuer = False
                    print(f"Vous avez perdu, le mot à découvrir était :{motATrouver}")
        else :
            print()
            print("Lettre déjà proposée")
            
def main() :
    while True :
        uneManche()
        rep = input("Vouslez-vous rejouer ? (o/n)")
        if rep.lower() not in ['o', 'oui', 'y', 'yes'] :
            break
    print("Au revoir !")
    
            
if __name__ == "__main__" :
    main()
            
            
            