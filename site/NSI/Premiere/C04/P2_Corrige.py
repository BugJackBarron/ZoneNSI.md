import random


def carre(n) :
    t = []
    for i in range(n+1) :
        t.append(i**2)
    return t

def imagesf(deb,fin) :
    t =[]
    for i in range(deb, fin+1) :
        t.append(3*i**2 -2*i+1)
    return t

def genereListe(n) :
    t= []
    for i in range(n) :
        t.append(random.randint(1, n**2))
    return t
    


t = (12, 14, 15, 16, 17 ,19)
 
 