class Node :
    def __init__(self, valeur, gauche, droit) :
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
        
def appartient(x, tree) :
    if tree == None :
        return False
    elif tree.valeur == x :
        return True
    elif x<tree.valeur :
        return appartient(x, tree.gauche)
    else :
        return appartient(x, tree.droit)
    
def minimum(tree) :
    if tree is None :
        return None
    else :
        if tree.gauche is None :
            return tree.valeur
        else :
            return minimum(tree.gauche)

def maximum(tree) :
    if tree is None :
        return None
    else :
        if tree.droit is None :
            return tree.valeur
        else :
            return maximum(tree.droit)
        
def insertion(tree, elem) :
    if tree is None :
        return Node(elem, None, None)
    else :
        if elem< tree.valeur :
            return Node(tree.valeur, insertion(tree.gauche, elem), tree.droit)
        else :
            return Node(tree.valeur, tree.gauche, insertion(tree.droit, elem))

def estVide(t) :
    return t is None

def visiteInfixe(tree) :
    if not(estVide(tree.gauche)) :
        visiteInfixe(tree.gauche)
    print(tree.valeur, end=" ")    
    if not(estVide(tree.droit)) :
        visiteInfixe(tree.droit)
        
def triABR(liste) :
    t = None
    for e in liste :
        t = insertion(t, e)
    return visiteInfixe(t)
        
        
l1 = [15,12,7,8,1,23,13]
l2 = [7,1,23,13,15,8,12]


tree1 = None
for elem in l1 :
    tree1 = insertion(tree1, elem)
    
tree2 = None
for elem in l2 :
    tree2 = insertion(tree2, elem)
    
        