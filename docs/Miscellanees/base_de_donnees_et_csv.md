# Utilisation de bases de données et de fichiers CSV avec Python


````Python
import csv, sqlite3

conn = sqlite3.connect('BD_danse_justine.db')
cursor = conn.cursor()

#Vidange des tables


def vidange_tables() :
    cursor.execute("select name from sqlite_master where type = 'table';") 
    for table in cursor.fetchall() :
        cursor.execute(f'DELETE FROM {table[0]}')




def insere_dans_table(table, donnees):
    placeholders = ', '.join(['?'] * len(donnees))
    columns = ', '.join(donnees.keys())
    sql = f'INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})'    
    cursor.execute(sql, list(donnees.values()))
    
vidange_tables()  

with open('file.csv', 'r', encoding='latin1') as file:
    reader = csv.DictReader(file)

    #traitements

conn.commit()
conn.close()
    
''''