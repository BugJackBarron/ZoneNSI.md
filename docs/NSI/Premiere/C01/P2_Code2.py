nb = int(input("Entrez un nombre entre 1 et 100 :"))
if nb<1 :
    print("Votre nombre est trop petit")
elif nb>100 :
    print("Votre nombre est trop grand")
elif nb < 50 :
    nb = nb + 50
    print(f"Le nombre final est {nb}")
else :
    nb = nb - 50
    print(f"Le nombre final est {nb}")
print("FIN")