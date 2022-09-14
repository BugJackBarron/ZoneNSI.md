def ask_user_int(borne_min,borne_max, prenom='Inconnu') :
    if not(isinstance(borne_min,int)) or not(isinstance(borne_max,int)) :
        raise ValueError("One or both of the arguments are not of type int")
    if borne_min>borne_max :
        raise ValueError("First argument must be lesser or equal to second argument")
    while True :
        nb = input(f"{prenom}, entrez un nombre entier entre {borne_min} et {borne_max} : ")
        try :
            nb=int(nb)
        except ValueError :
            print(f"{Inconnu}, vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if borne_min<= nb<= borne_max :
                break
            else :
                print(f"{Inconnu}, votre nombre n'est pas compris entre {borne_min} et {borne_max}. Veuillez recommencer !")
    return nb    