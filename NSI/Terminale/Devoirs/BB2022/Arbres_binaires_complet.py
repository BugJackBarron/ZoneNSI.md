import graphviz
from pilesFiles import Pile, File


class Arbre_binaire:
    """
    Classe implémentant un arbre binaire dont les noeuds sont caractérisés par 
    - une valeur (de type quelconque)
    - une fils gauche et un fils droit
    Les enfants gauche et droit sont eux-mêmes des arbres
    """

    def __init__(self, valeur=None, gauche=None, droit=None):
        """
        Constructeur
        """
        if valeur:
            self.valeur = valeur
            if gauche:
                self.gauche = gauche
            else:
                self.gauche = None
            if droit:
                self.droit = droit
            else:
                self.droit = None
        else:  # arbre vide
            self.valeur = None
            self.gauche = None
            self.droit = None

    def get_valeur(self):
        """
        Accesseur de la valeur de l'arbre
        """
        return self.valeur

    def set_valeur(self, valeur):
        """
        Mutateur de la valeur de l'arbre
        """
        self.valeur = valeur

    def get_gauche(self):
        """
        Accesseur du fils gauche
        """
        return self.gauche

    def set_gauche(self, arbre):
        """
        Mutateur du fils gauche
        """
        self.gauche = arbre

    def get_droit(self):
        """
        Accesseur du fils droit
        """
        return self.droit

    def set_droit(self, arbre):
        """
        Mutateur du fils droit
        """
        self.droit = arbre

    def est_feuille(self) -> bool:
        """
        Renvoie True si l'arbre est une feuille (pas d'enfants)
        False dans le cas contraire
        """
        return self.gauche == None and self.droit == None

    def taille(self) -> int:
        """
        Renvoie la taille de l'arbre (le nombre de noeud)
        """
        t = 0
        if self.get_valeur():
            t += 1

        if self.gauche:
            t += self.gauche.taille()
        if self.droit:
            t += self.droit.taille()

        return t

    def hauteur(self) -> int:
        """
        Renvoie la hauteur de l'arbre
        Renvoie 1 si l'arbre est une feuille
        """
        h = 1

        hauteurs = [0]

        if self.gauche:
            hauteurs.append(self.gauche.hauteur())
        if self.droit:
            hauteurs.append(self.droit.hauteur())

        return h + max(hauteurs)

    def parcours_largeur(self) -> None:
        """
        Renvoie la chaîne de caractère formée par les valeurs
        des noeuds rencontrés lors d'un parcours en largeur
        """
        if self.valeur == None:
            return "L'arbre est vide"

        p = ""

        f = File()

        f.enfiler(self)

        while not f.est_vide():
            enCours = f.defiler()
            p += (str(enCours.get_valeur()) + " -> ")
            if enCours.gauche:
                f.enfiler(enCours.gauche)
            if enCours.droit:
                f.enfiler(enCours.droit)

        return p[:-4]

    def parcours_profondeur_prefixe(self, depart=True) -> None:
        """
        Renvoie la chaîne de caractère formée par les valeurs
        des noeuds rencontrés lors d'un parcours en profondeur prefixe
        """
        if self.valeur == None:
            return ""
        else:
            p = ""

            p += str(self.valeur) + " -> "

            if self.gauche:
                p += self.gauche.parcours_profondeur_prefixe(False)

            if self.droit:
                p += self.droit.parcours_profondeur_prefixe(False)

            if depart:
                return p[:-4]
            else:
                return p

    def parcours_profondeur_postfixe(self, depart=True) -> None:
        """
        Renvoie la chaîne de caractère formée par les valeurs
        des noeuds rencontrés lors d'un parcours en profondeur postfixe
        """
        if self.valeur == None:
            return ""
        else:
            p = ""

            if self.gauche:
                p += self.gauche.parcours_profondeur_postfixe(False)

            if self.droit:
                p += self.droit.parcours_profondeur_postfixe(False)

            p += str(self.valeur) + " -> "

            if depart:
                return p[:-4]
            else:
                return p

    def parcours_profondeur_infixe(self, depart=True) -> None:
        """
        Renvoie la chaîne de caractère formée par les valeurs
        des noeuds rencontrés lors d'un parcours en profondeur infixe
        """
        if self.valeur == None:
            return ""
        else:
            p = ""

            if self.gauche:
                p += self.gauche.parcours_profondeur_infixe(False)

            p += str(self.valeur) + " -> "

            if self.droit:
                p += self.droit.parcours_profondeur_infixe(False)

            if depart:
                return p[:-4]
            else:
                return p

    def dessiner(self, nom="graph") -> None:
        """
        Représente l'arbre
        """
        key = 0
        pile = Pile()

        g = graphviz.Graph(format="png")
        g.node(str(key), str(self.valeur))
        pile.empiler((self, key))

        while not pile.est_vide():
            enCours, enCours_key = pile.depiler()
            if enCours.gauche:
                key += 1
                g.node(str(key), str(enCours.gauche.valeur))
                pile.empiler((enCours.gauche, key))
                g.edge(str(enCours_key), str(key))
            else:
                key += 1
                g.node(str(key), style='invis')
                g.edge(str(enCours_key), str(key), style="invis", weight="20")
            if enCours.droit:
                key += 1
                g.node(str(key), str(enCours.droit.valeur))
                pile.empiler((enCours.droit, key))
                g.edge(str(enCours_key), str(key))
            else:
                key += 1
                g.node(str(key), style='invis')
                g.edge(str(enCours_key), str(key), style="invis", weight="20")

        g.render(nom, view=True)

        return None

    def __str__(self):
        """
        Représentationd dee l'arbre dans la console
        """
        h_barre = "_____"

        s = ""
        if self.valeur == None:
            s = "L'arbre est vide"
        else:
            depth = 0
            p = Pile()
            p.empiler((self, depth))
            while not p.est_vide():
                enCours, depth = p.depiler()
                if depth > 0:
                    s += "  |"+(" "*8+"|")*(depth-1) + h_barre + \
                        str(enCours.get_valeur()) + "\n"
                elif depth == 0:
                    s += str(enCours.get_valeur()) + "\n"
                if enCours.gauche:
                    p.empiler((enCours.gauche, depth+1))
                if enCours.droit:
                    p.empiler((enCours.droit, depth+1))

        return s


if __name__ == "__main__":
    arbre_binaire = Arbre_binaire("T", Arbre_binaire("Y"), Arbre_binaire("O"))
    gauche = arbre_binaire.get_gauche()
    gauche.set_gauche(Arbre_binaire("P"))
    droit = arbre_binaire.get_droit()
    droit.set_gauche(Arbre_binaire("H"))
    droit.set_droit(Arbre_binaire("N"))

    arbre_binaire.dessiner()
    print(arbre_binaire)
    print("La taille de l'arbre est :", arbre_binaire.taille())
    print("La hauteur de l'arbre est :", arbre_binaire.hauteur())
    print("Le parcours en largeur de l'arbre est :",
          arbre_binaire.parcours_largeur())
    print("Le parcours en profondeur prefixe de l'arbre est :",
          arbre_binaire.parcours_profondeur_prefixe())
    print("Le parcours en profondeur infixe de l'arbre est :",
          arbre_binaire.parcours_profondeur_infixe())
    print("Le parcours en profondeur postfixe de l'arbre est :",
          arbre_binaire.parcours_profondeur_postfixe())
