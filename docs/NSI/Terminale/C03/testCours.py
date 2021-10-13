import random
tab = [random.randint(1,100) for _ in range(10)]


class Chainon :
    """Chainon d'une liste chainée"""
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        
def longueur(chaine) :
    if chaine == None :
        return 0
    else :
        return 1+longueur(chaine.suivant)
    
def longueurI(chaine) :
    l = 0
    c = chaine
    while c != None :
        l+=1
        c = c.suivant
    return l
        
chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
print(longueur(chaine))