import pygame as pg
from random import randint


class HappinessLevel :
    def __init__(self, startLevel = 2) :
        pass
    
class KawaiiMonster :
    
    def __init__(self, name : str, image_base :str, happiness_max  : int = 100, happiness_speed : int = 2, upgrade_happiness : int= 100) :
        self. name = name
        self.image_base = image_base
        self.happiness_max= happiness_max
        self.happiness_speed = happiness_speed
        self.happiness = self.happiness_max
        self.upgrade_happiness = upgrade_happiness
        self.level = 1
        
    def sad(self) :
        self.happiness -= self.happiness_speed*self.level
            
        
    def feed(self, value) :
        self.happiness += value
    
    
    def upgrade(self) :
        self.level += 1
        self.happiness_max += self.upgrade_happiness
        self.happiness = self.happiness_max//2
        
        
    def __str__(self) :
        return f"""
{self.name} :
    -> level : {self.level}
    -> happiness max : {self.happiness_max}
    -> current  happiness : {self.happiness}
    -> happiness speed : {self.happiness_speed}
    """
    
        
    

