import timeit


animaux = ['Vache', 'Chien', 'Chat', 'Poule', 'Ane', 'Cochon', 'Dindon']
cri = ['Meuh', 'Wouf', 'Miaou', 'Cot-cot', 'Hi-Han', 'Gruik', 'Leon']


def affiche_cri(animal) :   
    for i in range(len(animaux)) :
        if animaux[i] == animal :
            return cri[i]
    return f"Je ne connais pas le cri de {animal}"


def make_big_lists() :
    import csv
    with open("Long_Dico.csv","r",encoding = "utf8") as file :
        dicReader = csv.DictReader(file, delimiter=';')
        etablissements =[]
        GPS = []
        for line in dicReader :
            etablissements.append(line['Nom'])
            GPS.append(line['GPS'])
    return etablissements, GPS

etablissements, GPS = make_big_lists()


def affiche_GPS(etab) :   
    for i in range(len(etablissements)) :
        if etablissements[i] == etab :
            return GPS[i]
    return None


cris = {"Vache" : "Meuh",
           "Chien" : "Wouf",
           "Chat" : "Miaou",
           "Poule" : "Cot-cot",
           "Ane" : "Hi-Han",
           "Cochon" : "Gruik",
           "Dindon" : "Leon"
           }

def affiche_cri_2(animal) :
    if animal in cris :
        return cris[animal]
    return f"Je ne connais pas le cri de {animal}"


def make_big_dict() :
    import csv
    with open("Long_Dico.csv","r",encoding = "utf8") as file :
        dicReader = csv.DictReader(file, delimiter=';')
        etablissements=dict()
        for line in dicReader :
            etablissements[line['Nom']] = line['GPS']
    return etablissements

dic_etablissements = make_big_dict()
