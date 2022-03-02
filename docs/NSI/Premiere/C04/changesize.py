from PIL import Image
from math import sqrt

def getNeighboursMean(image, x, y) :
    w,h = image.size
    red = []
    green = []
    blue = []
    alpha = []
    for vx in [-1, 0, 1] :
        for vy in [-1, 0, 1] :
            if (0<= x+vx < w) and (0<= y + vy < h) :
                px = image.getpixel((x+vx, y+vy))
                red.append(px[0])
                green.append(px[1])
                blue.append(px[2])
                alpha.append(px[3])
                    
    return (sum(red)//len(red), sum(green)//len(green), sum(blue)//len(blue), sum(alpha)//len(alpha))

def divideSizeBy2Interpolate(image) :
    w, h = image.size
    divided = Image.new('RGBA', (w//2, h//2))    
    for x in range(w//2) :
        for y in range(h//2) :
            divided.putpixel((x,y), getNeighboursMean(image, x*2, y*2))
    return divided

def divideSizeBy2Simple(image) :
    w, h = image.size
    divided = Image.new('RGBA', (w//2, h//2))    
    for x in range(w//2) :
        for y in range(h//2) :
            divided.putpixel((x,y), image.getpixel((x*2, y*2)))
    return divided


def doubleSizeSimple(image) :
    w, h = image.size
    double = Image.new('RGBA', (2*w, 2*h))    
    for x in range(w) :
        for y in range(h) :
            double.putpixel((2*x,2*y), image.getpixel((x, y)))
            double.putpixel((2*x+1,2*y), image.getpixel((x, y)))
            double.putpixel((2*x,2*y+1), image.getpixel((x, y)))
            double.putpixel((2*x+1,2*y+1), image.getpixel((x, y)))
    return double

def mean2px(px1, px2) :
    return tuple((c1+c2)//2 for c1, c2 in zip(px1, px2))

def doubleSizeInterpolate(image) :
    w, h = image.size
    double = Image.new('RGBA', (2*w, 2*h))
    for x in range(w) :
        for y in range(h) :
            double.putpixel((2*x,2*y), image.getpixel((x, y)))
            if x!= w-1 and y!= h-1:                
                double.putpixel((2*x+1,2*y), mean2px(image.getpixel((x, y)), image.getpixel((x+1, y))))
                double.putpixel((2*x,2*y+1), mean2px(image.getpixel((x, y)), image.getpixel((x, y+1))))
                double.putpixel((2*x+1,2*y+1),  mean2px(image.getpixel((x, y)), image.getpixel((x+1, y+1))))
            elif x == w-1 and y != h-1:
                
                double.putpixel((2*x+1,2*y), image.getpixel((x, y)))
                double.putpixel((2*x,2*y+1), mean2px(image.getpixel((x, y)), image.getpixel((x, y+1))))
                double.putpixel((2*x+1,2*y+1),  mean2px(image.getpixel((x, y)), image.getpixel((x, y+1))))
            elif x != w-1 and y == h-1:
                
                double.putpixel((2*x+1,2*y), mean2px(image.getpixel((x, y)), image.getpixel((x+1, y))))
                double.putpixel((2*x,2*y+1), image.getpixel((x, y)))
                double.putpixel((2*x+1,2*y+1),  mean2px(image.getpixel((x, y)), image.getpixel((x+1, y))))
            else :
                
                double.putpixel((2*x+1,2*y), image.getpixel((x, y)))
                double.putpixel((2*x,2*y+1), image.getpixel((x, y)))
                double.putpixel((2*x+1,2*y+1), image.getpixel((x, y)))
            
    return double
    
if __name__ == "__main__" :
    image = Image.open('Naruto.png')
    divideSizeBy2Simple(image).save('DemiNarutoSimple.png')
    doubleSizeSimple(image).save('DoubleNarutoSimple.png')
    doubleSizeSimple(divideSizeBy2Simple(image)).save('NarutoTransformeSimple.png')
    
    divideSizeBy2Interpolate(image).save('DemiNarutoInterpolate.png')
    doubleSizeInterpolate(image).save('DoubleInterpolateNaruto.png')
    doubleSizeInterpolate(divideSizeBy2Interpolate(image)).save('NarutoTransformeInterpolate.png')
    