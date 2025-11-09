from PIL import Image

originale = Image.open("YingYang.pgm")

width, height = originale.size

copie = Image.new("L", originale.size)

for x in range(width) :
    for y in range(height) :
        if originale.getpixel((x,y)) == 255 :
            copie.putpixel((x, y), 0)
        else :
            copie.putpixel((x, y),  255)
            
copie.save("YangYing.bmp")
copie.show()







