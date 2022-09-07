"""
Compter le nombre chaînes de N bits dans lesquelles il n'y a pas deux bits à 1 qui se suivent
Trouve ces chaînes
"""
from time import perf_counter_ns


def k_ieme_bit(n, k):
    """
    Renvoie le k-ième bit d'un nombre
    """
    if n & 2**k == 2**k :
        return 1
    else :
        return 0


def disposition_valide(n: int, maxi: int) -> bool:
    """
    Vérifie que l'écriture binaire du nombre n ne comporte pas deux bits 1 à la suite
    """
    for rang in range(0, maxi):
        if k_ieme_bit(n, rang) == 1 and k_ieme_bit(n, rang) == k_ieme_bit(n, rang+1):
            return False
    return True


def dispositions_ITER(n: int) -> int:
    """
    Compte le nombre chaînes de N bits dans lesquelles il n'y a pas deux bits à 1 qui se suivent
    Retourne ce nombre
    On utilise la programmation dynamique avec une approche ascendante
    """
    # Le tableau stockant le nombre de chaînes de i caractères satisfaisant la condition
    # et se terminant par 0 ou 1
    T = [[0, 0] for i in range(n+1)]

    # Il y a une chaîne de 1 caractère se terminant par 0 et une se terminant par 1
    T[1][0] = 1
    T[1][1] = 1

    # Calcul des autres valeurs
    for i in range(2, n+1):
        # Il est possible d'ajouter un 0 après un 0 ou un 1
        T[i][0] = T[i-1][0] + T[i-1][1]
        # Il n'est possible d'ajouter un 1 qu'après un 0
        T[i][1] = T[i-1][0]

    # On renvoie la somme de T[n][0] et T[n][1]
    return T[n][0] + T[n][1]


def dispositions_RECUR(n: int) -> int:
    """
    Compte le nombre chaînes de N bits dans lesquelles il n'y a pas deux bits à 1 qui se suivent
    Retourne ce nombre
    On utilise la programmation dynamique avec une approche descendante
    Retourne un triplet :
        * nombre de nombres à n bits se terminant par 0
        * nombre de nombres à n bits se terminant par 1
        * nombre de nombres à n bits se terminant par 0 ou 1 (somme des précédents)
    """
    # Cas de base n = 1 :
    if n == 1:
        return 1, 1, 2
    else:
        if (n, 0) not in memoire:  # Les valeurs n'ont pas encore été calculées
            zeros, uns, somme = dispositions_RECUR(n-1)
            memoire[(n, 0)] = zeros + uns
            memoire[(n, 1)] = zeros
        return memoire[(n, 0)], memoire[(n, 1)], memoire[(n, 0)]+memoire[(n, 1)]


def liste_dispositions(n, mot="", solution=None):
    """
    Trouve les solutions au problème et les ajoute à une liste globale
    """
    if solution is None:
        solution = []
    # S'il n'y plus de chiffres à ajouter,
    # on ajoute le mot à la liste
    if n == 0:
        solution.append(mot)

    else:
        if mot == "" or mot[-1] == "0":
            liste_dispositions(n-1, mot+"0", solution)
            liste_dispositions(n-1, mot+"1", solution)
        else:
            liste_dispositions(n-1, mot+"0", solution)
        return solution


def afficher(n, mot=""):
    """
    Affiche les solutions au problème et les ajoute à une liste globale
    """
    # S'il n'y plus de chiffres à ajouter,
    # on affiche le mot
    if n == 0:
        print(mot)

    else:
        if mot == "" or mot[-1] == "0":
            afficher(n-1, mot+"0")
            afficher(n-1, mot+"1")
        else:
            afficher(n-1, mot+"0")


if __name__ == '__main__':

    # Test des fonctions k_ieme_bits et disposition valide
    n = 19
    print(f"{n} (décimal)={bin(n)[2:]} (binaire)")
    print(f"Le 1ème bit de {n} : {k_ieme_bit(n,1)}")
    print(f"Le 2ème bit de {n} : {k_ieme_bit(n,2)}")
    print(f"Le nombre {n} représente-t-il une disposition valide ? {disposition_valide(n,10)}")

    # Nombre de chiffrres
    n = 6

    print(f"On considère des nombres de {n} bits")
    t1 = perf_counter_ns()
    a = dispositions_ITER(n)
    t2 = perf_counter_ns()
    print(f"La solution itérative : {a} (en {round((t2-t1)/1000,3)} µs)")
    print(f"On considère {n} chiffres")
    memoire = {}
    t1 = perf_counter_ns()
    _, _, a = dispositions_RECUR(n)
    t2 = perf_counter_ns()
    print(f"La solution récursive : {a} (en {round((t2-t1)/1000,3)} µs)")
    print(f"Les chaînes solutions : {liste_dispositions(n)}")
    # afficher(n)

    # Par curiosité : quels sont les nombres de dispositions pour différentes valeurs de N ?
    print("Le nombre de dispositions valides de 1 à 20")
    print([dispositions_ITER(i) for i in range(1, 20)])
    # C'est la suite de Fibonacci !

    # Par curiosité : quels sont les dispositions converties en entier pour une certaine valeur de N ?
    print("Les première dispositions valides écrites en décimal")
    print([int(dispo, 2) for dispo in liste_dispositions(10)])
    # C'est la suite des nombres "Fibbinaires" : A003714 dans https://oeis.org/A003714
