class GraphV1 :
    def __init__(self, n=0) :
        self.n = n
        self.adj = [[0]*n for _ in range(n)]

    def add_vertice(self) :
        self.n +=1
        for l in self.adj :
            l.append(0)
        self.adj.append([0]*(self.n))

    def add_edge(self, s, e, p=1) :
        self.adj[s][e] = p
        
    def exist_edge(self, s, e) :
        return self.adj[s][e] !=0
    
    def get_vertices(self) :
        return range(self.n)

    def get_order(self) :
        return self.n

    def get_neighbours(self,s) :
        neighbours = []
        for i in range(self.n) :
            if self.adj[s][i] !=0 :
                neighbours.append(i)
        return neighbours

    def get_degree(self, s):
        deg = 0
        for i in range(self.n) :
            deg += self.adj[s][i]!=0
            deg += self.adj[i][s]!=0
        return deg

    def is_directed(self) :
        for i in range(self.n) :
            for j in range(i,self.n) :
                if self.adj[i][j] != self.adj[j][i] :
                    return True
        return False

    def is_undirected_and_eulerian(self) :
        if self.is_directed() :
            return False
        degrees=[]
        for i in range(self.n) :
            # ATTENTION ! La méthode get_degree renvoie le double
            # du degré réel dans le cas d'un graphe non-orienté
            # Pour que le théorème d'Euler fonctionne
            # il faut donc diviser par 2 la valeur obtenue !
            degrees.append((self.get_degree(i)//2)%2)
        print(degrees)
        if sum(degrees) == 0 :
            return True
        elif sum(degrees) == 2 :
            return degrees.index(1), self.n-1-degrees[::-1].index(1)
        return False
            
    def delete(self,s, e) :
        self.adj[s][e] = 0


    def __repr__(self) :
        rep =""
        for l in self.adj :
            for e in l :
                rep+=f'{e: >3} '
            rep += "\n"
        return rep
        
        
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
    
class DiGraph(GraphV3) :
    def __init__(self) :
        super().__init__()
        
    def add_edge(self, s, e, p=1) :
        super().add_edge(s,e,p)
        super().add_edge(e,s,p)
        
def DFS(G) :
    def explore_vertice(G, s, explored) :
        explored.append(s)
        for n in G.get_neighbours(s) :
            if n not in explored :
                explore_vertice(G, n, explored)
        
    explored = []
    for s in G.get_vertices() :
        if s not in explored :
            explore_vertice(G,s, explored)
    return explored
            
            
if __name__ == "__main__"  :
    G =GraphV1(5)
    G.add_edge(0,1)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(0,4)
    G.add_edge(2,0)
    G.add_edge(2,3)
    G.add_edge(4,2)
    DFS(G)

        
        
        
