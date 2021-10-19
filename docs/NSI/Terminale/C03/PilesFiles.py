class Pile :
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
