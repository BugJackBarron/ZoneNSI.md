class Noeud:
    def __init__(self, poids, caractere=None, gauche=None,droit=None):
        self.poids = poids
        self.caractere = caractere
        self.gauche = gauche
        self.droit = droit

    def est_feuille(self):
        """Renvoie True si l’arbre est une feuille, False sinon."""
        return self.gauche is None and self.droit is None

def fusionner(G, D) :
    return Noeud(G.poids+D.poids, gauche=G, droit = D)

def get_dict(chaine) :
    
    carac = set([c for c in chaine])
    return {c:chaine.count(c) for c in carac}

def construire_liste_arbres(d) :
    return [Noeud(v, caractere=k) for k,v in d.items()]

def construire_arbre_huffman(d):
    liste_arbres = construire_liste_arbres(d) 
    while len(liste_arbres) > 1: 
        G = extraire_arbre_poids_min(liste_arbres)
        D = extraire_arbre_poids_min(liste_arbres)
        T = fusionner(G, D)
        liste_arbres.append(T)
    return T

def extraire_arbre_poids_min ( liste_arbres ):
    poids_mini = liste_arbres[0]. poids
    indice_mini = 0
    for i in range(len(liste_arbres)) :
        if liste_arbres[i].poids< poids_mini :
            poids_mini = liste_arbres[i].poids
            indice_mini = i
    arbre_extrait = liste_arbres.pop( indice_mini )
    return arbre_extrait

def construire_codes (A, chemin, dico ):
    if A.est_feuille() :
        dico [A.caractere ] = chemin
    else :
        construire_codes (A.gauche, chemin + "0", dico)
        construire_codes (A.droit , chemin + "1", dico)
