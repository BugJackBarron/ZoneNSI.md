from constantes import *
import pygame

class Vaisseau:
    def __init__(self, screen):
        self.width = 50
        self.height = 20
        self.x = WIDTH // 2 - self.width // 2
        self.y = HEIGHT - 60
        self.speed = 5
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < WIDTH - self.width:
            self.x += self.speed