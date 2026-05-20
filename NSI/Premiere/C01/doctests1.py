#Import des modules
import doctest


# Déclaration des fonctions 

def times3(n) :
    """
    Fonction qui multiplie par 3
>>> times3(10)
30
>>> times3(5)
15
>>> times3('a')
'aaa'
"""
    return 3*n

# Code réellement exécuté

doctest.testmod() # tests de toutes les fonctions déclarées