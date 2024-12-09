# Projet Web : Flask et Bases de Données

Avant ce cours, vous devez reprendre si nécessaire le cours sur Flask situé dans le cours de première [Transmission Client-Serveur](../../../Premiere/C08/Client_Serveur) {:target="_blank"}

## TP : Ajouter des bases de données à Flask

!!! warning "SQLAlchemy"
    Dans la production d'un site plus professionnel, il serait déconseillé d'utiliser la méthode présentée dans cette page. Le module [`SQLAlchemy`](https://www.sqlalchemy.org/){:target="_blank"} permet une liaison plus sécurisée et plus rapide d'une application `Flask` avec une base de donnée relationnelle.

    Cependant, pour des raisons pédagogiques, nous utiliserons le module `SQLite` qui permet d'interagir avec une base de donnée par l'intermédiaire de chaines de caractères.

!!! info "Un exemple de site web avec base de données : Chat"
    On souhaite créer un site web de chat utilisant l'architecture de base de données suivante (la clé primaire est en gras, les clés étrangères précédées d'un symbole `#`) :

    * Utilisateur(**id INT**, pseudo VARCHAR(20), email VARCHAR(30), password VARCHAR(30), id_autorisation INT)
    * Message(**id INT**, #id_auteur INT, date TIMESTAMP, message TEXT)

    Cette application permettra aux utilisateurs d'avoir deux rôles : administrateur (*id_autorisation* valant alors 0) et éditeur (*id_autorisation* valant alors 1).

    L'application contiendra plusieurs pages :

    1. Une page `index.html` qui présentera les 20 derniers messages du chat, et permettant à un utilisateur connecté de déposer un nouveau message.
    2. Une page `connexion.html` permettant à un utilisateur de se connecter.
    3. Une page `home.html` présentant les informations de l'utilisateur, et lui permettant de changer son pseudo, son email et son mot de passe
    4. Une page `administration_utilisateurs.html`, permettant à un administrateur de changer toutes les informations d'un autre utilisateur, voir de le supprimer.
    

### Initialisation de projet `Flask` 

On crée un dossier `Le_Chat`, qui contiendra deux sous-dossiers :

* `templates` : qui contiendra tous les *gabarits* `html` des différentes pages du site ;
* `static` : qui contiendra tous les fichiers «fixes», comme par exemples les feuilles de style `CSS`.

Puis, dans le dossier `Le_Chat`, on crée le fichier minimal `le_chat.py`suivant :

``` python
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'PAS_TOP_COMME_CLE_SECRETE'

@app.route('/')
def index() :
    return "Hello World !"

if __name__ == "__main__" :
    app.run(port=5555, debug=True)
```

!!! warning "Risque de Bug"
    En travaillant avec la version de Thonny du Lycée, il peut arriver que ce code ne fonctionne pas, à cause du paramètre `debug` de la dernière ligne. Dans ce cas, vous pouvez le supprimer. Cependant, ce paramètre est extrêmement pratique puisqu'il permet de faire des modifications *en live* sur le serveur, c'est-à-dire sans avoir besoin d'arrêter le code puis de le relancer.


### Création de la base de données

On crée un script python `create_db.py` contenant les lignes suivantes :

``` python
import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas)
conn = sqlite3.connect('chat.db')
cursor = conn.cursor()


# Création de la table Utilisateur
cursor.execute('''
CREATE TABLE IF NOT EXISTS Utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pseudo VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL CHECK(length(password)>=10),
    id_autorisation INTEGER CHECK (id_autorisation =0 OR id_autorisation=1)
);
''')

# Création de la table Message
cursor.execute('''
CREATE TABLE IF NOT EXISTS Message (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_auteur INTEGER NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message TEXT NOT NULL,
    FOREIGN KEY (id_auteur) REFERENCES Utilisateur(id)
);
''')

# Validation des modifications
conn.commit()

#Insertion d'un utilisateur de base admin
## Bien entendu, dans une véritable création de base de donnée, l'utilisateur admin ne
## devrait pas avoir un mot de passe si faible et en clair

cursor.execute('''INSERT INTO Utilisateur(pseudo, email, password, id_autorisation)
               VALUES ('admin', 'admin@lechat.fr', 'admin1234!', 0)
               ''')

conn.commit()
# Fermeture de la connexion
conn.close()

print("Base de données et tables créées avec succès.")
```
Une fois le code exécuté, une base de donnée est créée, et vous pouvez la regarder avec un logiciel tel `DBBrowser for SQLite`.




### Premières pages

Commençons par créer une première page `index.html`, qui sera sauvegardée dans le dossier `templates` adjacent







