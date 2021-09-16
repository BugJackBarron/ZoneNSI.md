import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))
continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.update()
pygame.quit()
