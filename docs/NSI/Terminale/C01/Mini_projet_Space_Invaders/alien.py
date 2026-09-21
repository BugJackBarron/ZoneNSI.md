from constantes import *
import pygame

class Alien:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20
        self.speed = 1
        self.direction = 1
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x + self.width >= WIDTH:
            self.direction *= -1
            self.y += 20
