from p5 import *

f = None
RED = Color(255,0,0) 

def setup():
        global f
        size(640, 360)

        # Create the font
        f = create_font("DSEG14Classic-Bold.ttf", 14)
        text_font(f)
        text_align("CENTER")
        
        

def draw():
        background(102)
        text_align("CENTER")
        fill(RED)
        text("MINESWEEPER", (100, 20))
        fill(0)
        line(200, 0, 200,480)
        
        

def drawType(x):
        line((x, 0), (x, 65))
        line((x, 220), (x, height))
        fill(0)
        text("ichi", (x, 95))
        fill(51)
        text("ni", (x, 130))
        fill(204)
        text("san", (x, 165))
        fill(255)
        text("shi", (x, 210))

if __name__ == '__main__':
        run()