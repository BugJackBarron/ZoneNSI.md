class Graph :
    def __init__(self, n=0) :
        self.n = n
        self.adj = [[0]*n for _ in range(n)]
        
    def add_vertice(self) :
        self.n +=1
        for l in self.adj :
            l.append(0)
        self.adj.append([0]*(self.n))
        
    def add_edge(self, s, t, p=1) :
        self.adj[s][t] = p
        
    def __repr__(self) :
            return str(self.adj)
