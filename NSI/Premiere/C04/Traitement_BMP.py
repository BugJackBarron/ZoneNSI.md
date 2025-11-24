from PIL import Image 

def negatifGris(originale) :
    width, height = originale.size
    copie = Image.new(originale.mode, originale.size)   
    for x in range(width) :                         
        for y in range(height) :                    
           copie.putpixel((x,y), 255-originale.getpixel((x,y)))
    return copie

def eclaircir(originale, t=20) :
    width, height = originale.size
    copie = Image.new(originale.mode, originale.size)   
    for x in range(width) :                         
        for y in range(height) :                    
           copie.putpixel((x,y),t+originale.getpixel((x,y)))
    return copie

def assombrir(originale, t=20) :
    return eclaircir(originale, -t)


    