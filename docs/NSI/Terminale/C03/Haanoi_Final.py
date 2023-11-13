class ChainonPile :
    def __init__(self, valeur, suivant) :
        self.valeur = valeur
        self.suivant = suivant
        
    def __str__(self) :
        if self.suivant is None :
            return f" {self.valeur}"
        return f"  {self.valeur}  <-  {str(self.suivant)}  "


class Pile :
    """interface de pile"""
    def __init__(self) :
        self.tete = None
        self._taille = 0

    def est_vide(self) :
        return self.tete == None

    def empiler(self, v) :
        self.tete = ChainonPile(v, self.tete)
        self._taille += 1

    def depiler(self) :
        v = self.tete.valeur
        self.tete = self.tete.suivant
        self._taille -= 1
        return v
    
    def vider(self) :
        self.tete = None
        self._taille = 0
        
    def consulter(self):
        if self.est_vide() :
            return float("inf")
        return self.tete.valeur
    
    def __str__(self) :
        if self.est_vide() :
            return ""
        return str(self.tete)


class HanoiGame :
    def __init__(self, n) :
        if type(n) != int :
            raise TypeError("argument n must be int")
        if n<= 0 :
            raise ValueError("n must be strictly positive")
        self.n = n
        self.piles = [Pile(), Pile(), Pile()]
        self.petit_a_bouge = False
        self.ou_est_petit = 0
        for i in range(n, 0, -1) :
            self.piles[0].empiler(i)
            
            
    def affiche(self) :
        print(f"D :{self.piles[0]}")
        print(f"I :{self.piles[1]}")
        print(f"F :{self.piles[2]}")
        
 
    def next_move(self) :
        if self.petit_a_bouge :
            mvt_possibles = [0,1,2]
            mvt_possibles.remove(self.ou_est_petit)          
            
            if  self.piles[mvt_possibles[0]].consulter()< self.piles[mvt_possibles[1]].consulter() :
                self.piles[mvt_possibles[1]].empiler(self.piles[mvt_possibles[0]].depiler())
            elif  self.piles[mvt_possibles[1]].consulter()< self.piles[mvt_possibles[0]].consulter() :
                self.piles[mvt_possibles[0]].empiler(self.piles[mvt_possibles[1]].depiler())
            
            self.petit_a_bouge = False
        else :            
            self.piles[(self.ou_est_petit-1)%3].empiler(self.piles[self.ou_est_petit].depiler())
            self.ou_est_petit = (self.ou_est_petit-1)%3
            self.petit_a_bouge = True
            
    def resout_iteratif(self, etapes= True) :
        print("Départ")
        self.affiche()
        i=0
        while not(self.piles[0].est_vide()) or not(self.piles[1].est_vide()) :
            i+=1
            if etapes : print(f"Etape {i}")
            self.next_move()
            if etapes :
                self.affiche()
                print("")
        if not(etapes) :
            print("Nombre total d'étapes : {i}")

                        
if __name__ == "__main__" :
    g = HanoiGame(3)
    g.resout_iteratif()