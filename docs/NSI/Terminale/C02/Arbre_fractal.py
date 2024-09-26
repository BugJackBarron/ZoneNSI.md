from turtle import *

angle = 30
color('#3f1905')

def arbre(n,longueur):
    if n==0:
        color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle) # tourne vers la gauche de angle degrés
        arbre(n-1,longueur*2/3)
        right(2*angle) # tourne vers la droite de angle degrés
        arbre(n-1,longueur*2/3)
        left(angle) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule

hideturtle() # cache la tortue
speed(0)
up() # lève le stylo
right(90) # tourne de 90 degrés vers la droite 
forward(300) # avance de 300 pixels
left(180) # fait un demi-tour
down() # pose le stylo
arbre(9,500) # exécute la macro
showturtle() # affiche la tortue
mainloop()