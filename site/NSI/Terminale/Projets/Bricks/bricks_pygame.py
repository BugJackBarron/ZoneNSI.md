import pygame as pg
from math import cos, sin, radians

# --- Constantes ---------------------------------------------------------
LARGEUR, HAUTEUR = 640, 480
FPS = 60

RAQUETTE_L, RAQUETTE_H = 90, 14
RAQUETTE_VITESSE = 450       # pixels par seconde
RAYON = 8
VITESSE_BALLE = 320          # pixels par seconde
VITESSE_MAX = 560

BRIQUE_L, BRIQUE_H = 58, 22
COLONNES, LIGNES = 10, 6
MARGE_HAUT = 60
ESPACE = 2                   # espace entre deux briques
VIES = 3

FOND = (20, 20, 35)
COULEUR_RAQUETTE = (230, 230, 240)
COULEUR_BALLE = (255, 255, 255)
COULEUR_TEXTE = (240, 240, 240)
COULEURS_BRIQUES = [(220, 50, 50), (240, 140, 30), (240, 220, 50),
                    (70, 200, 90), (50, 150, 230), (160, 80, 220)]


class Raquette:
    def __init__(self):
        self.rect = pg.Rect(0, 0, RAQUETTE_L, RAQUETTE_H)
        self.reinitialiser()

    def reinitialiser(self):
        self.rect.midbottom = (LARGEUR // 2, HAUTEUR - 20)
        self.x = float(self.rect.x)

    def deplacer(self, direction, dt):
        """direction vaut -1, 0 ou 1 ; dt est en secondes."""
        self.x += direction * RAQUETTE_VITESSE * dt
        self.x = max(0, min(LARGEUR - RAQUETTE_L, self.x))
        self.rect.x = round(self.x)

    def afficher(self, surface):
        pg.draw.rect(surface, COULEUR_RAQUETTE, self.rect, border_radius=6)


class Balle:
    def __init__(self):
        self.x = self.y = 0.0
        self.vx = self.vy = 0.0
        self.collee = True   # posée sur la raquette, en attente du lancement

    @property
    def rect(self):
        return pg.Rect(round(self.x - RAYON), round(self.y - RAYON), 2 * RAYON, 2 * RAYON)

    def poser_sur(self, raquette):
        self.collee = True
        self.x = raquette.rect.centerx
        self.y = raquette.rect.top - RAYON

    def lancer(self):
        self.collee = False
        self.vx, self.vy = 0.0, -VITESSE_BALLE

    def deplacer(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

    def rebondir_murs(self):
        """Rebonds sur les murs gauche, droit et haut."""
        if self.x < RAYON:
            self.x = RAYON
            self.vx = abs(self.vx)
        elif self.x > LARGEUR - RAYON:
            self.x = LARGEUR - RAYON
            self.vx = -abs(self.vx)
        if self.y < RAYON:
            self.y = RAYON
            self.vy = abs(self.vy)

    def rebondir_raquette(self, raquette):
        """L'angle de renvoi dépend de l'endroit où la balle touche la raquette."""
        if self.vy > 0 and self.rect.colliderect(raquette.rect):
            position = (self.x - raquette.rect.centerx) / (RAQUETTE_L / 2)   # de -1 à 1
            position = max(-1, min(1, position))
            angle = radians(position * 60)                                      # de -60° à 60°
            vitesse = min(VITESSE_MAX, (self.vx ** 2 + self.vy ** 2) ** 0.5)
            self.vx = vitesse * sin(angle)
            self.vy = -vitesse * cos(angle)
            self.y = raquette.rect.top - RAYON

    def rebondir_brique(self, brique):
        """Rebond sur l'axe où la balle a le moins pénétré dans la brique."""
        r, b = self.rect, brique.rect
        dx = min(r.right - b.left, b.right - r.left)
        dy = min(r.bottom - b.top, b.bottom - r.top)
        if dx < dy:
            self.vx = -self.vx
        else:
            self.vy = -self.vy

    def accelerer(self, facteur):
        vitesse = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if vitesse and vitesse * facteur <= VITESSE_MAX:
            self.vx *= facteur
            self.vy *= facteur

    def est_perdue(self):
        return self.y - RAYON > HAUTEUR

    def afficher(self, surface):
        pg.draw.circle(surface, COULEUR_BALLE, (round(self.x), round(self.y)), RAYON)


class Brique:
    def __init__(self, colonne, ligne):
        x = colonne * (BRIQUE_L + ESPACE) + ESPACE
        y = MARGE_HAUT + ligne * (BRIQUE_H + ESPACE)
        self.rect = pg.Rect(x, y, BRIQUE_L, BRIQUE_H)
        self.couleur = COULEURS_BRIQUES[ligne % len(COULEURS_BRIQUES)]
        self.points = 10 * (LIGNES - ligne)    # les briques du haut rapportent plus

    def afficher(self, surface):
        pg.draw.rect(surface, self.couleur, self.rect, border_radius=3)


def creer_briques():
    return [Brique(c, l) for l in range(LIGNES) for c in range(COLONNES)]


class Jeu:
    def __init__(self):
        pg.init()
        self.ecran = pg.display.set_mode((LARGEUR, HAUTEUR))
        pg.display.set_caption("Casse-briques")
        self.horloge = pg.time.Clock()
        self.police = pg.font.Font(None, 28)
        self.grande_police = pg.font.Font(None, 56)
        self.reinitialiser()

    def reinitialiser(self):
        self.raquette = Raquette()
        self.balle = Balle()
        self.balle.poser_sur(self.raquette)
        self.briques = creer_briques()
        self.score = 0
        self.vies = VIES
        self.etat = "jeu"       # "jeu", "perdu" ou "gagne"

    def gerer_evenements(self):
        """Renvoie False si le joueur veut quitter."""
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                return False
            if evenement.type == pg.KEYDOWN:
                if evenement.key == pg.K_ESCAPE:
                    return False
                if evenement.key == pg.K_SPACE:
                    if self.etat != "jeu":
                        self.reinitialiser()
                    elif self.balle.collee:
                        self.balle.lancer()
        return True

    def mettre_a_jour(self, dt):
        """dt est en secondes."""
        if self.etat != "jeu":
            return
        touches = pg.key.get_pressed()
        direction = touches[pg.K_RIGHT] - touches[pg.K_LEFT]
        self.raquette.deplacer(direction, dt)

        if self.balle.collee:
            self.balle.poser_sur(self.raquette)
            return

        self.balle.deplacer(dt)
        self.balle.rebondir_murs()
        self.balle.rebondir_raquette(self.raquette)
        self.gerer_briques()

        if self.balle.est_perdue():
            self.vies -= 1
            if self.vies == 0:
                self.etat = "perdu"
            else:
                self.balle.poser_sur(self.raquette)

    def gerer_briques(self):
        """Détruit au plus une brique par image pour éviter les double rebonds."""
        for brique in self.briques:
            if self.balle.rect.colliderect(brique.rect):
                self.balle.rebondir_brique(brique)
                self.balle.accelerer(1.01)
                self.briques.remove(brique)
                self.score += brique.points
                break
        if not self.briques:
            self.etat = "gagne"

    def afficher(self):
        self.ecran.fill(FOND)
        for brique in self.briques:
            brique.afficher(self.ecran)
        self.raquette.afficher(self.ecran)
        self.balle.afficher(self.ecran)
        self.ecran.blit(self.police.render(f"Score : {self.score}", True, COULEUR_TEXTE), (10, 10))
        vies = self.police.render(f"Vies : {self.vies}", True, COULEUR_TEXTE)
        self.ecran.blit(vies, vies.get_rect(topright=(LARGEUR - 10, 10)))
        if self.etat != "jeu":
            titre = "Gagné !" if self.etat == "gagne" else "Perdu !"
            self.centrer(self.grande_police, titre, HAUTEUR // 2 + 30)
            self.centrer(self.police, "Espace : rejouer", HAUTEUR // 2 + 70)
        elif self.balle.collee:
            self.centrer(self.police, "Espace : lancer la balle", HAUTEUR // 2 + 70)
        pg.display.flip()

    def centrer(self, police, texte, y):
        image = police.render(texte, True, COULEUR_TEXTE)
        self.ecran.blit(image, image.get_rect(center=(LARGEUR // 2, y)))

    def lancer(self):
        en_cours = True
        while en_cours:
            dt = self.horloge.tick(FPS) / 1000
            en_cours = self.gerer_evenements()
            self.mettre_a_jour(dt)
            self.afficher()
        pg.quit()


if __name__ == "__main__":
    Jeu().lancer()
