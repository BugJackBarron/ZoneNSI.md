import random


def carre(n) :
    t = []
    for i in range(n+1) :
        t.append(i**2)
    return t


def carreC(n) :
    return [nb**2 for nb in range(n+1)]


def imagesf(deb,fin) :
    t =[]
    for i in range(deb, fin+1) :
        t.append(3*i**2 -2*i+1)
    return t

def imagesfC(deb, fin) :
    return [ 3*i**2 -2*i+1 for i in range(deb, fin+1) ]

def genereListe(n) :
    t= []
    for i in range(n) :
        t.append(random.randint(1, n**2))
    return t

def genereListeC(n) :
    return [random.randint(1, n**2) for i in range(n)]
    
    
def insereV1(monTab, val, i) :
    # Version avec slices
    t1 = monTab[:i]  # toutes les valeurs jusqu'à i exclu
    t2 = monTab[i:] # toutes lesvaleurs à partir de l'indice i
    return t1 + [val] + t2

def insereV2(monTab, val, i) :
    # version avec parcours et nouveau tableau
    newTab = []
    for k in range(len(monTab)) :
        if k == i : #si on est à la bonne position
            newTab.append(val) # on insère la valeur donnée
        newTab.append(monTab[k]) # dans tous les cas on recopie le tableau
    return newTab

def insereV3(monTab, val, i):
    # version avec parcours à l'envers et "en place"
    monTab.append(0)
    toto = len(monTab)-2
    while toto >= i :
        monTab[toto+1] = monTab[toto]
        toto = toto - 1 # ou toto -= 1 ou toto += -1
    monTab[i] = val
    return None


def compter(monTab, val) :
    # Avec un parcours par valeurs
    nbOcc = 0
    for v in monTab :
        if v == val :
            nbOcc += 1
    return nbOcc

def compterIndices(monTab, val) :
    # avec un parcours par indice
    positions = []
    for i in range(len(monTab)) :
        if monTab[i] == val :
            positions.append(i)
    return positions

def separer(monTab, val) :
    # On effectue un parcours par éléments
    inf = []# en créant deux tableaus pour les valeurs inférieures ou égales à val
    sup = [] # et un pour les strictement supérieures
    for v in monTab :
        if v> val :
            sup.append(v)
        else :
            inf.append(v)
    return inf, sup # On renvoie les deux tableaux

def plusProche(monTab,val) :
    plusProche = monTab[0]
    mini = abs(plusProche - val) 
    for elem in monTab :
        if abs(elem - val)< mini:
            plusProche = elem
            mini = abs(plusProche - val) 
    return plusProche
    
            
    
    

t = [12, 14, 15, 16, 17 ,19]
print(insereV1(t, 5, 4))
 