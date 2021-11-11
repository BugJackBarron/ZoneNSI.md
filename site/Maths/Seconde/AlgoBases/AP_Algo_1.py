nom = input("Quel est votre nom ?")
age = int(input("Quel est votre age ?"))
majeur = age>=18
if majeur :
    majorite = age - 18
    message = f"Bonjour {nom}, vous avez {age} ans et êtes majeur depuis {majorite} ans."
else :
    majorite = 18 - age
    message = f"Bonjour {nom}, vous avez {age} ans et serez majeur dans {majorite} ans."
print(message)
