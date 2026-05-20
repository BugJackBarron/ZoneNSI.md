continuer = True
while continuer :
    nb = input("Entrez un nombre entre 1 et 10 : ")
    if nb != "" :
        est_un_entier = True
        indice_depart = 0
        if nb[0] == "-" :
            indice_depart = 1
        for letter in nb[indice_depart : len(nb)] :
            if letter not in "0123456789" :
                est_un_entier = False
        if est_un_entier :
            nb = int(nb)
            if 1<= nb <= 10 :
                continuer = False
print(f"Vous avez saisi {nb}")
