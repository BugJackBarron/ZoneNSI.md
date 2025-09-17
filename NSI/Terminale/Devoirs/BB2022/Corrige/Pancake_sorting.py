class Pile :
    def __init__(self) :
        self.p = []
        
    def est_vide(self) :
        return self.p == []
    
    def empiler(self, v) :
        self.p.append(v)
        
    def depiler(self) :
        return self.p.pop()
    
    def __repr__(self) :
        rep =""
        for i in range(len(self.p)) :
            rep += str(self.p[-i-1])
        return rep
    
def mystere(p):
    if p.est_vide ():
        return 0
    else :
        a = p.depiler()
        nb = 1 + mystere(p)
        p. empiler(a)
        return nb
    
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

def plus_grande(p, n) :
    tp=Pile()
    ipg = 1
    pg = p.depiler()
    i = 1
    tp.empiler(pg)
    while i<n :
        cp = p.depiler()
        tp.empiler(cp)
        i += 1
        if cp>pg :
            pg = cp
            ipg = i
    while not(tp.est_vide()) :
        p.empiler(tp.depiler())
    return ipg
    

def placer_plus_grande(p, n) :
    i = plus_grande(p, n)
    p = retourner(p,i)
    p = retourner(p,n)
    return p

def tri_crepes(p, nb) :
    for i in range(nb) :
        p = placer_plus_grande(p, nb-i)
    return p
    
    
    
if __name__ == "__main__" :
    p = Pile()
    for i in [2,4,1,6,3,5] :
        p.empiler(i)
    print(p)
    