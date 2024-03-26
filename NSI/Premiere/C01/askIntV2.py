
while True :
    nb = input("Entrez un nombre entier entre 1 et 10 : ")
    #  Ici nb est du type 'str'
    # Il faut donc d'abord le convertir en entier, mais si l'utilisateur a saisi une chaine qu'il est impossible
    # de convertir, l'interpréteur lèvera par défaut une erreur et arrêtera le programme.
    # Or nous ne voulons pas d'interruption , nous signifions donc explicitement au programme ce que nous souhaitons
    # qu'il fasse avec le bloc 'try : ...' 'except : ...' `else : ...`
    try :
        nb=int(nb)
        # si l'interpréteur n'arrive pas à exécuter l'instruction ci-dessus, il déclenche une erreur et passe
        # directement au bloc 'except'. Sinon il passe au bloc 'else'.
    except ValueError :
        print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
    else :
        if 1<= nb<= 10 :
            break
        else :
            print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
    

print(f'Le carré de {nb} est {nb**2}')