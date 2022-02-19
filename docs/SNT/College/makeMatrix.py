from PIL import Image
from copy import deepcopy

def affiche(M) :
    print("[")
    for line in M :
        print(line,end="")
        print(",")
    print("]")

img = Image.open('Mario.png').convert('LA')
width, height = img.size
newimg = deepcopy(img)
matrix = [[255]*width for _ in range(height) ]
pixels = newimg.load()
for y in range(height) :
    for x in range(width) :
        col, alpha = img.getpixel((x,y))
        if alpha == 255 :
            matrix[y][x] = col
            
 
affiche(matrix)


