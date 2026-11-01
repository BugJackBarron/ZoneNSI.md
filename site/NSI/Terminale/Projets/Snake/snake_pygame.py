import pygame as pg
from random import randint

# --- Constantes ---------------------------------------------------------
CASE = 20                    # taille d'une case en pixels
COLONNES, LIGNES = 20, 15    # taille de la grille en cases
LARGEUR, HAUTEUR = COLONNES * CASE, LIGNES * CASE
FPS = 60
DELAI_DEPART = 150           # ms entre deux déplacements du serpent
DELAI_MIN = 60

FOND = (30, 30, 40)
COULEUR_TETE = (255, 170, 0)
COULEUR_CORPS = (60, 200, 90)
COULEUR_POMME = (220, 40, 40)
COULEUR_TEXTE = (240, 240, 240)

HAUT, BAS, GAUCHE, DROITE = (0, -1), (0, 1), (-1, 0), (1, 0)
TOUCHES = {pg.K_UP: HAUT, pg.K_DOWN: BAS, pg.K_LEFT: GAUCHE, pg.K_RIGHT: DROITE}


class Serpent:
    def __init__(self):
        self.corps = [(5, 7), (4, 7), (3, 7)]   # la tête est en position 0
        self.direction = DROITE
        self.prochaine_direction = DROITE
        self.a_grandir = False

    @property
    def tete(self):
        return self.corps[0]

    def changer_direction(self, nouvelle):
        """Refuse le demi-tour (comparé à la direction réellement suivie)."""
        opposee = (-self.direction[0], -self.direction[1])
        if nouvelle != opposee:
            self.prochaine_direction = nouvelle

    def avancer(self):
        self.direction = self.prochaine_direction
        x, y = self.tete
        dx, dy = self.direction
        self.corps.insert(0, (x + dx, y + dy))
        if self.a_grandir:
            self.a_grandir = False
        else:
            self.corps.pop()

    def grandir(self):
        self.a_grandir = True

    def mord_sa_queue(self):
        return self.tete in self.corps[1:]

    def sort_de_la_grille(self):
        x, y = self.tete
        return not (0 <= x < COLONNES and 0 <= y < LIGNES)

    def afficher(self, surface):
        for i, (x, y) in enumerate(self.corps):
            couleur = COULEUR_TETE if i == 0 else COULEUR_CORPS
            pg.draw.rect(surface, couleur, (x * CASE, y * CASE, CASE - 1, CASE - 1))


class Pomme:
    def __init__(self, serpent):
        self.position = (0, 0)
        self.replacer(serpent)

    def replacer(self, serpent):
        """Choisit une case libre au hasard."""
        while True:
            position = (randint(0, COLONNES - 1), randint(0, LIGNES - 1))
            if position not in serpent.corps:
                self.position = position
                return

    def afficher(self, surface):
        x, y = self.position
        pg.draw.rect(surface, COULEUR_POMME, (x * CASE, y * CASE, CASE - 1, CASE - 1))


class Jeu:
    def __init__(self):
        pg.init()
        self.ecran = pg.display.set_mode((LARGEUR, HAUTEUR))
        pg.display.set_caption("Snake")
        self.horloge = pg.time.Clock()
        self.police = pg.font.Font(None, 28)
        self.reinitialiser()

    def reinitialiser(self):
        self.serpent = Serpent()
        self.pomme = Pomme(self.serpent)
        self.score = 0
        self.delai = DELAI_DEPART
        self.temps_depuis_pas = 0
        self.perdu = False

    def gerer_evenements(self):
        """Renvoie False si le joueur veut quitter."""
        for evenement in pg.event.get():
            if evenement.type == pg.QUIT:
                return False
            if evenement.type == pg.KEYDOWN:
                if evenement.key == pg.K_ESCAPE:
                    return False
                if self.perdu:
                    if evenement.key == pg.K_SPACE:
                        self.reinitialiser()
                elif evenement.key in TOUCHES:
                    self.serpent.changer_direction(TOUCHES[evenement.key])
        return True

    def mettre_a_jour(self, dt):
        if self.perdu:
            return
        self.temps_depuis_pas += dt
        if self.temps_depuis_pas < self.delai:
            return
        self.temps_depuis_pas -= self.delai
        self.serpent.avancer()
        if self.serpent.sort_de_la_grille() or self.serpent.mord_sa_queue():
            self.perdu = True
        elif self.serpent.tete == self.pomme.position:
            self.serpent.grandir()
            self.score += 1
            self.delai = max(DELAI_MIN, self.delai - 4)
            self.pomme.replacer(self.serpent)

    def afficher(self):
        self.ecran.fill(FOND)
        self.pomme.afficher(self.ecran)
        self.serpent.afficher(self.ecran)
        self.ecran.blit(self.police.render(f"Score : {self.score}", True, COULEUR_TEXTE), (6, 4))
        if self.perdu:
            message = self.police.render("Perdu ! Espace : rejouer", True, COULEUR_TEXTE)
            self.ecran.blit(message, message.get_rect(center=(LARGEUR // 2, HAUTEUR // 2)))
        pg.display.flip()

    def lancer(self):
        en_cours = True
        while en_cours:
            dt = self.horloge.tick(FPS)
            en_cours = self.gerer_evenements()
            self.mettre_a_jour(dt)
            self.afficher()
        pg.quit()


if __name__ == "__main__":
    Jeu().lancer()
