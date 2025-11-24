import pygame as pg
from pygame.locals import *


#CURSOR_LEVEL= 5
RED = (255, 0, 0)
ORANGE = (255, 173, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
CURSOR_COLOURS = [RED, ORANGE, GREEN, BLUE, PURPLE ]
pg.init()
STARFONT = pg.font.Font('Starjout.ttf', 40)


class ForceMonster :
    def __init__(self, number, image, collect_pts = 1, force_max = 100, force_buff = 10, force_speed = 1, force_speed_buff = 1) :
        self.level = 0
        self.number = number
        self.collect_pts = collect_pts
        self.force_max = force_max
        self.actual_force = force_max//2
        self.force_buff = force_buff
        self.force_speed = force_speed
        self.force_speed_buff = force_speed_buff
        self.is_alive = True
        
        self.monster_frame = pg.Surface((130, 450))
        self.rect = self.monster_frame.get_rect()
        self.rect.center = (200*number, 250)
        self.monster_frame.set_colorkey((0,0,0))
        self.flamme_inverted = True
        
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (128, 152))
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (65, 144)
        self.force_bar = ForceBar(self.actual_force, self.force_max, (65, 310))
        self.feed_button = FeedButton(self, (65, 425))
        self.text = pg.font.Font('Starjout.ttf', 20
            ).render(f"Level {self.level:02d}", 1, (0,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (65,30)
        self.text_bg = pg.Surface(self.text.get_size())
        self.text_bg.fill((50, 50, 50))
        self.flamme = Flamme(self.image_rect.center)
        
        
    def decrease_force(self) :
        self.actual_force -= self.force_speed
        if self.actual_force <=0 :
            self.is_alive = False
            self.actual_force=0
            self.collect_pts = 0
        self.force_bar.set_actual_force(self.actual_force)
        
    def level_up(self) :
        if self.is_alive :
            self.level+=1
            self.force_max += self.force_buff
            self.actual_force = self.force_max//2
            self.force_speed += self.force_speed_buff+self.level%2
            self.collect_pts += self.level
            self.text = pg.font.Font('Starjout.ttf', 20
            ).render(f"Level {self.level:02d}", 1, (0, 255, 255))
            
            
            
        
    def show(self, main_frame, blit) :
        if self.is_alive :
            if blit :
                self.flamme_inverted = not(self.flamme_inverted)
            self.feed_button.show(self.monster_frame)
            self.force_bar.show(self.monster_frame, blit)
            level = max((self.actual_force *5)//self.force_max,0)
            if level == 5 :
                level = 4
            self.flamme.set_level(level) 
            self.flamme.show(self.monster_frame, self.flamme_inverted)
        else :
            self.monster_frame = pg.Surface((130, 400))
        self.monster_frame.blit(self.image, self.image_rect)
        self.text_bg.fill((50,50,50))
        self.text_bg.blit(self.text, (0,0))
        self.monster_frame.blit(self.text_bg, self.text_rect)
        main_frame.blit(self.monster_frame, self.rect)
        
            
    def collidepoint(self, mouse_position) :
        return self.feed_button.rect.collidepoint((mouse_position[0] - self.rect.left, mouse_position[1] - self.rect.top))        
        
        
class ForceSquareLevel :
    def __init__(self, color, yshift, container_rect) :
        self.square = pg.Surface((30, 30))
        self.rect = self.square.fill(color)
        self.rect.centerx = container_rect.centerx
        self.rect.centery = container_rect.centery + yshift
        
class ForceBar :
    def __init__(self, actual_force, force_max, center_position) :
        self.force_max = force_max
        self.actual_force = actual_force
        self.container = pg.Surface((40, 180))
        self.rect = self.container.get_rect()
        self.rect.center = center_position
        self.container.fill((50,50,50))
        self.last_blitting = True # make the upper square blit
        self.squares = [ForceSquareLevel(RED, 70, self.rect),
                        ForceSquareLevel(ORANGE, 35, self.rect),
                        ForceSquareLevel(GREEN, 0, self.rect),
                        ForceSquareLevel(BLUE, -35, self.rect),
                        ForceSquareLevel(PURPLE, -70, self.rect)
            ]
        
    def set_actual_force(self, value) :
        self.actual_force = value
        
    def show(self, surface, blit) :
        if blit :
            self.last_blitting= not(self.last_blitting)
        surface.blit(self.container, self.rect)
        level = (self.actual_force*5)//self.force_max-1*self.last_blitting
        if level <= -1 :
            level = 0
        if level >= 5 :
            level = 4
        for i in range(level+1) :
            try :
                surface.blit(self.squares[i].square, self.squares[i].rect)
            except IndexError :
                raise IndexError(f"Index {i} in square blit") 
        
        


class ForceButton :
    def __init__(self) :
        self. image = pg.Surface((100,50))
        self.rect = self.image.fill((0,255,0))
        self.rect.center=(600, 525)
        self.text = pg.font.Font(pg.font.match_font('starjedioutline'), 25).render('FARM', 1, (50,50,50))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        
    def show(self, frame_to_blit) :
        frame_to_blit.blit(self.image, self.rect)
        frame_to_blit.blit(self.text, self.text_rect)
        

class FeedButton :
    def __init__(self, monster, center_position) :
        self.monster = monster
        self.button = pg.Surface((80, 50))
        self.rect = self.button.fill((50,50,50))
        self.rect.center = center_position
        self.text = pg.font.Font(pg.font.match_font('starjedioutline'), 25).render('FEED', 1, (0,255,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.rect.center
        
    def show(self, surface) :
        surface.blit(self.button, self.rect)
        surface.blit(self.text, self.text_rect)
        
    def feed(self, force_point) :
        diff = self.monster.force_max -self.monster.actual_force
        if diff > force_point :
            self.monster.actual_force += force_point
            return 0
        else :
            
            self.monster.level_up()
            return force_point-diff
            
            
        
        


class ForceCounter :
    def __init__(self) :
        self.value = 0
        self.growth_rate = 1
        self.text = f"Force : {self.value}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (50,550)
        
    def show(self, frame_to_blit) :
        frame_to_blit.blit(self.surface, self.rect)
        
    def update_text(self) :
        #self.value +=self.growth_rate
        self.text = f"Force : {self.value}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        
    def reinit(self, value) :
        self.valeur = value
        self.update()
        
    def get_value(self) :
        return self.value
    
    def set_value(self, value) :
        self.value = value
        
    def update_value(self) :
        self.value +=self.growth_rate
        self.update_text()
        
    def set_growth_rate(self, value) :
        self.growth_rate = value
    
class ScoreCounter :
    def __init__(self) :
        self.value = 0
        self.text = f"Score : {self.value:06d}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (700,550)
        
    def show(self, frame_to_blit) :
        frame_to_blit.blit(self.surface, self.rect)
        
    def update_text(self) :
        self.text = f"Score : {self.value:06d}"
        self.surface = STARFONT.render(self.text, 1, (0, 255, 0))
        
    def reinit(self, value) :
        self.valeur = value
        self.update()
        
    def get_value(self) :
        return self.value
    
    def set_value(self, value) :
        self.value = value
        
    def update_value(self, value) :
        self.value += value
        self.update_text()
        
   

class Flamme :
    def __init__(self, center, level=2) :
        self.center = center
        self.level = level
        self.colors= {0 : 'R',
                      1 : 'O',
                      2 : 'G',
                      3 : 'B',
                      4 : 'P'}
        
        
    def show(self,frame, inversed = False) :
        if not(inversed) :
            flamme = pg.transform.scale(pg.image.load(f'Flamme{self.colors[self.level]}.png').convert_alpha(), (128, 152))
        else :
            flamme = pg.transform.scale(pg.image.load(f'Flamme{self.colors[self.level]}I.png').convert_alpha(), (128, 152))
        flamme_rect=flamme.get_rect()
        flamme_rect.center = self.center
        frame.blit(flamme, flamme_rect)
        
    def set_level(self, value) :
        self.level = value
    
        
    
def main() :
    main_frame = pg.display.set_mode((1200, 675))
    
    background = pg.image.load('Cantina.png').convert()
    pg.display.set_caption('KawaiiWars')
    main_frame.blit(background, (0,0))
    game_playing = True
    force_button = ForceButton()
    force_counter = ForceCounter()
    score_counter = ScoreCounter()
    
    monsters = [ForceMonster(1, "Troops.png" , force_max = 10),
                ForceMonster(2, "Yoda.png", force_buff=5 ),
                ForceMonster(3, "Chewie.png",force_speed_buff = 3 ),
                ForceMonster(4, "Leia.png" ),
                ForceMonster(5, "Vador.png", force_max = 10, force_speed_buff = 3 )]
                
    
    
    decrease_force = pg.USEREVENT +0
    set_blit = pg.USEREVENT +1
    pg.time.set_timer(decrease_force, 1000)
    pg.time.set_timer(set_blit, 50)
    while game_playing :
        for monster in monsters :
            if monster.actual_force > monster.force_max :
                raise ValueError("Bug sur niveau de force")
        
        blit = False
        force_counter.set_growth_rate(sum([monster.collect_pts for monster in monsters]))
        for event in pg.event.get() :
            if event.type ==QUIT :
                game_playing = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 :
                mouse_position = pg.mouse.get_pos()
                if force_button.rect.collidepoint(mouse_position) :
                    force_counter.update_value()
                    score_counter.update_value(force_counter.growth_rate)
                for monster in monsters :
                    if monster.is_alive and monster.collidepoint(mouse_position) :
                        force_counter.set_value(monster.feed_button.feed(force_counter.get_value()))
                        force_counter.update_text()
                
                    
            if event.type == decrease_force :
                for monster in monsters :
                    monster.decrease_force()
                
            if event.type == set_blit :
                blit=True
        monsters_alive = sum([1 for monster in monsters if monster.is_alive])
        if monsters_alive == 0 :
            game_playing = False
        main_frame.blit(background, (0,0))
        for monster in monsters :
            monster.show(main_frame, blit)
        score_counter.show(main_frame)
        force_counter.show(main_frame)
        force_button.show(main_frame)
        pg.display.update()
    pg.quit()
    

if __name__ == "__main__" :
    main()