INDENTATION = "--"


def hauteur(t) :
    if t is None :
            return 0
    return 1 + max(hauteur(t.gauche), hauteur(t.droit))

#### CLASS NODE ####

class Node :
    def __init__(self, valeur, gauche = None, droit = None, parent = None) :
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        self.parent = parent
        
    def estFeuille(self) :
        return self.gauche is None and self.droit is None
    
    def toString(self, shift) :
        representation = shift + str(self.valeur)+"\n"
        if self.estFeuille() :
            return representation
        if self.gauche is None :
            representation += shift + INDENTATION +"X\n"
        else :
            representation += self.gauche.toString(shift+INDENTATION)
        if self.droit is None :
            representation += shift + INDENTATION +"X\n"
        else :
            representation += self.droit.toString(shift+INDENTATION)
        return representation


#### CLASS ABR ####
        
class ABR :
    def __init__ (self, racine = None) :
        self.racine = racine
    
    def estVide(self):
        return self.racine is None
    
    def hauteur(self) :
        if self.racine is None :
            return 0
        else :
            return hauteur(self.racine)
        
#### MAIN ####
        
if __name__ == "__main__" :
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2, n1, n2)
    n1.parent = n3
    n2.parent = n3
    n4 = Node(10)
    n5 = Node( 7)
    n6 = Node(9,n5, n4)
    n4.parent=n6
    n5.parent = n6
    n7 = Node(5, n3, n6)
    n3.parent = n7
    n6. parent = n7
    n8 = Node(4)
    n2.droit = n8
    n8.parent = n2

    tree = ABR(n7)