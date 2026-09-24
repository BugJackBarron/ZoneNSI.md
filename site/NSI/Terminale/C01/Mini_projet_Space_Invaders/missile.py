from constantes import *
import pygame

class Missile:
    def __init__(self, x, y, screen):
        self.x = x + 20
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = 7
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y -= self.speed