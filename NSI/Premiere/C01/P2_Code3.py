nb= int(input("Donnez un nombre entier positif:"))
puissance = 0
while nb//2 >=1  :
    puissance = puissance +1
    nb=nb//2
print("Votre nombre est supérieur ou égal à 2 puissance {p} et inférieur à 2 puissance {q}".format(
    p=puissance,q=puissance+1))#A noter qu'ici le texte étant trop long, on a pu "sauter" à la ligne
                            #le saut de ligne étant compris entre les parenthèses de la méthode format