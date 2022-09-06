from math import sqrt
	
def polynome(t) :
    a,b,*c = t
    if not(isinstance(a,(int, float))
    ) or not(isinstance(b,(int, float))
    ) or len(c) >1 or not(isinstance(*c,(int, float))) :
           raise ValueError()
    if a == 0 :
           raise ValueError()
    return t
    
def _discriminant(p) :
    a,b,c = polynome(p)
    return b**2 - 4*a*c
        
def _nombreRacines(p) :
    ...
    
def valeursracines(p) :
    ...
    
def convexite(p) :
    ...
    
def _calcule(p,x) :
    ...

def _nombreDerive(p,x) :
    ...
    
def tangente(p,x) :
    ...
