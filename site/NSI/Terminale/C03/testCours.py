import random
tab = [random.randint(1,100) for _ in range(10)]


class Chainon :
    """Chainon d'une liste chainée"""
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        

    def __str__(self)  :
        return f"{self.valeur}->{str(self.suivant)}"
        

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


def niemeElement(chaine, i) :
    if chaine == None or i<0:
        raise IndexError("Invalid index")
    if i == 0 :
        return chaine.valeur
    else :
        return niemeElement(chaine.suivant, i-1)

def concatener(c1, c2) :
    if c1 == None :
        return c2
    else :
        return Chainon(c1.valeur,concatener(c1.suivant, c2))



def concatenerI(c1, c2) :
    """Non fonctionnel"""
    if c1 == None :
        return c2
    else :
        newc = Chainon(c1.valeur, None)
        while c1.suivant != None :
            newc.suivant = Chainon(c1.suivant.valeur, None)
            newc = newc.suivant
            c1 = c1.suivant
        newc.suivant = c2
        return newc
        
chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
chaine2 = Chainon(13, Chainon(16, None))

