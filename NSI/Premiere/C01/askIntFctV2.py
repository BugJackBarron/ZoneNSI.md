#### Zone des fonctions

def ask_user_int() -> int :
    while True :
        nb = input("Entrez un nombre entier entre 1 et 10 : ")
        try :
            nb=int(nb)
        except ValueError :
            print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if 1<= nb<= 10 :
                return nb #Renvoie l'objet associé à nb
            else :
                print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")

### Code principal

nb1 = ask_user_int()
nb2 = ask_user_int()
nb3 = ask_user_int()
if (nb1**2 == nb2**2 + nb3**2) or (nb2**2 == nb1**2 + nb3**2) or (nb3**2 == nb2**2 + nb1**2) :
    print("C'est une configuration de Pythagore !")
else :
    print("Ce n'est pas une configuration de Pythagore !")