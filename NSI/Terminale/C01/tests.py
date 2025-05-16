def askIntFrom1To10() :
    while True :
        nb = input("Entrez un entier entre 1 et 10 :")
        if nb.isnumeric() and "." not in (nb) :
            nb = int(nb)
            if 1<=nb and nb<=10 :
                return nb
            else :
                print("L'entier saisi n'est pas entre 1 et 10. Veuillez recommencer")
        else :
            print("Ce n'est pas un entier, veuillez recommencer !")


def askIntFrom1To10G() :
    while True :
        try :
            nb = int(input("Entrez un entier entre 1 et 10 :"))
            if 1<=nb and nb<=10 :
                return nb
            else :
                print("L'entier saisi n'est pas entre 1 et 10. Veuillez recommencer")
        except ValueError :
            print("Ce n'est pas un entier, veuillez recommencer !")

s = '½'