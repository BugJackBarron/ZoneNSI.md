#### Zone des fonctions

def askUserInt() :
    while True :
        nb = input("Entrez un nombre entier entre 1 et 10 : ")
        try :
            nb=int(nb)
        except ValueError :
            print("Vous n'avez pas saisi un entier. Veuillez recommencer !")
        else :
            if 1<= nb<= 10 :
                break
            else :
                print("Votre nombre n'est pas compris entre 1 et 10. Veuillez recommencer !")
    return nb #Renvoie l'objet associé à nb

### Code principal

nb1 = askUserInt()
nb2 = askUserInt()
nb3 = askUserInt()
if (nb1**2 == nb2**2 + nb3**2) or (nb2**2 == nb1**2 + nb3**2) or (nb3**2 == nb2**2 + nb1**2) :
    print("C'est une configuration de Pythagore !")
else :
    print("Ce n'est pas une configuration de Pythagore !")