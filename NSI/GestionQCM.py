import csv

def exportQuestion(num) :
    with open('export_questions_csv.csv', newline='', encoding = 'utf8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        for row in spamreader :
            
            if row['numero de la question'] == str(num) :
                return f"""numero de la question : {row['numero de la question']}
Enoncé : {row[' question']}
Réponse A : {row[' reponseA']}
Réponse B : {row[' reponseB']}
Réponse C : {row[' reponseC']}
Réponse D : {row[' reponseD']}

Bonne réponse : {row[' bonne_reponse']}

"""
                
                
               
    return 

def exportBonneReponses(listequestions) :
    with open('export_questions_csv.csv', newline='', encoding = 'utf8') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=',')
        finalstring ='|'
        for row in spamreader :
            if row['numero de la question'] in  ['18', '19', '21', '22', '25', '26', '27', '1671'] :
                finalstring +=" "+row['numero de la question']+":"+row[' bonne_reponse']+" |"
    return finalstring

def formatReponsesEleves(listerep) :
    returnString ="| "
    for i,c in enumerate(listerep) :
        if c == ';' and listerep[i-1] in '0123456789' :
            returnString +=":"
        elif c == ';' and listerep[i-1] in 'ABCDEFGH' :
            returnString +=" | "
        else :
            returnString +=c
    return returnString