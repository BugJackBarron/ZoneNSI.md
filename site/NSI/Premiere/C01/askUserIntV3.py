def ask_user_int(borne_min : int, borne_max: int) -> int :
    while True :
        nb = input(f"Entrez un nombre entier entre {borne_min} et {borne_max} : ")
        try :
            nb=int(nb)
        except ValueError :
            print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if borne_min<= nb<= borne_max :
                break
            else :
                print(f"Votre nombre n'est pas compris entre {borne_min} et {borne_max}. Veuillez recommencer !")
    return nb    