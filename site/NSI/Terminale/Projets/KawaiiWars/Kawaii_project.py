import pygame as pg
from pygame.locals import *
from random import randint

CURSOR_LEVEL= 5
RED = (255, 0, 0)
ORANGE = (255, 173, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CURSOR_COLOURS = [RED, ORANGE, GREEN, BLUE, PURPLE ]
pg.init()
STARFONT = pg.font.Font(pg.font.match_font('starjedioutline'), 64)


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
    
class Flamme :
    def __init(self, 
    
class ForceButton :
    def __init__(self) :
        self. image = pg.Surface((100,50))
        self.rect = self.image.fill((0,255,0))
        self.rect.center=(1000, 500)
        
    def show(self, frame_to_blit) :
        frame_to_blit.blit(self.image, self.rect)
        


class ForceCounter :
    def __init__(self) :
        self.value = 0
        self.growth_rate = 1
        self.text = f"Force Points : {self.value}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (50,50)
        
    def show(self, frame_to_blit) :
        frame_to_blit.blit(self.surface, self.rect)
        
    def update(self) :
        self.value +=self.growth_rate
        self.text = f"Force Points : {self.value}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        
    def reinit(self) :
        self.valeur = 0
        self.update()
        
    def get_event(self) :
        pass
    
    
    
        
    
def main() :
    main_frame = pg.display.set_mode((1200, 675))
    background = pg.image.load('Cantina.png').convert()
    pg.display.set_caption('KawaiiWars')
    main_frame.blit(background, (0,0))
    game_playing = True
    force_button = ForceButton()
    force_counter = ForceCounter()
    red_flamme = pg.Surface((64,76), pg.SRCALPHA, 32).convert_alpha()
    red_flamme = pg.transform.scale(red_flamme, (128, 152))
    red_flamme_image = (pg.transform.scale(pg.image.load('FlammeP.png').convert_alpha(), (128, 152)),
                  pg.transform.scale(pg.image.load('FlammePI.png').convert_alpha(), (128, 152)))
    
    red_flamme_rect=red_flamme.get_rect()
    red_flamme_rect.midbottom = (600, 300)
    
    
    troop = pg.transform.scale(pg.image.load('Troops.png').convert_alpha(), (128, 152))
    troop_rect=troop.get_rect()
    troop_rect.midbottom=(600,300)
    
    flamme_counter = 0
    decrease_force = pg.USEREVENT +0
    pg.time.set_timer(decrease_force, 1000)
    tc = 0
    while game_playing :
        flamme_counter = 1 -flamme_counter
        for event in pg.event.get() :
            if event.type ==QUIT :
                game_playing = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 :
                mouse_position = pg.mouse.get_pos()
                if force_button.rect.collidepoint(mouse_position) :
                    force_counter.update()
            if event.type == decrease_force :
                ...
                
                    
        main_frame.blit(background, (0,0))
        red_flamme.blit(red_flamme_image[flamme_counter], (0,0))
        main_frame.blit(red_flamme, red_flamme_rect)
        main_frame.blit(troop, troop_rect)
        force_counter.show(main_frame)
        force_button.show(main_frame)
        pg.display.update()
    pg.quit()
    

if __name__ == "__main__" :
    main()