from Arbres_binaires_complet import Arbre_binaire
from pilesFiles import Pile
from random import randint


def inserer(tas, valeur):
    """
    insère la valeur dans le tas
    Envoie le tas
    """
    tas.append(valeur)
    i = len(tas) - 1
    while i != 1 and tas[i//2] < valeur:
        tas[i], tas[i//2] = tas[i//2], tas[i]
        i = i//2

    return tas


def tas_vers_arbre(tas, indice=1, arbre=None):
    """
    Crée et retourne un arbre à partir du tas donné sous forme d'un tableau
    """
    arbre = Arbre_binaire(tas[indice])
    if 2*indice < len(tas):
        arbre.gauche = tas_vers_arbre(tas, 2*indice, arbre)
    if 2*indice+1 < len(tas):
        arbre.droit = tas_vers_arbre(tas, 2*indice+1, arbre)
    return arbre


def meilleure_priorite(tas):
    """
    Récupère la valeur maximale du tas et place la dernière valeur à la première position
    Renvoie la valeur maximale et le tas modifié
    """
    val = tas[1]
    tas[1] = tas[-1]
    tas.pop()
    return val, tas


def retablir(tas):
    # La valeur a descendre
    v = tas[1]
    # l'indice en cours
    i = 1

    # Tant qu'il y a un fils
    while 2*i < len(tas):
        # l'indice du fils-gauche
        i_g = 2*i
        # l'indice du fils-droit
        i_d = 2*i+1
        # Selection du fils ayant la priorite maximale
        i_max = i_g
        if i_d < len(tas) and tas[i_g] < tas[i_d]:
            i_max = i_d
        # Si la racine est superieure au fils maximal, on arrete
        if v > tas[i_max]:
            break
        else:  # Sinon, on fait remonter la valeur de i_max
            # on place la valeur d'indice i_max en i
            tas[i] = tas[i_max]
            # On etudie desormais i_max
            i = i_max
    # On place la valeur a descendre en i
    tas[i] = v

    # on retourne le tas
    return tas


"""
# Création
tas = [17,7,9,1,4]
print("Tas initial :",tas)

# Insertion
tas = inserer(tas, 3)
print("Insertion de 3 :",tas)

# Insertion
tas = inserer(tas, 6)
print("Insertion de 6 :",tas)
# arbre = tas_vers_arbre(tas)
# arbre.dessiner()

# Récupération
v_max,tas = meilleure_priorite(tas)
print("La valeur maximale :",v_max)
print("Le tas impropre :",tas)
# arbre = tas_vers_arbre(tas)
# arbre.dessiner()

# Rétablissement de l'arbre
tas = retablir(tas)
print("Le tas rétabli :",tas)
arbre = tas_vers_arbre(tas)
arbre.dessiner()
"""

tas = [0, 1]
for _ in range(40):
    tas = inserer(tas, randint(1, 100))
tas_vers_arbre(tas).dessiner("initial")
print(tas)
# input()  # Pour laisser à l'utlisateur le temps de sauver l'image, sans quoi les suivantes sont identiques à celle-ci

v_max, tas = meilleure_priorite(tas)
print("La valeur maximale :", v_max)
print(tas)
tas_vers_arbre(tas).dessiner("incorrect")
# input()

tas = retablir(tas)
print(tas)
tas_vers_arbre(tas).dessiner("retabli")
