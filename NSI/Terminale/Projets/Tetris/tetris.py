import pyxel

class Piece :
    def __init__(self, sx, sy, w, h, image = 0) :
        self.x = 0
        self.y = 0
        self.sx = sx
        self.sy = sy
        self.w = w
        self.h = h
        self.i = image
        
    def fall(self) :
        if self.y<148 :
            self.y += 8
        else :
            self.y = 20
        
    

class Tetris :
    def __init__(self) :
        pyxel.init(160, 180, fps=60 )
        pyxel.load("TETRIS.pyxres")
        self.piece = Piece(32, 0, 3*8,2*8)
        self.piece.x = 80
        self.piece.y = 20
        self.speed = 1
        pyxel.run(self.update, self.draw)
        
        
    def update(self) :
        if pyxel.frame_count%(60-self.speed) == 0 :
            self.piece.fall()
            self.speed *=2
        
        
        
    def draw(self) :
        pyxel.cls(0)
        pyxel.bltm(80,20, 0, 0, 0, 10*8, 21*8, 0)
        pyxel.blt(self.piece.x, self.piece.y, self.piece.i, self.piece.sx, self.piece.sy, self.piece.w, self.piece.h,0)

        
if __name__ == "__main__" :
    Tetris()