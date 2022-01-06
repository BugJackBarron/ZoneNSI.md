from graphviz import Digraph

INDENTATION = "  "

def hauteur(t) :
    if t is None :
        return 0
    else :
        return 1 + max(hauteur(t.gauche), hauteur(t.droit))

class ABR :
    def __init__ (self, racine = None) :
        self.racine = racine
        
    def estVide(self) :
        return self.racine is None
    
    def hauteur(self) :
        return hauteur(self.racine)
    
    
    def __str__(self) :
        if self.estVide() :
            return "Arbre vide !"
        else :
            return self.racine.toString("")
        
    def toImage(self, title="arbre") :
        if not(isinstance(title, str)) :
            title = 'arbre'
        graphe=Digraph()
        self.racine.toImage(graphe)
        graphe.render(title, view = True)
        
    def search(self, x) :
        if self.racine is None :
            return None
        else :
            return self.racine.search(x)
        
    def minimum(self) :
        if self.racine is None :
            return None
        return self.racine.minimum()
    
    def maximum(self) :
        if self.racine is None :
            return None
        return self.racine.maximum()
    
    def successor(self,x) :
        n = self.search(x)
        if n is None :
            return None
        else :
            if not(n.droit is None) :
                return n.droit.minimum()
            else :
                ancetre = n.parent
                while not(ancetre  is None) and (n == ancetre.droit) :
                    n = ancetre
                    ancetre = n.parent
                return ancetre
            
    def insert(self, x) :
        if self.racine is None :
            self.racine = Node(x)
        else :
            self.racine.insert(x)
            
    def supprimer(self, valeur):
        if self.estVide():
            return
        else:
            self.racine = self.racine.supprimer(valeur)
            
    def insererAVL(self, valeur):
        if self.estVide():
            self.racine = Node(valeur)
        else:
            self.racine = self.racine.insererAVL(valeur)
    
    
        
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
            representation += shift + INDENTATION + "X\n"
        else :
            representation += self.gauche.toString(shift+INDENTATION)
        if self.droit is None :
            representation +=  shift + INDENTATION + "X\n"
        else :
            representation += self.droit.toString(shift+INDENTATION)
        return representation
    
    def toImage(self, graphe, etiquette = None) :
        noeud = str(self.valeur)
        graphe.node(noeud)
        if not(self.parent is None) :
            graphe.edge(str(self.parent.valeur), noeud, label=etiquette)
        if not(self.gauche is None) :
            self.gauche.toImage(graphe, "G")
        if not(self.droit is None) :
            self.droit.toImage(graphe, "D")
            
    def search(self, x) :
        if self.valeur == x :
            return self
        elif x<self.valeur :
            if self.gauche is None :
                return None
            else :
                return self.gauche.search(x)
        else :
            if self.droit is None :
                return None
            else :
                return self.droit.search(x)

    def minimum(self) :
        if self.gauche is None :
            return self
        else :
            return self.gauche.minimum()
        
    def maximum(self) :
        if self.droit is None :
            return self
        else :
            return self.droit.maximum()
        
    def insert(self, x) :
        if self.valeur>x :
            if self.gauche is None :
                self.gauche = Node(x, parent = self)                
            else :
                self.gauche.insert(x)
        else :
            if self.droit is None :
                self.droit = Node(x, parent = self)                
            else :
                self.droit.insert(x)
                
    def supprimer(self, valeur):
        if valeur < self.valeur:
            self.gauche = self.gauche.supprimer(valeur)
            return self
        elif valeur > self.valeur:
            self.droit = self.droit.supprimer(valeur)
            return self
        else:
            return self.supprimerNoeudCourant()

    def supprimerNoeudCourant(self):
        if self.estFeuille():
            return None
        elif self.gauche is None:
            return self.droit
        elif self.droit is None:
            return self.gauche
        else:
            ## on cherche le noeud minimum du sous-arbre droit
            noeudMin = self.droit.minimum()
            ## On met à jour la valeur du noeud courant
            self.valeur = noeudMin.valeur
            ## On supprime le noeud minimal, qui ne possède pas de fils gauche (mais peut
            ## éventuellement posséder une descendance droite
            noeudMin.parent.droit = noeudMin.droit
            ## et on retourne le noeud courant
            return self
        
    def rotationGauche(self) :
        pivot = self.droit
        RG = Node(self.valeur, gauche = self.gauche, droit = pivot.gauche, parent = pivot)
        if RG.gauche is not None :
            RG.gauche.parent = RG
        if RG.droit is not None :
            RG.droit.parent = RG
        racine = Node(pivot.valeur, RG, pivot.droit, parent = self.parent)
        return racine
        
    def rotationDroite(self) :
        pivot = self.gauche
        RD = Node(self.valeur, gauche = pivot.droit, droit = self.droit, parent = pivot)
        if RD.gauche is not None :
            RD.gauche.parent = RD
        if RD.droit is not None :
            RD.droit.parent = RD
        racine = Node(pivot.valeur, pivot.gauche, RD, parent = self.parent)
        return racine
    
    def insererAVL(self, valeur):
        if valeur < self.valeur:
            if self.gauche is None:
                self.gauche = Node(valeur, parent=self)
                return self
            else:
                self.gauche = self.gauche.insererAVL(valeur)
                return self.equilibrer()
        elif valeur > self.valeur:
            if self.droit is None:
                self.droit = Node(valeur, parent=self)
                return self
            else:
                self.droit = self.droit.insererAVL(valeur)
                return self.equilibrer()
        else:
            return self
            
    def equilibrer(self):
        hauteur_gauche = hauteur(self.gauche)
        hauteur_droit = hauteur(self.droit)
        if hauteur_gauche - hauteur_droit == 2:
            hauteur_gauche_gauche = hauteur(self.gauche.gauche)
            hauteur_gauche_droit = hauteur(self.gauche.droit)
            if hauteur_gauche_gauche > hauteur_gauche_droit:
                return self.rotationDroite()
            else:
                self.gauche = self.gauche.rotationGauche()
                return self.rotationDroite()
        elif hauteur_gauche - hauteur_droit == -2:
            hauteur_droit_droit = hauteur(self.droit.droit)
            hauteur_droit_gauche = hauteur(self.droit.gauche)
            if hauteur_droit_droit > hauteur_droit_gauche:
                return self.rotationGauche()
            else:
                self.droit = self.droit.rotationDroite()
                return self.rotationGauche()
        else:
            return self
            
    def hauteur(self):
        hauteur_gauche = hauteur(self.gauche)
        hauteur_droit = hauteur(self.droit)
        return 1 + max(hauteur_gauche, hauteur_droit)
        
    
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
    tree = ABR(n7)
    n8 = Node(4)
    n2.droit = n8
    n8.parent = n2
    
    print(tree)
    
    tree = ABR()
    for elem in [15,12,7,8,1,23,13, 17, 28] :
        tree.insererAVL(elem)
    tree.toImage()
    
    