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

class Pile :
    """interface de pile"""
    def __init__(self) :
        self.tete = None

    def est_vide(self) :
        return self.tete == None

    def empiler(self, v) :
        self.tete = ChainonPile(v, self.tete)

    def depiler(self) :
        v = self.tete.valeur
        self.tete = self.tete.suivant
        return v
    
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
        return self.sorties.depiler()
