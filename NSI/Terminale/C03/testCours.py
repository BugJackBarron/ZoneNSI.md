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
    if chaine == None or n<0:
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

def occurences(valeur, chaine) :
    if chaine.suivant == None :
        return 0
    if chaine.valeur == valeur :
        return 1+ occurence(valeur, chaine.suivant)
    else :
        return occurence(valeur, chaine.suivant)
        

def occurencesI(valeur, chaine) :
    nbOcc = 0
    while chaine != None :
        if chaine.valeur == valeur :
            nbOcc +=1
        chaine = chaine.suivant
    return nbOcc

def premiereOccurence(valeur, chaine) :
    
    def pOccR(valeur, chaine) :
        if chaine == None :
            return False, -1
        if chaine.valeur == valeur :
            return True, 0
        else :
            status, indice = pOccR(valeur, chaine.suivant)
            return status, 1+ indice
        
    status, indice = pOccR(valeur, chaine)
    if status :
        return indice
    else :
        return -1

def premiereOccurenceI(valeur, chaine) :
    indice = 0
    while chaine != None :
        if chaine.valeur == valeur :
            return indice
        else :
            indice = indice+1
            chaine = chaine.suivant
    return -1

def identique (c1, c2) :
    
    def idR(c1, c2) :
        if c1 == None and c2 == None :
            return True
        if c1.valeur == c2.valeur :
            return idR(c1.suivant, c2.suivant)
        else :
            return False
        
    if longueur(c1)!=longueur(c2)  :
        return False
    else :
        return idR(c1,c2)

class ListeC :
    """A real docstring here"""
    
    def __init__(self) :
        self.head = None
        
    def is_empty(self) :
        return self.head == None
        
    def push(self, v) :
        self.head = Chainon(v, self.head)
        
    def pop(self) :
        self.head = self.head.suivant
    
        
    def __str__(self) :
        return str(self.head)
    
    def __len__(self) :
        if self.head == None :
            return 0
        else :
            return longueur(self.head)
            
    def __getitem__(self, i) :
        return niemeElement(self.head, i)
        
    def __add__(self, other) :
        if not isinstance(other, ListeC) :
            raise TypeError(f"Unable to add ListeC object with {type(other)} object")
        result = ListeC()
        result.head = concatener(self.head, other.head)
        return result
    
    def __eq__(self, other) :
        if not isinstance(other, ListeC) :
            raise TypeError(f"Unable to compare ListeC object with {type(other)} object")
        return identique(self.head, other.head)
    

if __name__ == "__main__" :
    chaine = Chainon(21, Chainon(15, Chainon( 45, None)))
    chaine2 = Chainon(13, Chainon(16, None))
    creeDepuisTabV1([1,2,3,4])
    print(premiereOccurenceI(15, creeDepuisTabV1([12,15,18,24,18,42,36])))
    
