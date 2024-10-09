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

arbre1 = Node('A',
            Node('B', None, None),
            Node('C', None, None)
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

def estVide(t) :
    return t is None


def visitePrefixe(tree) :
    print(tree.valeur, end=" ")
    if not(estVide(tree.gauche)) :
        visitePrefixe(tree.gauche)
    if not(estVide(tree.droit)) :
        visitePrefixe(tree.droit)
