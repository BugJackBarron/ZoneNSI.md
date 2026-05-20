from math import sqrt
    
def polynome(t) :
    a,b,c = t
    if a == 0 :
        return None
    return t
    
def _discriminant(p) :
    a,b,c = polynome(p)
    return b**2 - 4*a*c
        
def _nombreRacines(p) :
    delta = _discriminant(p)
    if delta<0 :
        return 0
    elif delta == 0 :
        return 1
    else :
        return 2
    
def valeursracines(p) :
    a,b,c = polynome(p)
    n = _nombreRacines(p)
    if n == 0 :
        return None
    elif n == 1 :
        return -b/(2*a)
    else :
        delta = _discriminant(p)
        return ((-b-sqrt(delta)/(2*a)), (-b+sqrt(delta)/(2*a)))

    
def convexite(p) :
    a,b,c = polynome(p)
    if a >0 :
        return 'convexe'
    return 'concave'
    
def _calcule(p,x) :
    a,b,c = polynome(p)
    return a*x**2 + b*x + c

def _nombreDerive(p, x0) :
    a,b,c = polynome(p)
    return 2*a*x0+b
    
def tangente(p, x0) :
    a,b,c = polynome(p)
    return f'y = {_nombreDerive(p,x0)}(x - {x0}) + {_calcule(p, x0)}'
