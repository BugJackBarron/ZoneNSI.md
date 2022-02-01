class Case :
    def __init__(self, pos, wall=[]) :
        self.pos = pos
        self.wall =  {i :True  if i in wall else False for i in  [1,2,3,4] }
        
    def addWall(self,  num) :
        self.wall[num] = True
    
    def addMultiple(self, *nums) :
        for e in nums :
            self.addWall(e)
        
    def delWall(self, num) :
        self.wall[num] = False
        
    
        
if __name__  == "__main__" :
    s = "{"
    for i in range(4) :
        for j in range(4) :
            s +=f"({i},{j}) : Case(({i},{j})),"
    s+="}"
    lab = eval(s)
    lab[(0,0)].addMultiple(1,4)
    lab[(0,1)].addMultiple(3)
    lab[(0,2)].addMultiple(1,2)
    lab[(0,3)].addMultiple(1,2,4)
    
    lab[(1,0)].addMultiple(4,3)
    lab[(1,1)].addMultiple(1,2)
    lab[(1,2)].addMultiple(3,4)
    lab[(1,3)].addMultiple(2,3)
    
    lab[(2,0)].addMultiple(1,4)
    lab[(2,1)].addMultiple(3)
    lab[(2,2)].addMultiple(1,3)
    lab[(2,3)].addMultiple(2,1)
    
    lab[(3,0)].addMultiple(3,4)
    lab[(3,1)].addMultiple(1,2,3)
    lab[(3,2)].addMultiple(1,3,4)
    lab[(3,3)].addMultiple(2,3)
    
    
    
