class PileList :
    """Pile crée à partir du type list"""
    def __init__(self) :
        self.pile =  []

    def est_vide(self) :
        return self.pile == []

    def empiler(self, v) :#
        self.pile.append(v)

    def depiler(self) :#pop
        if self.est_vide() :
            raise IndexError("Erreur : dépiler une pile vide")
        return self.pile.pop()


class ChainonPile :
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        
    def __str__(self) :
        return f"\n  {self.valeur}  \n  __  \n  {str(self.suivant)}\n  "
    
def longueur(chaine) :
    if chaine == None :
        return 0
    else :
        return 1 + longueur(chaine.suivant)

class Pile :
    """interface de pile"""
    def __init__(self) :
        self.tete = None
        self._taille = 0

    def est_vide(self) :
        return self.tete == None

    def empiler(self, v) :
        self.tete = ChainonPile(v, self.tete)
        self._taille += 1

    def depiler(self) :
        v = self.tete.valeur
        self.tete = self.tete.suivant
        self._taille -= 1
        return v
    
    def vider(self) :
        self.tete = None
        self._taille = 0
        
    def consulter(self):
        return self.tete.valeur
    
    def taille(self) :
        return self._taille
    
    
    def __str__(self) :
        return str(self.tete)

class ChainonFile :
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        
    def __str__(self) :
        return f"{str(self.suivant)}  ->  {self.valeur}"


class FileLC :
    """interface de file"""
    def __init__(self) :
        self.tete = None                
        self.queue = None

    def est_vide(self) :
        return self.tete == None and self.queue == None

    def enfiler(self, v) :
        nc = ChainonFile(v, None)
        if self.est_vide() :
            self.tete = nc
        else :            
            self.queue.suivant = nc
        self.queue = nc

    def defiler(self) :
        if self.est_vide() :
            raise IndexError("Unable to dequeue from empty queue")
        v = self.tete.valeur
        self.tete = self.tete.suivant
        return v
    
    def __str__(self) :
        return str(self.tete)
    
    
class File :
    def __init__(self) :
        self.entrees = Pile()
        self.sorties = Pile()

    def est_vide(self) :
        return self.entrees.est_vide() and self.sorties.est_vide()

    def enfiler(self, v) :
        self.entrees.empiler(v)

    def defiler(self) :
        if self.est_vide() :
            raise IndexError("Unable to dequeue empty queue")
        while not(self.entrees.est_vide()) :
            self.sorties.empiler(self.entrees.depiler())
        return self.sorties.depiler()


def NPI(chaine) :
    operandes = chaine.split(" ")
    pile = Pile()
    for op in operandes :
        if op not in ["+","-","*"] :
            pile.empiler(int(op))
        else :
            nb1 = pile.depiler()
            nb2 = pile.depiler()
            if op == "+" :
                pile.empiler(nb2+nb1)
            elif op == "-" :
                pile.empiler(nb2-nb1)
            elif op == "*" :
                pile.empiler(nb2*nb1)
    return pile.depiler()


def NPIeval(chaine) :
    operandes = chaine.split(" ")
    pile = Pile()
    for op in operandes :
        if op not in ["+","-","*"] :
            pile.empiler(int(op))
        else :
            nb1 = pile.depiler()
            nb2 = pile.depiler()
            pile.empiler(eval(f"{nb2}{op}{nb1}"))
    return pile.depiler()



def searchIndexNext(string, baseIndex) :
    if string[baseIndex] not in "({[" :
        raise IndexError("Not a good Index")
    symb ={'(' :')', '[' : ']', '{' : '}'}
    imbrication = 0
    for i,c in enumerate(string[baseIndex+1:]) :
        if c == string[baseIndex] :
            imbrication +=1
        elif c == symb[string[baseIndex]] :
            if imbrication !=0 :
                imbrication -= 1
            else :
                return baseIndex+1+i
    raiseValueError("Invalid string")


















