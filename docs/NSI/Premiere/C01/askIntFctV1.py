def ask_user_int() -> int:
    while True :
        nb = input("Entrez un nombre entier entre 1 et 10 : ")
        try :
            nb=int(nb)
        except ValueError :
            print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if 1<= nb<= 10 :
                return nb
            else :
                print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
    