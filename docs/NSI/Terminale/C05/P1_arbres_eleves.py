class Node() :
    def __init__(self, valeur, gauche, droit) :
        self.valeur=valeur
        self.gauche = gauche
        self.droit = droit
        
tree = Node(1,
        Node(2,
            Node(3, None, None),
            None),
        Node(4, None, None))

arbre1 = Node("A", #Racine
                  Node("B", #FG
                       Node("D",None,None),#FG
                       Node("E",None,None),#FD
                       ),
                  Node("C",#FD
                       None,#FG
                       Node("F",#FD
                            None,#FG
                            Node("G", None, None)#FD
                            )
                       )    
    )

arbre2 = Node("P",
                  Node("A",
                       Node("R",
                            Node("C", None, None),
                            None
                            ),
                       Node("I",
                            Node("X", None, None),
                            Node("N", None, None)
                            )
                       ),
              None
              )

def hauteur(t) :
    if t is None :
        return 0
    else :
        return 1 + max(hauteur(t.gauche), hauteur(t.droit))
    
def taille(t) :
    if t is None :
        return 0
    else :
        return 1 + taille(t.gauche)+taille(t.droit)
    
def estVide(t) :
    return t is None


arbre1 = Node('A',
            Node('B', None, None),
            Node('H', None, None)
            )

arbre2 = Node('A',
            Node('B', 
                Node('C',
                    Node('D', None, None),
                    Node('E', None, None)),
                Node('F', 
                    Node('G', None, None),
                    None)
                ),
            Node('H',
                Node('I',
                    None,
                    Node('J', None,None)),
                Node('K',
                    Node('L', None,None),
                    None)
                )                   
            )


def visitePrefixe(tree) :
    print(tree.valeur, end=" ")
    if not(estVide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    if not(estVide(tree.droit)) :
        visitePrefixe(tree.droit)

