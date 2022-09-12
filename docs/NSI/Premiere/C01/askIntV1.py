while True : # Il s'agit d'une boucle infinie, la condition étant toujours vraie
    nb = input("Entrez un nombre entre 1 et 10 : ")
    nb=int(nb)
    if 1<=nb<=10 :
        # L'instruction 'break' arrête immédiatement la boucle  et sort de la boucle while
        break
    else :
        print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
        
#Une fois sorti de la boucle, on peut donc utiliser 'nb' en étant certain qu'il s'agit d'un entier entre 1 et 10.
print(f'Le carré de {nb} est {nb**2}')