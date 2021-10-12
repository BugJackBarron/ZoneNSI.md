import time
from random import randint
from copy import deepcopy

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f" {method.__name__}  : {te-ts}" )
        return result

    return timed


def tri_selection(tab):
    for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
    return tab


def tri_insertion(tab): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k


def fusion(t1, t2) :
    """
>>> fusion([12,35,45],[4,42,63])
[4, 12, 35, 42, 45, 63]
>>> fusion([12,35], [57])
[12, 35, 57]
>>> fusion([12,35], [42,57])
[12, 35, 42, 57]
>>> fusion([12,35], [])
[12, 35]
>>> fusion([], [12,35])
[12, 35]
>>> fusion([42,57,67,75], [12,35])
[12, 35, 42, 57, 67, 75]
>>> fusion([], [])
[]

"""
    tf = [0]*(len(t1)+len(t2))
    i, j = 0, 0
    for k in range(len(tf)) :
        if  i<len(t1) and j<len(t2) :
            if t1[i]<t2[j] :
                tf[k] = t1[i]
                i+=1
            else :
                tf[k] = t2[j]
                j+=1
        elif i<len(t1) :
            tf[k] = t1[i]
            i+=1
        elif  j<t2[j] :
            tf[k] = t2[j]
            j+=1
    return tf

@timeit
def callTriFusion(tab):
    return triFusion(tab)


def triFusion(tab) :
    if len(tab) <= 1 :
        return tab
    else :
        t1 = triFusion(tab[:len(tab)//2])
        t2 = triFusion(tab[len(tab)//2:])
        return fusion(t1,t2)
        

def genereTab(n) :
    return [randint(0, n**2) for _ in range(n)]

def testeTemps(n) :
    
    tab = genereTab(n)
    tabi = deepcopy(tab)
    print(f"#### TRI INSERTION {n} ####")
    tri_insertion(tabi)
    tabs = deepcopy(tab)
    print(f"#### TRI SELECTION {n} ####")
    tri_selection(tabs)
    tabf=deepcopy(tab)
    print(f"#### TRI FUSION {n} ####")
    callTriFusion(tabf)


import doctest
doctest.testmod()