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

    def affiche(self) :
        print(f"Bonjour, je suis {self.nom}, de niveau {self.niveau}."
         f"J'ai {self.force} en force, {self.endurance} en endurance, {self.rapidite}"
          f"en rapidité et {self.intelligence} en intelligence. J'ai {self.pv} Points de Vie")
