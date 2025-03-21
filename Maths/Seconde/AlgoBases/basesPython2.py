def estUnTriangleRectangle(a, b, c) :
    if a**2 == b**2 + c**2 :
        return f"le triangle est rectangle d'hypothénuse de longueur {a}"
    elif b**2 == a**2 + c**2 :
        return f"le triangle est rectangle d'hypothénuse de longueur {b}"
    elif c**2 == a**2 + b**2 :
        return f"le triangle est rectangle d'hypothénuse de longueur {c}"
    else :
        return "le triangle n'est pas rectangle"