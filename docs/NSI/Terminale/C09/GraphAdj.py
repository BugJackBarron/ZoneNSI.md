class GraphV1 :
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
        
        
class GraphV2 :
    def __init__(self) :
        self.adj = {}
        
    def add_vertice(self,s) :
        if s not in self.adj :
            self.adj[s] = set() # crée un objet set vide, et graranti l'unicité de chaque élément
        
    def add_edge(self, s, e, p=1) :
        self.add_vertice(s)
        self.add_vertice(e)
        self.adj[s].add((e,p)) # La méthode add des objets de type set
        
    def __repr__(self) :
        return str(self.adj)
        
class GraphV3 :
    def __init__(self) :
        self.adj = {}
        self.edges = {}
        
    def add_vertice(self,s) :
        if s not in self.adj :
            self.adj[s] = set() # crée un objet set vide, et graranti l'unicité de chaque élément
        
    def add_edge(self, s, e, p=1) :
        self.add_vertice(s)
        self.add_vertice(e)
        self.adj[s].add(e) # La méthode add des objets de type set
        self.edges[(s,e)] = p
        
    def __repr__(self) :
        return str(self.adj)
        
        
