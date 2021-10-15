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
    chainon = c1
    while chainon.suivant != None :
        chainon = chainon.suivant
    chainon.suivant = c2
    return c1

    
def renverser(chaine) :
    reverse = None
    c= chaine
    while c != None :
        reverse = Chainon(c.valeur, reverse)
        c = c.suivant
    return reverse
        

def renverser(chaine) :
    if chaine == None :
        return None
    else :
        return concatener(renverser(chaine.suivant), Chainon(chaine.valeur, None))


def inserer(v, n, chaine) :
    if n<0 :
        raise IndexError("Invalid index")
    if n == 0 or chaine == None:
        return Chainon(v, chaine)
    else :
        return Chainon(chaine.valeur, inserer(v, n-1, chaine.suivant))
    
def supprimer(n, chaine) :
    if chaine == None :
        raise IndexError("Invalid index")
    if n == 0  :
        return chaine.suivant
    else :
        return Chainon(chaine.valeur, supprimer(n-1, chaine.suivant))
    
def creeDepuisTabV1(tab) :
    """Version pythonesque avec reversed"""
    LC = None
    for e in reversed(tab) :
        LC = Chainon(e, LC)
    return LC
    
def creeDepuisTabV2(tab) :
    """Version avec calcul de l'indice"""
    LC = None
    l = len(tab)
    for i in range(len(tab)):
        LC = Chainon(tab[l-1-i], LC)
    return LC

def creeDepuisTabV3(tab) :
    """Version récursive"""
    if  tab == [] :
        return None
    else :
        return Chainon(tab[0], creeDepuisTabV3(tab[1:]))
    
def creeDepuisTabV4(tab) :
    """Version avec insertion ( mais moins bonne en terme de complexité"""
    LC = None
    for i, v in enumerate(tab) :
        print(i, v)
        LC = inserer(v,i,LC)
    return LC
    

if __name__ == "__main__" :
    chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
    chaine2 = Chainon(13, Chainon(16, None))

