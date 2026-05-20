from PIL import Image
from math import sqrt

def distance(p1,p2) :
    return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def makeCircle(a) :
    width = 3*a
    height = int((2+sqrt(3)/2)*a)
    img = Image.new("RGB", (width, height))
    for x in range(width) :
        for y in range(height) :
            R = 255*(distance((x,y), (2*a, (1+sqrt(3)/2)*a))<a)
            G = 255*(distance((x,y), (3*a/2, a))<a)
            B = 255*(distance((x,y), (a, (1+sqrt(3)/2)*a))<a)
            img.putpixel((x,y),(R,G,B))
    return img

def Filter(image, filtre) :
    r, g, b, a = filtre
    width, height = image.size
    retour = Image.new ("RGBA", image.size)
    for x in range(width) :
        for y in range(height) :
            R, G, B, A = image.getpixel((x,y))
            retour.putpixel((x,y), (r*R,g*G,b*B,a*A))
    return retour
                        
            
def negatif() :
    image = Image.open("Naruto.png")
    width, height = image.size
    retour = Image.new ("RGBA", image.size)
    for x in range(width) :
        for y in range(height) :
            R, G, B, A = image.getpixel((x,y))
            retour.putpixel((x,y), (255-R,255-G,255-B,A))
    retour.save('NarutoNegatif.png')
    retour.show()
if __name__ == "__main__" :
    image = Image.open('Naruto.png')
    width, height = image.size
    filters = [Filter(image, (True, False, False, True)),
               Filter(image, (False, True, False, True)),
               Filter(image, (False, False, True, True)),
               Filter(image, (True,  True, True, True)),
               Filter(image, (True, True, False, True)),
               Filter(image, (True, False, True, True)),
               Filter(image, (False,  True, True, True)),
               Filter(image, (False,  False, False, True))              
               ]
    warhol = Image.new('RGBA', (width*len(filters), height))
    w, h = warhol.size
    for x in range(w) :
        for y in range(h) :
            warhol.putpixel((x,y), filters[x//width].getpixel((x%width, y)))
    warhol.save('Multiclonage.png')
        
    
    