from random import randint
        
def genere_groupe() -> list :
    """fonction renvoyant un tableau de 23 nombres aléatoires entre 1 et 365"""
    return [randint(1,365) for _ in range(23)]

def contient_doublon(t : list) -> bool :
    """fonction renvoyant un booléen signalant la présence ou non d'un doublon dans le tableau"""
    s = [] # s est un tableau temporaire contenant les valeurs testées
    for data in t :
        if data in s : # si data est déjà dans s, alors c'est un doublon
            return True
        else : # sinon on ajoute data à la liste des valeurs testées.
            s.append(data)
    return False
    
def teste_hypothese(n : int) -> int:
    """fonction renvoyant le nombre de groupes contenant un doublon
    sur un échantillon de n groupes"""
    nbDoublons = 0 
    for _ in range(n) :
        t = genere_groupe()
        if contient_doublon(t) :
            nbDoublons +=1
    return nbDoublons