#### Zone des fonctions

def ask_user_int() -> int:
    repeter = True
    while repeter :
        saisie = input("Entrez un nombre entre 1 et 10 : ")
        if saisie != "" :
            est_un_entier = True
            indice_depart = 0
            if saisie[0] == "-" :
                indice_depart = 1
            for caractere in saisie[indice_depart : len(saisie)] :
                if caractere not in "0123456789" :
                    est_un_entier = False
            if est_un_entier :
                nb = int(saisie)
                if 1<= nb <= 10 :
                    repeter = False
    return nb
### Code principal

nb1 = ask_user_int()
nb2 = ask_user_int()
nb3 = ask_user_int()
if (nb1**2 == nb2**2 + nb3**2) or (nb2**2 == nb1**2 + nb3**2) or (nb3**2 == nb2**2 + nb1**2) :
    print("C'est une configuration de Pythagore !")
else :
    print("Ce n'est pas une configuration de Pythagore !")