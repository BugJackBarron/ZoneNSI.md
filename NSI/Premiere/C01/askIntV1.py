while True :
    n = input("Entrez un nombre entier entre 1 et 10 : ")
    if n.isdigit() : # regarde si la chaine ne contient que des chiffres
        n = int(n)
        if n>=1 and n<= 10 :
            print("Le nombre est correct")
            break # L'instruction break sort de la boucle immédiatement
        else :
            print("Votre nombre est entier mais pas entre 1 et 10.")
    else :
        print("Vous n'avez pas saisi un entier")
print(f"Vous avez saisi {n}")
    
    
