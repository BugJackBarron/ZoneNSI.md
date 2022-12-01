import csv
import sqlite3 as sql

#Extraction des données CSV

def extractData(filename) :
    with open(filename, "r", encoding="utf8") as csvfile :
        dico = csv.DictReader(csvfile, delimiter=',')
        realDico = []
        for line in dico :
            realDico.append(line)
    return realDico

#SQLITE 3

# Creation de la base de donnée

connexion = sql.connect('Custom_SW_DB.db')

curs = connexion.cursor()
curs.execute("DROP TABLE IF EXISTS People")
curs.execute(
    """CREATE TABLE People(id INTEGER PRIMARY KEY,
name TEXT,
height INTEGER,
mass FLOAT,
hair_color TEXT,
skin_color TEXT,
eye_color TEXT,
birth_year TEXT,
sex TEXT,
gender TEXT,
homeworld TEXT,
species TEXT,
films TEXT,
vehicles TEXT,
starships TEXT)""")

dico = extractData("StarWars.csv")

keys = tuple(dico[0].keys())

for line in dico :
    
    query = f"INSERT INTO People {keys} VALUES("
    for k in keys :
        if (line[k] == "NA" or line[k]=="") and k !='starships':
            query += "NULL, "
        elif (line[k] == "NA" or line[k]=="") and k =='starships':
            query +="NULL)"
        elif k == "height" :
            query+=line[k]+", "
        elif k == "mass" :
            query+=str(float(line[k]))+", "
        elif k=='starships' :
            query += "'"+line[k]+"')"
        else :
            query += "'"+line[k]+"', "
    
    print(query)

    curs.execute(query)

# NE pas oublier le commit() (tout ou rien)

connexion.commit()

## Creation de la table Planet
curs.execute("DROP TABLE IF EXISTS Planet;")    
curs.execute("CREATE TABLE Planet (id INTEGER PRIMARY KEY, name TEXT);")

# Recherche des éléments à intégrer

res = curs.execute("SELECT DISTINCT homeworld FROM People;")

res = tuple(p[0] for p in res.fetchall())


for p in res :
    # Attention aux guillemets
    req = f"INSERT INTO Planet(name) VALUES ('{p}');"
    print(req)
    curs.execute(req)
    connexion.commit()

query = f"INSERT INTO Planet(name) VALUES "

    
# print(req)
# curs.execute(req)


## Creation de la table Movie
    
curs.execute("DROP TABLE IF EXISTS Movie;")    
curs.execute("CREATE TABLE Movie (id INTEGER PRIMARY KEY, title TEXT);")

res = curs.execute("SELECT DISTINCT(films) FROM People")

listefilms=set()

for f in res.fetchall() :
    lf = f[0].split(",")
    for f in lf :
        listefilms.add(f.strip())
listefilms = list(listefilms)
query = "INSERT INTO Movie(title) VALUES "
for f in listefilms[:-1] :
    query+="('"+f+"'),"
query+="('"+listefilms[-1]+"');"

curs.execute(query)
connexion.commit()

## CREATION de la table Spaceships

curs.execute("DROP TABLE IF EXISTS Starship;")    
curs.execute("CREATE TABLE Starship (id INTEGER PRIMARY KEY, name TEXT);")

res = curs.execute("SELECT DISTINCT(Starships) FROM People")

listestarship=set()

for f in res.fetchall() :
    if f[0] != None :
        lf = f[0].split(",")
        for f in lf :
            listestarship.add(f.strip())
listestarship = list(listestarship)
query = "INSERT INTO Starship(name) VALUES "
for f in listestarship[:-1] :
    query+="('"+f+"'),"
query+="('"+listestarship[-1]+"');"

curs.execute(query)
connexion.commit()


### Modification de la table People pour lier aux autres tables

def tableLink(original_table, original_column, target_table, target_column) :
    curs.execute('ALTER TABLE People ADD planet_id TYPE INTEGER REFERENCES Planet(id);')

    query = curs.execute("SELECT id, name, homeworld  FROM People")

    for p in query.fetchall() :
        query2 = curs.execute(f"SELECT id FROM Planet wHERE name='{p[2]}';")
        curs.execute(f"UPDATE People SET planet_id={query.fetchone()[0]} WHERE id = '{p[0]}';")
        

    connexion.commit()

    curs.execute('ALTER TABLE People DROP COLUMN homeworld;')
