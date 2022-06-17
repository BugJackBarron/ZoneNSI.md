class Pile :
    def __init__(self) :
        self._stack = []
    
    def est_vide(self) :
        return self._stack == []
    
    def empiler(self, v) :
        self._stack.append(v)
    
    def depiler(self) :
        return self._stack.pop()
    
    def __repr__(self) :
        s=""
        for i in range(len(self._stack)) :
            s+=str(self._stack[-i-1])+"\n"
            s+="---"
        return s
            
    
def retourner(p, n) :
    p2 = Pile()
    p3 = Pile()
    for i in range(n) :
        p2.empiler(p.depiler())
    for i in range(n) :
        p3.empiler(p2.depiler())
    for i in range(n) :
        p.empiler(p3.depiler())
    return p

def  plus_grande(p,n) :
    pg = 
        
        
        
if __name__=="__main__" :
    s = [2,4,1,6,3,5]
    p= Pile()
    for e in s :
        p.empiler(e)