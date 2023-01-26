from p5 import *
from demineur import *

f = None
RED = Color(255,0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)

TAILLE = 10
started = False
grid = None
cell_size = 0
lost = False
win = False
game_mode ={'easy' : 1, 'normal' : TAILLE//4, 'hard' : TAILLE//2}
actual_mode = None

def start_game(mode, taille=TAILLE) :
    
    make_grid(grid, TAILLE+game_mode[mode])

def draw_grid(grid, lost= False, win = False) :
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
                        rect((230+x*cell_size, 40+y*cell_size), cell_size/-2, cell_size-2)
                    elif grid[x][y].value != -1 and win :
                        fill(GREEN)
                        rect((230+x*cell_size, 40+y*cell_size), cell_size/-2, cell_size-2)
                    else :
                        fill(BLUE)
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

def restart() :
    global started, lost, win
    started = False
    win= False
    lost = False
    setup()

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
        fill(RED)
        rect(100,200, 80, 40)
        fill(0)
        text('RESTART', (100, 200))
        draw_grid(grid, lost)
        fill(RED)
        text(f'Bombs : {TAILLE+game_mode[actual_mode]}', (100, 300))
        fill(BLUE)
        text(f'flags : {count_flagged(grid)}', (100, 350))
        
        
    if win :
        fill(GREEN)
        text('YOU WIN ', (100, 400))
        draw_grid(grid, win = True)

    if lost :
        fill(GREEN)
        text('YOU LOST ', (100, 400))
        draw_grid(grid, lost = True)

    
    
    
def mouse_pressed() :
    global started, lost, win, actual_mode
    if not(started) :
        if 60<= mouse_x <= 140 :
            if 50 <= mouse_y <= 70 :
                actual_mode = 'easy'
                
            elif 70 <= mouse_y <= 90 :
                actual_mode = 'normal'
                
            elif 70 <= mouse_y <= 90 :
                actual_mode = 'hard'
            start_game(actual_mode)
            started = True
    elif not(lost) and not(win):
        if 60<=mouse_x<=140 and 180<=mouse_y<=220 :
            restart()
        if 230-cell_size//2<= mouse_x <= 230+TAILLE*cell_size+cell_size//2 :
            if 40-cell_size//2<= mouse_y <= 40+TAILLE*cell_size+cell_size//2 :
                px = int(mouse_x-230+cell_size//2)//cell_size
                py = int(mouse_y-40+cell_size//2)//cell_size
                if mouse_button == 'LEFT' :
                    lost = not(apply_position(grid, False, px, py))
                else :
                    lost = not(apply_position(grid, True, px, py))
                
    else :
        if 60<=mouse_x<=140 and 180<=mouse_y<=220 :
            restart()
    print(count_uncovered(grid)+count_flagged(grid)==TAILLE**2)
    if not(lost) and count_uncovered(grid)+count_flagged(grid) == TAILLE**2 :
        win = True
    
        
if __name__ == '__main__':
    run()