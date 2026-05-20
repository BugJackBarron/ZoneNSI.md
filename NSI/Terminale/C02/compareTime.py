from triFusion import triFusion, tri_selection, tri_insertion
from random import randint
import time
from copy import deepcopy

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f" {method.__name__}  {te-ts}" )
        return result

    return timed

@timeit
def testeTriFusion(tab) :
    triFusion(tab)
    return

@timeit
def testeTriInsertion(tab) :
    tri_insertion(tab)
    return

@timeit
def testeTriSelection(tab) :
    tri_selection(tab)
    return



def genereTab(n):
    return [randint(0, n**2) for _ in range(n)]


def testeTemps(n) :
    tab0 = genereTab(n)
    print("##### TRI PAR INSERTION ###")
    testeTriInsertion(deepcopy(tab0))
    print("##### TRI PAR SELECTION ###")
    testeTriSelection(deepcopy(tab0))
    print("##### TRI PAR FUSION ###")
    testeTriFusion(deepcopy(tab0))
    
    



