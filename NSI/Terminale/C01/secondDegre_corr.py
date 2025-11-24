from math import sqrt

def polynome(*t) :
        try :
            if len(t) == 1 :# si on passe un tuple ou un tableau (1,2,3),
                # *t le convertit en [(1,2,3)]
                t = t[0] # d'où cette ligne
            a, b, *coeff  = t #Puis on unpack
        except TypeError :
            raise TypeError("Must pass three argument or a tuple of 3 element.")
        if len( coeff ) !=1 :
            raise ValueError("Bad Number of argument.")
        if not(isinstance(a,(int, float))
        ) or not(isinstance(b,(int, float))
        ) or not(isinstance(*coeff,(int, float))) :
                raise TypeError("argment Error : argument must be a tuple of integers or floats.")
        if a == 0 :
            raise ValueError("First element of tuple must not be 0.")
        return t
    
    
def _discriminant(p) :
    a,b,c = polynome(p)
    return b**2 - 4*a*c
        
def _nombreRacines(p) :
    d = _discriminant(p)
    if d < 0 :
        return 0
    elif d == 0 :
        return 1
    else : 
        return 2
    
def valeursRacines(p) :
    nbR = _nombreRacines(p)
    if nbR == 0 :
        return None
    elif nbR == 1 :
        a,b,c = p
        return -b/(2*a)
    else :
        a,b,c = p
        d = _discriminant(p)
        return  (-b -sqrt(d))/(2*a), (-b+ sqrt(d))/(2*a)
    
    
def convexite(p) :
    a,b,c = polynome(p)
    if a>0 :
        return "convexe"
    else :
        return "concave"
        
def _calcule(p,x) :
    a,b,c = polynome(p)
    if not(isinstance(x, (float, int))) :
        raise ValueError()
    else :
        return a*x**2+b*x+c

def _nombreDerive(p,x) :
    a,b,c = polynome(p)
    if not(isinstance(x, (float, int))) :
        raise ValueError()
    else :
        return 2*a*x+b
    
def tangente(p,x) :
    return f'y = {_nombreDerive(p,x)}(x-{x}) + {_calcule(p,x)}'
    
