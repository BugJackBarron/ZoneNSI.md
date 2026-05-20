saisie = input("Entrez un nombre entre 1 et 10 :")
while not(saisie in [ "1", "2", "3","4", "5", "6", "7", "8", "9", "10" ])     :
    saisie = input("Entrez un nombre entre 1 et 10 :")
nb = int(saisie)
print(f"Vous avez saisi {nb}")