def somme(a,b) :
    """ fonction qui renvoie la somme des arguments a et b, 
    en vérifiant si a et b sont bien du même type, 
    et qui renvoie None sinon.
    Par exemple :

    somme(4, 3) renvoie 7

    somme(4, "3") renvoie None
   
    """
    if type(a) == type(b) :
        return a+b
    else :
        return None