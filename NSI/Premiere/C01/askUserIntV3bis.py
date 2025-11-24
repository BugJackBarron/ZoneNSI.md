def is_integer(word : str) -> bool :
    est_un_entier = True
    indice_depart = 0
    if word[0] == "-" :
        indice_depart = 1
    for caractere in word[indice_depart : len(word)] :
        if caractere not in "0123456789" :
            est_un_entier = False
    return est_un_entier


def ask_user_int(borne_min : int, borne_max : int) -> int:
    repeter = True
    while repeter :
        saisie = input(f"Entrez un nombre entre {borne_min} et {borne_max} : ")
        if saisie != "" :
            est_un_entier = is_integer(saisie)
            if est_un_entier :
                nb = int(saisie)
                if borne_min<= nb <= borne_max :
                    repeter = False
    return nb