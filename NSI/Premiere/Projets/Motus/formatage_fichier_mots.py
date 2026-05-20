listeMots=[]

with open('liste_francais.txt','r', encoding='utf8') as file :
    for mot in file.readlines() :
        admissible = True
        for c in [' ', ')', '!', "'", '.'] :
            if c in mot :
                admissible = False
        if admissible :
            listeMots.append(mot.replace("\n","").strip())

liste_finale = []

for mot in listeMots :
    motFinal = ""
    for l in mot.lower() :
        if l in['é', 'è', 'ê', 'ë'] :
            motFinal += 'e'
        elif l in ['à', 'â', 'ä'] :
            motFinal += 'a'
        elif l in ['ô', 'ö'] :
            motFinal += 'o'
        elif l in ['î', 'ï'] :
            motFinal += 'i'
        elif l in ['ù', 'û', 'ü'] :
            motFinal += 'u'
        elif l == 'ç' :
            motFinal += 'c'
        elif l =='œ' :
            motFinal += 'oe'
        elif l =='æ':
            motFinal += 'ae'
        elif l not in [chr(97+i) for i in range(26)]+["-"] :
            print(l)
            raise ValueError(f'{l} not in latin alphabet')
        else :                           
            motFinal+=l
    liste_finale.append(motFinal.upper())
        

with open('liste_francais_modifie.txt','w', encoding='utf8') as file :
    for mot in liste_finale :
        file.write(mot+"\n")
        