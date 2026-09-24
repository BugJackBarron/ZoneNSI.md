import pygame
import random
from constantes import *
from alien import Alien
from missile import Missile
from vaisseau import Vaisseau

# Initialisation
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Space Invaders")
clock = pygame.time.Clock()



# --- Initialisation des objets ---
player = Vaisseau(screen)
missiles = []
aliens = [Alien(x * 80 + 50, 50, screen) for x in range(8)]

# --- Boucle principale ---
running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Contrôles clavier
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")
    if keys[pygame.K_SPACE]:
        if len(missiles) < 5:  # Limite de tirs à l'écran
            missiles.append(Missile(player.x, player.y, screen))

    # Déplacement des objets
    for alien in aliens:
        alien.move()

    # La notation missiles[:] effectue une copie de la liste missiles
    # nécessaire car on modifie l'objet missile dans le corps de la boucle.

    for missile in missiles[:]: 
        missile.move()
        if missile.y < 0:
            missiles.remove(missile)

    # Détection de collisions
    for missile in missiles[:]:
        for alien in aliens[:]:
            if (alien.x < missile.x < alien.x + alien.width and
                alien.y < missile.y < alien.y + alien.height):
                missiles.remove(missile)
                aliens.remove(alien)
                break

    # Dessin des objets
    player.draw()
    for missile in missiles:
        missile.draw()
    for alien in aliens:
        alien.draw()

    # Affichage
    pygame.display.flip()

pygame.quit()
