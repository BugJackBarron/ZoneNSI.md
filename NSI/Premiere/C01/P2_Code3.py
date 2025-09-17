nb= int(input("Donnez un nombre entier positif:"))
puissance = 0
while nb//2 >=1  :
    puissance = puissance +1
    nb=nb//2
print(f"Votre nombre est supérieur ou égal à 2 puissance {puissance} et\
    inférieur à 2 puissance {puissance+1}")
# Notez l'utilisation de \ pour éviter d'avoir une ligne trop longue.