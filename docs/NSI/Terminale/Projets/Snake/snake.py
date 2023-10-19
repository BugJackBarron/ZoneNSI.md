import pyxel



TITLE = "snake"
WIDTH = 200
HEIGHT = 160
CASE = 20
FRAME_REFRESH = 15

pyxel.init(WIDTH, HEIGHT, title=TITLE)
snake = [[3,3],[2,3],[1,3]]

direction = [1,0]
score = 0


def draw() :
    global snake
    pyxel.cls(1)
    for anneau in snake[1:] :
        x,y = anneau[0], anneau[1]
        pyxel.rect(x*CASE, y*CASE, CASE, CASE, 11)
    x_head, y_head = snake[0]
    pyxel.rect(x_head*CASE, y_head*CASE, CASE, CASE, 9)
    pyxel.text(4,4,f"Score : {score}", 7)
    
    
def update() :
    global snake
    global direction
    head = snake[0]    
    if pyxel.frame_count % FRAME_REFRESH == 0 :
        head = [snake[0][0]+direction[0], snake[0][1]+direction[1]]
        snake.insert(0, head)
        snake.pop(-1)
    
    if pyxel.btn(pyxel.KEY_ESCAPE) :
        exit()
    elif pyxel.btn(pyxel.KEY_RIGHT) and direction in ([0,1], [0,-1]):
        direction = [1,0]
    elif pyxel.btn(pyxel.KEY_LEFT) and direction in ([0,1], [0,-1]):
        direction = [-1,0]
    elif pyxel.btn(pyxel.KEY_UP) and direction in ([1,0], [-1,0]):
        direction = [0,-1]
    elif pyxel.btn(pyxel.KEY_DOWN) and direction in ([1,0], [-1,0]):
        direction = [0,1]
        
    if head in snake[1:] or head[0] < 0 or head[0] >WIDTH/CASE -1 or head[1]<0 or head[1]> HEIGHT/CASE -1 :
        exit()
    
        

pyxel.run(update, draw)