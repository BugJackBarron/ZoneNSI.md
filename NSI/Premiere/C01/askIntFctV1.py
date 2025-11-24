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