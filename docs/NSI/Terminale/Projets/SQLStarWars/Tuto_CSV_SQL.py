import csv
import sqlite3 as sql
# 
# #Extraction des données CSV

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

## Creation de la table species


def newTable(table_name, attribute_name, column_from, original_table) :
    curs.execute(f"DROP TABLE IF EXISTS {table_name};")    
    curs.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, {attribute_name} TEXT );")

    res = curs.execute(f"SELECT DISTINCT({column_from}) FROM {original_table}")
    liste=set()
    for f in res.fetchall() :
        if f[0] != None :
            lf = f[0].split(",")
            for f in lf :
                liste.add(f.strip())
    liste = list(liste)
    query = f"INSERT INTO {table_name}({attribute_name}) VALUES "
    for f in liste[:-1] :
        query+="('"+f+"'),"
    query+="('"+liste[-1]+"');"

    curs.execute(query)
    connexion.commit()
    
newTable('Specie', 'name', 'species', 'people')


### Modification de la table People pour lier à la table planet

def tableLink(original_table, original_column, new_column,target_table, target_column) :
    curs.execute(f'ALTER TABLE {original_table} ADD {new_column} TYPE INTEGER REFERENCES {target_table}({target_column});')
    query = curs.execute(f"SELECT id, {original_column } FROM {original_table}")
    for p in query.fetchall() :
        if p[1]!= None :
            query2 = curs.execute(f"SELECT id FROM {target_table} WHERE {target_column}='{p[1]}';")
            a = query2.fetchone()
            b = p
            print(a, " - > ",b)
            req = f"UPDATE {original_table} SET {new_column}={a[0]} WHERE id = '{b[0]}';"
            curs.execute(req)
    connexion.commit()
    curs.execute(f'ALTER TABLE {original_table} DROP COLUMN {original_column};')


tableLink('People', 'homeworld', 'planet_id', 'planet', 'name')
tableLink('People', 'species', 'specie_id', 'Specie', 'name')

### Modification de la table People pour lier à la table Movie (Ajout d'une table ISIN)

curs.execute("DROP TABLE IF EXISTS IsInMovie")
curs.execute(f'''CREATE TABLE IsInMovie(
character_id INTEGER REFERENCES People(id),
movie_id INTEGER REFERENCES Movie(id),
PRIMARY KEY(character_id, movie_id));''')
query = curs.execute(f"SELECT id, films FROM people;")
for p in query.fetchall() :
    people_id = p[0]
    people_films  = [p.strip() for p in p[1].split(",")]
    for f in people_films :
        query2 = curs.execute(f"SELECT id FROM Movie WHERE title='{f}';")
        curs.execute(f"INSERT INTO IsInMovie(character_id, movie_id) VALUES ({people_id},{query2.fetchone()[0]});")
connexion.commit()
curs.execute(f'ALTER TABLE people DROP COLUMN films;')


