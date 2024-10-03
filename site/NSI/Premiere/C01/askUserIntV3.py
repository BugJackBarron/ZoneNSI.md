def ask_user_int(borne_min : int, borne_max : int) -> int:
    repeter = True
    while repeter :
        saisie = input(f"Entrez un nombre entre {borne_min} et {borne_max} : ")
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
                if borne_min<= nb <= borne_max :
                    repeter = False
    return nb