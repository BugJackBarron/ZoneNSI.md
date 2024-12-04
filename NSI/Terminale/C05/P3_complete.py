from graphviz import Digraph

import os
os.environ["PATH"] += os.pathsep + 'P:\Documents\Graphviz\Graphviz\\bin'

INDENTATION = "--"

### Fonction utilitaire

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
        elif  self.valeur>x :
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
        
    def insert(self, v) :
        if v< self.valeur :
            if self.gauche is None :
                self.gauche = Node(v, parent=self)
            else :
                self.gauche.insert(v)
        else :
            if self.droit is None :
                self.droit = Node(v, parent=self)
            else :
                self.droit.insert(v)
                
    def supprimer(self, valeur):
        if valeur < self.valeur:
            self.gauche = self.gauche.supprimer(valeur)
            if self.gauche is not None :
                self.gauche.parent = self
            return self
        elif valeur > self.valeur:
            self.droit = self.droit.supprimer(valeur)
            if self.droit is not None :
                self.droit.parent = self
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
        
    def __str__(self) :
        return self.racine.toString("")

    def toImage(self, title="arbre") :
        if not(isinstance(title, str)) :
            title = 'arbre'
        graphe=Digraph()
        self.racine.toImage(graphe)
        graphe.render(title, view = True)
        
    def search(self, x) :
        if self.estVide() :
            return None
        else :
            return self.racine.search(x)
        
    def minimum(self) :
        if self.estVide() :
            return None
        else :
            return self.racine.minimum()
        
    def maximum(self) :
        if self.estVide() :
            return None
        else :
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
            
    def predecessor(self,x) :
        n = self.search(x)
        if n is None :
            return None
        else :
            if not(n.gauche is None) :
                return n.gauce.maximum()
            else :
                ancetre = n.parent
                while not(ancetre  is None) and (n == ancetre.gauche) :
                    n = ancetre
                    ancetre = n.parent
                return ancetre
            
    def insert(self, v) :
        if self.racine is None :
            self.racine = Node(v)
        else :
            self.racine.insert(v)
            
    def rotationGauche(

        
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


#    l1 = [5, 2, 11, 3, 7, 13, 9]
#    l2 = [7, 3, 11, 2, 5, 9, 13]
#    l3 = [2, 3, 5, 11, 7, 13, 9]
#    l4 = [2, 3, 5, 7, 9, 11, 13]
#    tree1 = ABR()
#    tree2 = ABR()
#    tree3 = ABR()
#    tree4 = ABR()
#    for i in range(1,5) :
#        eval(f"[tree{i}.insert(e) for e in l{i}]")
#        eval(f"tree{i}.toImage('arbre{i}')")
        
