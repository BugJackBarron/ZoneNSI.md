from random import randint

class Personnage :
    """ une classe pour représenter un personnage générique du MMORPG """
    def __init__(self, nom : str, force : int, endurance : int, rapidite : int, intelligence : int) :
        if type(nom) != str :
            raise TypeError("Parameter nom must be str")
        if nom =="" :
            raise ValueError("nom must not be an empty string")
        for carac in ["force", "endurance", "rapidite", "intelligence"] :
            if type(eval(carac)) != int :
                raise TypeError(f"{carac} parameter is not an int (it's {type(eval(carac))}) !")
            if not(1<= eval(carac) <= 40) :
                raise ValueError(f"{carac} is not between 1 and 40 (it's {eval(carac)}) !")
        self.nom = nom
        self.force = force
        self.endurance = endurance
        self.rapidite = rapidite
        self.intelligence = intelligence
        self.pv = self.endurance + self.force//2
        self.pex = 0
        self.niveau = 1
        
    def __str__(self) :
        return  f"""Bonjour, je suis {self.nom}, de niveau {self.niveau}.
         J'ai {self.force} en force, {self.endurance} en endurance, {self.rapidite}
           en rapidité et {self.intelligence} en intelligence. J'ai {self.pv} Points de Vie"""
    
    def affiche(self) :
        print(str(self))
        
            
    def attaque(self) :
        return self.force + randint(1,20)
    
    def defense(self, valeurAttaque) :
        valeurDefense = self.endurance + randint(1,20)
        if valeurAttaque> valeurDefense :
            self.pv -=  valeurAttaque-valeurDefense
            return False
        return True
    
    def initiative(self) :
        return self.rapidite+randint(1,20)
    
    def __eq__(self, other) :
        return (self.force == other.force) and (
            self.endurance == other.endurance) and (
            self. rapidite == other.rapidite) and (
            self.intelligence == other.intelligence)
            
def une_attaque(attaquant : Personnage, defenseur : Personnage) :
    VA = attaquant.attaque()
    print(f"{attaquant.nom} attaque avec {VA} !")
    if defenseur.defense(VA) :
        printf("=> {defenseur.nom} se défend et gagne 1 pex !")
        defenseur.pex+=1
    else :
        printf("=> {defenseur.nom} est blessé et n'a plus que {defenseur.pv} pv.")
        printf("=> {defenseur.nom} est blessé et n'a plus que {defenseur.pv} pv.")ex
        attaquant.pex += 2
    return attaquant,defenseur
            
def fight(p1 : Personnage, p2 : Personnage) ->tuple[Personnage] :
    while p1.pv > 0 and p2.pv > 0 :
        i1 = p1.initiative()
        i2 = p2.initiative()
        if i1>i2 :
            p1, p2 = une_attaque(p1, p2)
            if p2.pv>0 :
                p2,p1 = une_attaque(p2,p1)
        else :
            p2, p1 = une_attaque(p2, p1)
            if p1.pv>0 :
                p1,p2 = une_attaque(p1,p2)
    return p1, p2


if __name__ == "__main__" :
    firstPlayer = Personnage('Bob', 18, 25, 12, 30)
    secondPlayer = Personnage('Bill', 34, 10, 20, 12)
    
    