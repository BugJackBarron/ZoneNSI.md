from random import randint
import random
import colorama
from colorama import Fore, Style


class Cell :
    def __init__(self) :
        """ construit et initialise un objet de classe Cell possédant tro#is attributs :
- value, qui prend les valeurs  :
    * -1 si la cellule possède une bombe ;
    * sinon un entier de 0 à 8 représentant le nombre de bombes dans les cases vosines.
- flag, un booléen représentant le fait qu'une cellule possède un drapeau ou non ;
- covered : un booléen représentant une case couverte ou découverte.
        """
        self.value = 0
        self.flag = False
        self.covered = True
        
    def draw(self) :
        pass


def init_grid(taille) :
    """ Crée et renvoie une grille carré de dimension taille*taille
    dont chaque cellule est un objet de classe Cell, et renvoie cette grille sous la forme d'une liste de listes."""
    return [[Cell() for cy in range(taille)] for cx in range(taille)]


def compute_cell(grid, x, y) :
    """ Fonction mettant à jour et renvoyant la valeur d'une cellule ne comportant pas de bombes en fonction
du nombre de cases voisines comportant des bombes
Exemples sur la grille | 0 | -1 | -1 |
                       | 0 |  0 |  0 |
                       | 0 |  0 | -1 |
>>> grid = init_grid(3)
>>> grid[0][1].value = -1
>>> grid[0][2].value = -1
>>> grid[2][2].value = -1 
>>> compute_cell(grid, 1, 1)
3
>>> compute_cell(grid, 1, 0)
1
>>> compute_cell(grid, 0, 0)
1
>>> compute_cell(grid, 2, 0)
0
>>> compute_cell(grid, 1, 2)
3
>>> compute_cell(grid, 2, 2)
-1
    """
    taille=len(grid)
    if grid[x][y].value != -1 :
        for vx in [-1, 0, 1] :
            for vy in [-1, 0, 1] :
                    if 0<=x+vx<taille and 0<=y+vy<taille  :
                        if grid[x+vx][y+vy].value == -1 :
                            grid[x][y].value +=1
    return grid[x][y].value
                            
    
def make_grid(grid, nb_bombes) :
    """ fonction créant une grille avec nb_bombes bombes dissimulées et placées aléatoirement, et mettant à jour les valeurs de toutes les cases
Non testable avec doctest.
Attention, on ne doit pas placer une bombe sur une case déjà occupée par une autre bombe.
Cette fonction ne renvoie rien, puisqu'elle modifie la grille existante (mutabilité des listes en Python). 
    """
    taille=len(grid)
    nb_bombes_a_placer = nb_bombes
    while nb_bombes_a_placer>0 :
        n = random.randint(0,taille-1)
        m = random.randint(0,taille-1)
        if grid[n][m].value == 0 :
            grid[n][m].value = -1
            nb_bombes_a_placer -=1
    for x in range(taille) :
        for y in range(taille) :
            compute_cell(grid,x,y)


def affichegrid(grid, colors= False, detonate= False) :
    """ fonction traçant la grille dans la console
Si l'argument colors est True, alors certaines cases sont colorées :
- en vert lorsque le joueur agagné, on représente les bombes ;
- en rouge : lorsque le joueur a perdu, non seukement on représente les bombes mais aussi les drapeaux mal placés.
L'argument detonate permet de savoir si le joueur a perdu.
Non testatble dans doctest.
La fonction ne renvoie rien, et ne modifie pas la grille. Elle ne fait qu'afficher.
    """
    taille=len(grid)
    caracter_map={-1 : "◕", 0 : " "}
    for i in range(1,9) :
        caracter_map[i] = str(i)
    print("     "+"".join([f"{i:2d}  " for i in range(taille)]))
    print("    ╔"+'═══╦'*(taille-1)+"═══╗")
    for x in range(taille) :
        print(f"  {chr(65+x)} ", end="")
        for y in range(taille) :
            if grid[x][y].flag :
                if colors and grid[x][y].value != -1 :
                    print("║ "+Fore.RED+"◘"+Fore.WHITE+" ", end="" )
                elif colors and grid[x][y].value == -1 :
                    print("║ "+Fore.GREEN+"◘"+Fore.WHITE+" ", end="" )
                else :
                    print("║ ◘ ", end="" )
            elif grid[x][y].covered :
                if colors and grid[x][y].value == -1 and detonate :
                    print("║ "+Fore.RED+"◕"+Fore.WHITE+" ", end="" )
                elif colors and grid[x][y].value == -1  :
                    print("║ "+Fore.GREEN+"◕"+Fore.WHITE+" ", end="" )
                else :
                    print(f"║ █ ", end="" )
            else :
                print(f"║ {caracter_map[grid[x][y].value]} ", end="" )
        print("║")
        if x != taille -1 :
            print("    ╠"+'═══╬'*(taille-1)+"═══╣")
    print("    ╚"+'═══╩'*(taille-1)+"═══╝")
    

def ask_position(grid) :
    """ Fonction dumbProof demandant au joueur une position sous la forme suivante :
soit du type A3, B4, C0, etc... où la lettre représente l'indice de ligne (A=0, B=1, ...), et le chiffre l'indice de colonne.
    Une telle saisie découvre la case à laquelle elle fait référence.
soit du type fA5, fB6, etc... (donc comme ci-dessus, mais précédé d'un f) : place un drapeau sur la case correspondante.

La fonction renvoie un tuple de la forme (flag, x, y) où :
- flag est un booléen (drapeau ou non) ;
- x est un entier représentant l'indice de la ligne visée ;
- y est un entier représentant l'indice de la colonne visée;


Ainsi sur une grille de taille 5:
    - une saiie de type F3 ou B7 est invalide et doit être recommencée, tout comme une saisie de type 0B
    - la saisie fB3 renvoie le tuple (True, 1, 3)
    - la saisie E0 renvoie le tuple (False, 4, 0)
    
Non testable par doctest
"""
    taille=len(grid)
    while True :
        f = input("Votre position (Ligne/colone) ? (précédez d'un f pour flag une position)")
        if len(f) == 3 and f[0] == 'f' and f[2] in [str(i) for i in range(taille)] and f[1] in [chr(i+65) for i in range(taille)] :
            return (True, int(ord(f[1])-65),int(f[2]))
        elif len(f) == 2 and f[1] in [str(i) for i in range(taille)] and f[0] in [chr(i+65) for i in range(taille)] :
            return (False, int(ord(f[0])-65), int(f[1]))
        else :
            print("Saisie invalide")

def propagate(grid, x, y) :
    """ fonction propageant la découverte de cellules de proche en proche selon les règles classiques du démineur,
en partant d'une cellule dont les coordonnées x et y sont données, x étant l'indice de ligne, et y l'indice de colonne.
L'algorithme est le suivant :
1) On utilise deux listes, to_uncover qui contiendra la liste des coordonnées des cellules à découvrir, et to_compute
qui contiendra la liste des cellules sur lesquels on va travailler. Ces deux listes sont initialisées avec un élément,
le tuple (x,y)
2) tant que la liste to_compute n'est pas vide :
    a) retirer le dernier élément de to_compute, et garder les coordonnées obtenues
    b) si la cellule ayant ces coordonnées possède une valeur égale à 0, alors ajouter chacune de ses
        voisines à la fois à la liste to_compute et à la liste to_uncover
3) Parcourir la liste to_uncover et découvrir toutes les cellules correspondantes.
"""
    
    taille=len(grid)    
    to_uncover=[(x,y)]
    to_compute = [(x,y)]
    while to_compute !=[] :
        ax, ay = to_compute.pop()
        if grid[ax][ay].value == 0 :
            for vx in [-1,0,1] :
                for vy in [-1, 0, 1] :
                    if 0<= ax+vx < taille and 0<= ay+vy< taille :
                        if not (vx==0 and vy==0) :
                            if (ax+vx, ay+vy) not in to_uncover :
                                to_compute.append((ax+vx, ay+vy))
                                to_uncover.append((ax+vx, ay+vy))
    for c in to_uncover :
        x,y = c
        grid[x][y].covered = False



def apply_position(grid, flag, x, y) :
    """ fonction modifiant la grille selon la saisie proposée, et renvoyant True si la position est valide
(placement de drapeau ou case pouvant être découverte (= sans bombe)) et False si la position est celle d'une bombe.
Dans le cas où la case ne possède pas de bombe, fait appel à la fonction propagate pour découvrir toutes les cellules nécessaires"""
    
    taille=len(grid)
    if flag :
        grid[x][y].flag = True
        return True
    else :
        if grid[x][y].value == -1 :
            grid[x][y].covered = False
            return False
        else :
            propagate(grid,x,y)
            return True
        
def count_uncovered(grid) :
    """ fonction comptant le nombre de caese découvertes sur le plateau de jeu"""
    taille=len(grid)
    uncovered = 0
    for x in range(taille) :
        for y in range(taille) :
            uncovered += not(grid[x][y].covered)
    return uncovered
    

  

def main_console(taille, difficulte = 1) :
    """ Fonction principale, lançant une partie de démineur avec la taille donnée, et un nombre de bombe correspondant
à taille + difficulte.
En fin de partie, montre au joueur si il a perdu la position de toutes les bombes."""
    grid = init_grid(taille)
    BOMB_NUMBER = taille+difficulte
    make_grid(grid, BOMB_NUMBER)
    lost= False
    while (count_uncovered(grid) < (taille**2-BOMB_NUMBER)) and not(lost) :
        affichegrid(grid)
        flag, x, y = ask_position(grid)
        if not apply_position(grid,flag,x,y) :
            lost = True
    if lost :
        print("Perdu")
        affichegrid(grid, colors=True, detonate=True)
    else :
        print("Gagné !")
        affichegrid(grid, colors=True)




    
if __name__ == "__main__" :
    from doctest import testmod
    testmod()
    taille = 6
    main_console(taille, difficulte=3)