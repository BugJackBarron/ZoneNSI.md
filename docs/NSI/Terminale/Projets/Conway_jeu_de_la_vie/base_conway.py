import pygame as pg
from pygame.locals import *
from random import choice, randint

class Cell :
    def __init__(self, x, y, state, size):
        self.x = x
        self.y = y
        self.size = size
        self.state  = state
        
class Grid :
    def __init__(self, width, height, cell_size, rules):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.rules = rules
        self.cells = [[Cell(x, y, "unborn", cell_size) for x in range(width)] for y in range(height)]

    def draw(self, surface, cell_color=(255, 255, 255)):
        for row in self.cells:
            for cell in row:
                color = cell_color if cell.state == "alive" else (0, 0, 0)
                pg.draw.rect(surface, color, (cell.x * self.cell_size, cell.y * self.cell_size, self.cell_size, self.cell_size))
                pg.draw.rect(surface, (40, 40, 40), (cell.x * self.cell_size, cell.y * self.cell_size, self.cell_size, self.cell_size), 1)  
                
    def get_neighbors(self, x, y):
        neighbors = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    neighbors.append(self.cells[ny][nx])
        return neighbors
    
    def is_clicked(self, mouse_x, mouse_y) :
        x = mouse_x // self.cell_size
        y = mouse_y // self.cell_size
        if self.cells[y][x].state == "dead" or self.cells[y][x].state == "unborn" :
            self.cells[y][x].state = "alive"
        else :
            self.cells[y][x].state = "unborn" 

    
    def update(self):
        new_states = [[cell.state for cell in row] for row in self.cells]
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                neighbors = self.get_neighbors(x, y)
                alive_neighbors = sum(1 for n in neighbors if n.state == "alive")
                
                if cell.state == "alive":
                    if alive_neighbors < self.rules['underpopulation'] or alive_neighbors > self.rules['overpopulation']:
                        new_states[y][x] = "dead"
                elif cell.state == "unborn" or cell.state == "dead":
                    if alive_neighbors == self.rules['born']:
                        new_states[y][x] = "alive"    
                    elif alive_neighbors in self.rules['survive']:
                        new_states[y][x] = "alive"
        
        for y, row in enumerate(self.cells):
            for x, cell in enumerate(row):
                cell.state = new_states[y][x]
    
def main():
    pg.init()
    cell_size = 15
    grid_width, grid_height = 60, 40
    screen = pg.display.set_mode((grid_width * cell_size, grid_height * cell_size))
    clock = pg.time.Clock()
    
    rules = {
        'underpopulation': 2,
        'overpopulation': 3,
        'born': 3,
        'survive':(3,)
    }
    
    grid = Grid(grid_width, grid_height, cell_size, rules)
    
    # Initial configuration (Glider)
    grid.cells[9][9].state = "alive"
    grid.cells[8][11].state = "alive"
    grid.cells[9][11].state = "alive"
    grid.cells[10][11].state = "alive"
    grid.cells[10][10].state = "alive"
    
    
    updating = False
    running = True
    screen.fill((0, 0, 0))
    grid.draw(screen)
    pg.display.flip()
    grid.update()
    while running:
        for event in pg.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    updating = 1-updating
                if event.key == K_n :
                    screen.fill((0, 0, 0))
                    grid.draw(screen, (255,0,0))
                    grid.update()                    
                    grid.draw(screen)
                    pg.display.flip()
            if event.type == MOUSEBUTTONDOWN :
                mouse_x, mouse_y = event.pos
                grid.is_clicked(mouse_x, mouse_y)
                screen.fill((0, 0, 0))
                grid.draw(screen)
                pg.display.flip()
        if updating: 
            screen.fill((0, 0, 0))
            grid.draw(screen)
            pg.display.flip()
            grid.update()
            clock.tick(10)
    
    pg.quit()
    
if __name__ == "__main__":
    main()
    

        