from random import randint

class Personnage :
    """ une classe pour représenter un personnage générique du MMORPG """
    def __init__(self, nom, force, endurance, rapidite, intelligence) :
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
        
            
    def affiche(self) :
        print(f"Bonjour, je suis {self.nom}, de niveau {self.niveau}."
         f"J'ai {self.force} en force, {self.endurance} en endurance, {self.rapidite}"
          f"en rapidité et {self.intelligence} en intelligence. J'ai {self.pv} Points de Vie")

    def attaque(self) :
        return self.force + randint(1,20)
    
    def defense(self, valeurAttaque) :
        valeurDefense = self.endurance + randint(1,20)
        if valeurAttaque> valeurDefense :
            self.pv -=  valeurAttaque-valeurDefense
            return False
        return True
    
    def __eq__(self, other) :
            return (self.force == other.force) and (
            self.endurance == other.endurance) and (
            self. rapidite == other.rapidite) and (
            self.intelligence == other.intelligence)

if __name__ == "__main__" :
     
    firstPlayer = Personnage('Bob', 18, 25, 12, 30)
    secondPlayer = Personnage('Bill', 34, 10, 20, 12)
    