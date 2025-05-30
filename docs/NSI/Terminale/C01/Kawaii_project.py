import pygame as pg
from random import randint

CURSOR_LEVEL= 5
RED = (255, 0, 0)
ORANGE = (255, 173, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
CURSOR_COLOURS = [RED, ORANGE, YELLOW, GREEN, PURPLE ]


class HappinessLevel :
    def __init__(self, start_level = 2) :
        self.start_level = start_level
        self.max_level = 5

    
class KawaiiMonster :
    
    def __init__(self, name : str, image_base :str, happiness_max  : int = 100, happiness_speed : int = 2, base_value : int =100) :
        """
        Méthode constructeur d'un monstre :

        * name : chaine de caractère, nom d'un personnage
        * image_base : listes de noms fichiers (str) pour affichage
        * happiness_max : niveau maximum de bonheur du monstre
        * happinesse_speed : vitesse de décroissance du bonheur
        * base_value : coût de base d'un monstre/coût d'une augmentation de niveau
         """

        self. name = name
        self.image_base = pg.image.load(image_base).convert_alpha()
        self.imaghe_rect = self.image_base.get_rect()
        self.happiness_max = happiness_max
        self.happiness_speed = happiness_speed
        self.happiness = self.happiness_max
        self.level = 1
        self.base_value = base_value
        
        
    def sad(self) :
        self.happiness -= self.happiness_speed*self.level
            
        
    def feed(self, value) :
        self.happiness += value
        if self.happiness> self.happiness_max :
            self.happiness = self.happiness_max
    
    
    def upgrade(self) :
        self.level += 1
        self.happiness_max += self.base_value
        self.happiness = self.happiness_max//2
        
        
    def __str__(self) :
        return f"""
{self.name} :
    -> level : {self.level}
    -> happiness max : {self.happiness_max}
    -> current  happiness : {self.happiness}
    -> happiness speed : {self.happiness_speed}
    """
    
        
    

