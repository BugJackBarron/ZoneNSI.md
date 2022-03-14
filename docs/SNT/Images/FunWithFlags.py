from PIL import Image


img=Image.new('RGB',(600,450))
for x in range(600) :
    for y in range(150) :
            img.putpixel((x,y),(0,0,255))
            img.putpixel((x,y+150),(255,255,255))
            img.putpixel((x,y+300),(255,0,0))
img.save("drapeauFr.png")
img.show()