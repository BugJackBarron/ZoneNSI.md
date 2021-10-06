### Corrigé Ex n°1

def estUnPalindrome (X) :
    L = len(X)
    if L == 1 :
        return True
    elif L == 2 :
        return X[0] == X[1]
    else :
        if X[0]!=X[L-1] :
            return False
        else :
            return estUnPalindrome(X[1:L-1])
        
        
### Corrigé Ex n°2
from math import gcd        
def pgcd(a,b) :
    if not(isinstance(a, int) and isinstance(b, int)) :
        raise TypeError
    elif a<0 or b<0 :
        raise ValueError
    else:
        return gcd(a,b)
    