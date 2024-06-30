import turtle

STANDARDSCALE = 40


def convert(pos, scale = STANDARDSCALE) :
    """ convert position from the maze into réeal turtle coordinates"""
    l, c = pos
    return scale*c, -scale*l

def getCase(pos, scale=STANDARDSCALE) :
    """ Bien plus difficile..."""
    x,y = pos
    return -(y-0.5*scale)//scale, (x+0.5*scale)//scale

class Case :
    def __init__(self, pos, wall=[]) :
        self.pos = pos
        self.wall =  {i :True  if i in wall else False for i in  range(4) }
        
    def addWall(self,  num) :
        self.wall[num] = True
    
    def addMultiple(self, *nums) :
        for e in nums :
            self.addWall(e)
        
    def delWall(self, num) :
        self.wall[num] = False
        
    def draw(self, scale=STANDARDSCALE) :
        nt = turtle.Turtle()
        nt.speed(0)
        x, y = convert(self.pos, scale=scale)
        nt.up()
        nt.setpos(x-0.5*scale,y+0.5*scale)
        nt.setheading(0)
        for i in range(4) :
            if self.wall[i] :
                nt.down()
            nt.forward(scale)
            nt.up()
            nt.right(90)
        nt.ht()
        del(nt)
        
        
def nextMove(t,case) :
    cv = {90 : 0, 0 : 1, 180 : 3, 270 : 2}
    direction = cv[t.heading()]
    if not(case.wall[(direction+1)%4]) :
        return 'R'
    elif not(case.wall[direction]) :
        return 'F'
    elif not(case.wall[(direction-1)%4]) :
        return 'L'
    else :
        return 'B'    

       
if __name__  == "__main__" :
    s = "{"
    for i in range(4) :
        for j in range(4) :
            s +=f"({i},{j}) : Case(({i},{j})),"
    s+="}"
    lab = eval(s)
    lab[(0,0)].addMultiple(0,3)
    lab[(0,1)].addMultiple(2)
    lab[(0,2)].addMultiple(0,1)
    lab[(0,3)].addMultiple(0,1,3)
    
    lab[(1,0)].addMultiple(3,2)
    lab[(1,1)].addMultiple(0,1)
    lab[(1,2)].addMultiple(2,3)
    lab[(1,3)].addMultiple(1,2)
    
    lab[(2,0)].addMultiple(0,3)
    lab[(2,1)].addMultiple(2)
    lab[(2,2)].addMultiple(0,2)
    lab[(2,3)].addMultiple(1,0)
    
    lab[(3,0)].addMultiple(2,3)
    lab[(3,1)].addMultiple(0,1,2)
    lab[(3,2)].addMultiple(0,2,3)
    lab[(3,3)].addMultiple(1,2)
    
    screen = turtle.Screen()
    screen.bgcolor('lightgray')
    
    for i in range(4) :
        for j in range(4) :
            lab[(i,j)].draw()
            
    t=turtle.Turtle()
    t.pencolor('red')
    t.up()
    t.setposition(convert((3,2)))
    t.down()
    path=''
    actualCase = (3,2)
    while actualCase[0] in [0,1,2,3] and actualCase[1] in [0,1,2,3] :
        newMove = nextMove(t, lab[actualCase])
        path +=  newMove
        if newMove == 'F' :
            pass
        elif newMove == 'R' :
            t.right(90)
        elif newMove == 'L' :
            t.left(90)
        else :
            t.left(180)
        t.forward(STANDARDSCALE)
        actualCase = getCase(t.pos())

print(f"R :{path.count('R')}\n F :{path.count('F')}\n L :{path.count('L')}\n B :{path.count('B')}\n")
