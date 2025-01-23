from PIL import Image
import os


def makeImage(matrix,width,height) :
    img=Image.new('L',(width,height))
    for x in range(width) :
        for y in range(height):
            img.putpixel((x,y),matrix[y][x])
    img.show()
    return None

def makeBiggerImage(matrix, width, height, scale=1) :
    img=Image.new('L',(width*scale,height*scale))
    for x in range(width*scale) :
        for y in range(height*scale):
            img.putpixel((x,y),matrix[y//scale][x//scale])
    img.show()
    return None



if __name__=="__main__" :
    matrix=[
    [255, 0, 0, 255, 255, 0, 0, 255],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [255, 0, 0, 0, 0, 0, 0, 255],
    [255, 255, 0, 0, 0, 0, 255, 255],
    [255, 255, 255, 0, 0, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 255],
    ]   
    
    makeImage(matrix,8,8)
    
