class Case :
    def __init__(self, pos, neighbours=[]) :
        self.pos = pos
        self.neighbours =  {i :True  if i in neighbours else False for i in  [1,2,3,4] }
        
    def addNeighbour(self,  num) :
        self.neighbours[num] = True
    
    def addMultiple(self, *nums) :
        for e in nums :
            self.addNeighbour(e)
        
    def delNeighbour(self, num) :
        self.neighbours[num] = False
        
if __name__  == "__main__" :
    s = "{"
    for i in range(4) :
        for j in range(4) :
            s +=f"({i},{j}) : Case(({i},{j})),"
    s+="}"
    lab = eval(s)
    lab[(0,0)].addMultiple(3,4)
    
