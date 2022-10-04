listeMots=[]

with open('liste_francais.txt','r', encoding='utf8') as file :
    for mot in file.readlines() :
        admissible = True
        for c in [' ', ')', '!', "'", '.'] :
            if c in mot :
                admissible = False
        if admissible :
            listeMots.append(mot.replace("\n","").strip())

with open('liste_francais_modifie.txt','w', encoding='utf8') as file :
    for mot in listeMots :
        file.write(mot+"\n")
        