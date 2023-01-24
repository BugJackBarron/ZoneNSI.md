from p5 import *
from demineur import *

f = None
RED = Color(255,0,0)
GREEN = Color(0,255,0)
TAILLE = 10
started = False
grid = None
cell_size = 0
lost = False
win = False

def start_game(mode, taille=TAILLE) :
    game_mode ={'easy' : 1, 'normal' : TAILLE//4, 'hard' : TAILLE//2}
    make_grid(grid, TAILLE+game_mode[mode])

def draw_grid(grid, lost= False) :
    rect_mode(CENTER)
    
    for x in range(TAILLE) :
        for y in range(TAILLE) :
            fill(255)
            rect((230+x*cell_size, 40+y*cell_size), cell_size, cell_size)
            if grid[x][y].covered :
                fill(90)
                rect((230+x*cell_size, 40+y*cell_size), cell_size-2, cell_size-2)
                if grid[x][y].flag :
                    if grid[x][y].value != -1 and lost :
                        fill(RED)
                    else :
                        fill(0)
                    rect((230+x*cell_size, 40+y*cell_size), cell_size//2, cell_size//2)
                else :
                    if lost and grid[x][y].value == -1 :
                        fill(RED)
                        rect((230+x*cell_size, 40+y*cell_size), cell_size//2, cell_size//2)
            else :
                if grid[x][y].value == 0 :
                    fill(200)
                    rect((230+x*cell_size, 40+y*cell_size), cell_size-2, cell_size-2)
                elif grid[x][y].value == -1  :
                    fill(RED)
                    rect((230+x*cell_size, 40+y*cell_size), cell_size-2, cell_size-2)
                else :
                    fill(200)
                    rect((230+x*cell_size, 40+y*cell_size), cell_size-2, cell_size-2)
                    colors = {1: 'GREEN',
                          2 : 'ORANGE',
                          3 : 'BLUE',
                          4: 'RED',
                          5 : 'PURPLE',
                          6 : 'PURPLE',
                          7 : 'PURPLE',
                          8 : 'PURPLE',
                          }
                    fill(colors[grid[x][y].value])
                    text(str(grid[x][y].value), 230+x*cell_size, 40+y*cell_size)

def setup():
    global f, grid, cell_size
    size(640, 480)

    # Create the font
    f = create_font("DSEG14Classic-Bold.ttf", 14)
    text_font(f)
    text_align("CENTER")
    grid = init_grid(TAILLE)
    cell_size = 400//TAILLE
        
        

def draw():
    global TAILLE 
    background(102)
    text_align("CENTER", "CENTER")
    fill(RED)
    text("MINESWEEPER", (100, 20))
    fill(0)
    line(200, 0, 200,480)
    rect_mode(CENTER)
    for i,txt in enumerate(['easy', 'normal', 'hard']) :
        fill(80)
        rect(100,60+20*i, 80, 20)
        fill(GREEN)
        text(txt, (100, 60+20*i))
    
    if started :
        draw_grid(grid, lost)
        
    
    
    
    
def mouse_pressed() :
    global started, lost
    if not(started) :
        if 60<= mouse_x <= 140 :
            if 50 <= mouse_y <= 70 :
                start_game('easy')
            elif 70 <= mouse_y <= 90 :
                start_game('normal')
            elif 70 <= mouse_y <= 90 :
                start_game('hard')
            started = True
    elif not(lost) :
        if 230-cell_size//2<= mouse_x <= 230+TAILLE*cell_size+cell_size//2 :
            if 40-cell_size//2<= mouse_y <= 40+TAILLE*cell_size+cell_size//2 :
                px = int(mouse_x-230+cell_size//2)//cell_size
                
                py = int(mouse_y-40+cell_size//2)//cell_size
                print(f"case :({px}; {py})")
                print(mouse_button)
                print(grid[px][py].value)
                if mouse_button == 'LEFT' :
                    lost = not(apply_position(grid, False, px, py))
                else :
                    lost = not(apply_position(grid, True, px, py))

                
        
if __name__ == '__main__':
        run()