# Projet Web : Flask et Bases de Données

Avant ce cours, vous devez reprendre si nécessaire le cours sur Flask situé dans le cours de première [Transmission Client-Serveur](../../../Premiere/C08/Client_Serveur){:target="_blank"}

## TP : Ajouter des bases de données à Flask

!!! warning "SQLAlchemy"
    Dans la production d'un site plus professionnel, il serait déconseillé d'utiliser la méthode présentée dans cette page. Le module [`SQLAlchemy`](https://www.sqlalchemy.org/){:target="_blank"} permet une liaison plus sécurisée et plus rapide d'une application `Flask` avec une base de donnée relationnelle.

    Cependant, pour des raisons pédagogiques, nous utiliserons le module `SQLite` qui permet d'interagir avec une base de donnée par l'intermédiaire de chaines de caractères.

!!! info "Un exemple de site web avec base de données : Chat"
    On souhaite créer un site web de chat utilisant l'architecture de base de données suivante (la clé primaire est en gras, les clés étrangères précédées d'un symbole `#`) :

    * Utilisateur(**id INT**, pseudo VARCHAR(20), email VARCHAR(30), password VARCHAR(30), id_autorisation INT)
    * Message(**id INT**, #id_auteur INT, date TIMESTAMP, message TEXT)

    Cette application permettra aux utilisateur·trice·s d'avoir deux rôles : administration (*id_autorisation* valant alors 0) et édition (*id_autorisation* valant alors 1).

    L'application contiendra plusieurs pages :

    1. Une page `index.html` qui présentera les 10 derniers messages du chat, et permettant à un·e utilisateur·trice connecté de déposer un nouveau message.
    2. Une page `connexion.html` permettant à un·e utilisateur·trice de se connecter.
    3. Une page `inscription.html` permettant à un·e nouvel·le utilisateur·trice de s'inscrire.
    4. Une page `moderation.html`, permettant à un·e administrateur·trice de supprimer un message.
    

### Initialisation de projet `Flask` 

On crée un dossier `Le_Chat`, qui contiendra deux sous-dossiers :

* `templates` : qui contiendra tous les *gabarits* `html` des différentes pages du site ;
* `static` : qui contiendra tous les fichiers «fixes», comme par exemples les feuilles de style `CSS`.

Puis, dans le dossier `Le_Chat`, on crée le fichier minimal `le_chat.py`suivant :

``` python
from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

app.secret_key = 'PAS_TOP_COMME_CLE_SECRETE'

@app.route('/')
def index() :
    return "Hello World !"

if __name__ == "__main__" :
    app.run(port=5555, debug=True)
```

!!! info "Les imports de Flask"
    Nous avons déjà croisé les imports `Flask`, `render_template` et `request`. Les quatre autres imports seront détaillés par la suite, mais en voici une description sommaire

    * `session` : permet de créer une variable de session (équivalente à un cookie) qui autorisera à garder certaines informations de l'utilisateur de pages en pages.
    * `redirect` : permet de rediriger une connexion vers une URL.
    * `url_for` : créé une URL à partir d'une route (le nom donné dans le décorateur `@app.route()`). Très pratique pour éviter d'avoir à taper à la main des URL complexes, et d'avoir à les changer quand le site web est déployé en production.
    * `flash`: permet de faire apparaitre des messages spécifiques dans une zone dédiée.


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

#### Pages d'accueil et de connexion

!!! question "Héritage de template"
    Nous souhaiterions forcément avoir une certaine cohérence entre les différentes pages de notre site, par exemple avoir le même bandeau d'entête, le même pied de page, la même feuille de style CSS.
    Une des possibilités pourrait être de faire de simples copié-collé de page html en page html. Mais toute modification souhaitée devra être alors répétée sur chaque page, ce qi peut devenir très rapidement lassant, voire conduire à des erreurs plus importantes.

    Pour pallier à ce problème, Flask, et la syntaxe `JINJA2` utilisent le concept d'{==**héritage de template**==} : on va créer une pseudo page `JINJA/html` qui contiendra les parties communes à toutes les pages du site, mais aussi une ou des zones nommées spécifiques qui pourront être réécrites par d'autres pages html.

Commençons par créer une première page `base.html`, qui sera sauvegardée dans le dossier `templates`.

``` HTML
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>{% raw %}{% block title%}Chat App{% endblock %}{% endraw %}</title>
</head>
<body>
    
    <header>
        
        <h1>Bienvenu sur Le Chat !</h1>
        <a href="">S'enregistrer</a>
        <a href="{{ "{{" }} url_for('connexion') {{ "}}" }}">Se connecter</a>
    </header>

    {% raw %}
    {% block contenu %}
    {% endblock %}
    {% endraw %}
    <footer>
        Lycée A.P. 2024-2025
    </footer>
</body>
</html>

```

Cette page contient deux blocs nommés :

* `title` : dans la page de base, le titre est «Le Chat».

* `contenu` : dans la page de base, le contenu est vide.

Nous pouvons ensuite créer deux pages `html`, une pour l'accueil (`ìndex.html`) et une pour la connexion (`connexion.html`). Ces deux pages héritent du template `base.html`, et par conséquent ne nécessitent pas de recopier les lignes déjà présentes dans `base.html` :

``` HTML title="index.html"

{{ "{" }}% extends "base.html" %{{ "}" }}

{{ "{" }}% block contenu % {{ "}" }}

<h2>Bienvenu sur le site du Chat !</h2>
<p>Bientôt les messages s'afficheront ici !</p>

{{ "{" }}% endblock %{{ "}" }}

```

``` HTML title="connexion.html"

{{ "{" }}% extends "base.html" %{{ "}" }}

{{ "{" }}% block titre %{{ "}" }}
Login
{{ "{" }}% endblock %{{ "}" }}

{{ "{" }}% block contenu %{{ "}" }}

<h2>Connexion</h2>
<form action="{{ "{{" }} url_for('check_login') {{ "}}" }}" method="post">
    <label for="pseudo">Pseudo:</label><br>
    <input type="text" id="pseudo" name="pseudo" required><br><br>
    <label for="password">Mot de passe:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <input type="submit" value="Se connecter">
</form>
{{ "{" }}% endblock %{{ "}" }}

```

Il faut maintenant relier ensemble tous les éléments :

* dans le code python, nous allons modifier la fonction `ìndex` afin qu'elle utilise le gabarit `index.html`, grâce à la fonction `render_template` : 

    ``` python
    def index() :
        return render_template("index.html")
    ```

* vous avez peut-être constaté dans le code du gabarit `base.html` la présence de la ligne suivante :

    ``` HTML
        <a href="{{ "{{" }} url_for('connexion') {{ "}}" }}">Se connecter</a>
    ```
    Elle signifie que l'hyperlien créé doit faire appel à une route `connexion`. Il faut donc créer cette route et la fonction python qui va avec :

    ``` python
    @app.route('connexion')
    def connexion() :
        return render_template('connexion.html')
    ```
    Désormais un clic sur l'hyperlien permet d'atteindre la page dont l'url est `127.0.0.1:5555/connexion`.


#### Connexion à la base de données

Pour l'instant, remplir le formulaire de connexion ne mène qu'à une chose : un plantage du site, qui cherche sans succès une route `check_login`.

Il faut donc créer cette route, qui a pour objectif de vérifier si l'utilisateur·trice est dans la base de données, et dans ce cas lui donner accès au site dans son ensemble, et sinon de le/la renvoyer vers la page de connexion. Le formulaire utilisant la méthode `POST`, on va récupérer les informations des champs `pseudo` et `password`, puis vérifier qu'ils correspondent bien à une entrée de la base de données.


``` python
@app.route('check_login', methods=['GET', 'POST'])
def check_login() :
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']

        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT pseudo, id_autorisation FROM Utilisateur WHERE pseudo = ? AND password = ?", (pseudo, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            flash('Connexion réussie!', 'success')
            
            return redirect(url_for('index'))
        else:
            flash('Pseudo ou mot de passe incorrect', 'danger')

    return render_template('connexion.html')
```

Si cela fonctionne correctement, il y a plusieurs points qui restent insatisfaisants :

* les messages ne s'affichent pas ;
* mais surtout **il n'y a aucune trace dans le code permettant de savoir si l'utilisateur·trice s'est bien connecté·e**, puisque les traces de connexions ne sont que des variables locales à la fonction `check_login`.


#### Affichage des messages créés avec `flash`

Il faut rajouter au gabarit `base.html` une partie de code `Jinja2`, par exemple en dessous du `header` :

``` HTML
    {{ "{" }}% with messages = get_flashed_messages() %{{"}"}}
        {{"{"}}% if messages %{{"}"}}
            <ul>
            {{"{"}}% for message in messages %{{"}"}}
                <li>{{"{{"}} message {{"}}"}}</li>
            {{"{"}}% endfor %{{"}"}}
            </ul>
        {{"{"}}% endif %{{"}"}}
    {{"{"}}% endwith %{{"}"}}
```
On voit ici certains éléments de la syntaxe `Jinja 2` :

* la structure conditionnelle est définie par un bloc {{"{"}}% if ... %{{"}"}}. Vous trouverez la syntaxe exacte [ici](https://jinja.palletsprojects.com/en/stable/templates/#if){:target="_blank"}.
* le parcours par éléments est possible, avec une boucle `for`. Vous trouverez la syntaxe exacte [ici](https://jinja.palletsprojects.com/en/stable/templates/#for){:target="_blank"}.
* Chaque bloc doit se terminer par une fin de bloc correspondante `{{"{"}}% endif %{{"}"}}` ou `{{"{"}}% endfor %{{"}"}}` par exemple.
* Une variable, ici `message`, peut être utilisée dans le code HTML en utilisant la syntaxe `{{"{{"}} message {{"}}"}}`.

Désormais, quand un·e utilisateur·trice essaye de se connecter, qu'iel réussisse ou qu'iel échoue, iel aura un message spécifique (qui pourra être formaté par du CSS plus tard). Pour en connaitre plus sur les messages, voir [cette page](https://flask.palletsprojects.com/en/stable/patterns/flashing/){:target="_blank"}.

#### Utiliser les variables de sessions

!!! info "Protocole HTTP et cookies"
    HTTP est sans mémoire (*stateless*) : il n'y a aucun lien entre deux requêtes successives. Cela pose évidemment problème dès que des données doivent être conservées de pages en pages, comme par exemple un panier sur un site de e-commerce. Il existe donc deux possibilités pour résoudre cette difficulté :

    * stocker les informations côté client, par l'intermédiaire de {==**cookies**==}, c'est-à-dire de petits fichiers (4 ko), non-cryptés, stockés dans le navigateur web, et qui sont transmis et mis à jour à chaque requête.
    * stocker les informations côté serveur, dans une base de données.

    Les deux solutions ont leurs avantages et inconvénients, par exemple des données sensibles ne doivent pas être stockées dans des cookies, mais des données communes seront plus rapidement utilisables sans requêtes sur une base de données.

`Flask` utilise le principe des cookies, pratiquement en utilisant un dictionnaire spécifique nommé `session`. Il est possible de stocker à peu près n'importe quel objet Python dans le dictionnaire.

Pour mémoriser, l'utilisateur connecté, nous allons stocker dans le dictionnaire `session` deux paires clés/valeurs contenant le pseudo et le numéro
d'autorisation (pour repérer qui dispose des droits d'administration).

Ainsi nous modifions la fonction `check_login`, plus particulièrement le moment où l'identification a été reconnue. La variable `user` contient donc à l'indice 0 le pseudo, et à l'indice 1 le numéro d'autorisation :

``` python 
if user:
    flash('Connexion réussie!', 'success')
    session['pseudo'] = user[0]
    session['autorisation'] = user[1]
    return redirect(url_for('index'))
```
Désormais, il est possible d'utiliser les variables `session['pseudo']` et `session['autorisation']`dans tout le code, en prenant garde à ce qu'elles existent réellement.

Par exemple on peut modifier le code du gabarit `base.html` en changeant le `header` ainsi :

``` HTML
<header>
    <h1>Bienvenu sur Le Chat !</h1>
    {{"{"}}% if session['pseudo'] %{{"}"}}
        <span> Bonjour {{"{{"}} session['pseudo'] {{"}}"}} !</span>    
        <a href="">Se déconnecter</a>    
    {{"{"}}% else %{{"}"}}
        <a href="">S'enregistrer</a>
        <a href="{{"{{"}} url_for('connexion') {{"}}"}}">Se connecter</a>
    {{"{"}}% endif %{{"}"}}
</header>
```

Un·e utilisateur·trice connecté·e verra donc son pseudo s'afficher.

!!! question "A faire"
    Vous devez créer une route `deconnexion` qui permet à un·e utilisateur·trice connecté·e de se déconnecter, en utilisant simplement la ligne suivante : `session.pop('pseudo', default=None)`. N'oubliez pas de supprimer aussi les autorisations ! Une déconnexion réussie devra amener à la page d'index.

### Rendre l'application fonctionnelle

Avec tout ce que nous avons appris, il est temps de rentrer dans le vif du sujet : il faut permettre à un utilisateur de s'inscrire, puis lui permettre de poster des messages sur le chat.

#### Inscription des utilisateurs

On crée une route `inscription`, et la fonction qui lui est associée. Celle ci renverra le gabarit `inscription.html` à condition qu'il n'existe pas d'utilisateur·trice connecté·e·s.

```python 
@app.route('/inscription')
def inscription() :
    if 'pseudo' in session :
        flash("Vous êtes déjà inscrit·e !")
        return redirect(url_for('index'))
    return render_template('inscription.html')

```

``` HTML title="inscription.html"
{{"{"}}% extends "base.html" %{{"}"}}

{{"{"}}% block titre %{{"}"}}
Inscription
{{"{"}}% endblock %{{"}"}}

{{"{"}}% block contenu %{{"}"}}

<h2>Inscription</h2>
<form action="{{"{{"}} url_for('check_signin') {{"}}"}}" method="post">
    <label for="pseudo">Pseudo:</label><br>
    <input type="text" id="pseudo" name="pseudo" required><br><br>
    <label for="password">Mot de passe:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <label for="password">Vérification :</label><br>
    <input type="password" id="password2" name="password2" required><br><br>
    <label for="email">Email:</label><br>
    <input type="text" id="email" name="email" required><br><br>
    <input type="submit" value="Se connecter">
</form>
{{"{"}}% endblock %{{"}"}}

``` 
Il faut maintenant crée une route `check_signin`, qui effectuera les vérifications nécessaires :

* le pseudo est-il déjà utilisé ?
* les deux mots de passe sont-ils identiques ?
* le mot de passe est-il de la bonne taille ?

Par défaut, les nouveaux inscrits n'ont pas les droits d'administration.

``` python
@app.route("/check_signin", methods=['POST', 'GET'])
def check_signin():
    if 'pseudo' in session :
        flash("Vous êtes déjà inscrit·e !")
        return redirect(url_for('index'))
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']
        password2 = request.form['password2']
        email = request.form['email']
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT pseudo FROM Utilisateur WHERE pseudo = ?", (pseudo,))
        user = cursor.fetchone()
        conn.close()
        if user :
            flash("Le pseudo est déjà utilisé")
            return render_template('inscription.html')
        if password != password2 :
            flash("Les mots de passe ne correspondent pas")
            return render_template('inscription.html')
        if len(password)<10 :
            flash("Le mot de passe doit être au moins de longueur 10 !")
            return render_template('inscription.html')            
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Utilisateur(pseudo, password, email, id_autorisation) VALUES (?, ?, ?, 1) ;""", (pseudo, password,email,))
        conn.commit()
        conn.close()
        flash("Vous êtes inscrit·e. Veuillez vous connecter !")
        return redirect(url_for("connexion"))
        
        
    return render_template('inscription.html')
```
!!! warning "Valider la requête"
    N'oubliez pas de commit après avoir effectué votre insertion ! Sinon votre requête aura été testée, mais pas effectuée en réalité.

!!! danger "Question de sécurité"
    Attention, la méthode présentée ci-dessus n'est absolument pas valide pour un site en production ! En effet, outre les mots de passe en clair, il faut ABSOLUMENT vérifier et nettoyer les saisies de l'utilisateur pour éviter des failles de sécurité permettant des [injections SQL](https://fr.wikipedia.org/wiki/Injection_SQL){:target="_blank"}.

#### Ajouter les messages

Il reste maintenant l'essentiel : permettre la lecture et l'ajout de messages par les personnes connectées. Pour cela, on va modifier le gabarit `index.html` ainsi que la route racine `\`, puis créer une route `add_post`.

D'abord la modification du bloc `contenu` du gabarit `index.html`, pour qu'il affiche les derniers messages, ainsi qu'un champ de formulaire si un·e utilisateur·trice est connecté·e :

``` HTML
{{"{%"}} block contenu {{"%}"}}
<h2>Voici les derniers messages :</h2>
{{"{%"}} if session['pseudo'] {{"%}"}}
<form action="{{"{{"}} url_for('add_post') {{"}}"}}" method="post">
    <label for="message">Votre message :</label><br>
    <input type="text" id="message" name="message" required><br><br>    
    <input type="submit" value="envoyer">
</form>
{{"{%"}} endif {{"%}"}}
{{"{%"}} if messages {{"%}"}}
<ul>
    {{"{%"}} for message in messages {{"%}"}}
    <li>{{"{{"}} message[0] {{"}}"}} ({{"{{"}} message[1] {{"}}"}}) : {{"{{"}} message[2] {{"}}"}}</li>
    {{"{%"}} endfor {{"%}"}}
</ul>
{{"{%"}} endif {{"%}"}}
{{"{%"}} endblock {{"%}"}}
```
Puis la modification de la route racine, qui ajoute une variable `messages` obtenue par une requête avec jointure sur les deux tables. Au lieu de renvoyer tous les messages, on privilégie le fait de renvoyer uniquement les 10 derniers :

```python 
@app.route('/')
def index() :
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Utilisateur.pseudo, Message.date, Message.message
        FROM Message JOIN Utilisateur ON Message.id_auteur = Utilisateur.id ORDER BY Message.date DESC;
        """)
    messages = cursor.fetchall()
    conn.close()        
    return render_template("index.html", messages = messages[:10])
```

Puis une route supplémentaire pour permettre l'ajout d'un message :

``` python
@app.route('/add_post', methods= ['GET', 'POST'])
def add_post() :
    if request.method == 'POST' :
        text = request.form['message']
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Message(id_auteur, message) VALUES (?, ?)", (session['user_id'], text))
        conn.commit()        
        conn.close()
    return redirect(url_for('index'))
```
On notera l'utilisation de `redirect`, qui n'a pas encore été évoquée. Par l'utilisation de `return redirect(url_for('index'))`, on force l'application à recharger complètement la route correspondant à la fonction `index`.

!!! warning "Un défaut"
    Un des défauts de cette manière de faire est qu'une personne connectée doit rafraichir «à la main» sa page si elle veut voir les derniers messages apparaitre. Une solution possible est d'utiliser Javascript et en particulier le format JSON pour automatiser le rafraichissement d'une partie de la page. Une vidéo intéressante, mais en anglais, est disponible [ici](https://www.youtube.com/watch?v=ATEGpAb8GWI){:target="_blank"}

### Ajouter du CSS

On crée un fichier `blog.css` dans le dossier `static`, contenant :

``` CSS
body{
    background-color : black;
    color : antiquewhite;
}
``` 

Puis dans le gabarit `base.html`, on insère la ligne suivante dans les méta-données :

``` HTML
<link href="{{"{{"}} url_for('static', filename='blog.css') {{"}}"}}" rel="stylesheet" type="text/css">
``` 
Toutes les pages de notre projet héritant du template `base.html`, le CSS sera appliqué sur chaque page.

!!! info "Fichier statiques"

    Pour les utilisations d'images, ou de tout autre fichier pouvant être utilisé par plusieurs pages de votre projet, il est nécessaire d'utiliser la syntaxe `url_for` pour écrire l'URL du fichier, afin qu'elle soit compatible quel que soit la machine utilisée. En travaillant ainsi, vous garantissez que même lors d'un déploiement réel, les url resteront correctes.

### Partie Facultative : page de modération

Pour l'instant, avoir des droits d'administration ne sert à rien. Nous allons modifier ce point en créant une page `moderation.html` qui permettra de supprimer un ou des messages.

On modifie d'abord le template `base.html` afin de faire apparaitre dans le «header» une page spécifique si l'utilisateur·trice connecté·e possède les droits d'administration Le code suivant est à placer après la ligne de déconnexion :

``` HTML
{{"{"}}% if session['autorisation'] == 0 %{{"}"}}
    <a href="{{"{{"}} url_for('moderation') {{"}}"}}">Modérer</a>    
{{"{"}}% endif %{{"}"}}
```

On crée ensuite une route `moderation` qui va contenir avoir plusieurs particularités :

* elle ne doit être accessible que par des personnes ayant les droits d'administration.
* elle doit afficher tous les messages par ordre chronologique inverse, sous la forme d'une liste de case à cocher dans un formulaire de type `POST`, chaque élément à cocher devant avoir pour valeur l'`id` (la clé primaire) du message dans la base de donnée (pour permettre la suppression).
* le formulaire doit renvoyer *vers la page `moderation` elle-même*, afin de permettre à la personne administratrice de poursuivre les suppressions.

``` python 
@app.route('/moderation', methods = ['GET', 'POST'])
def moderation() :
    if 'autorisation' not in session or session['autorisation']!= 0:
        flash('Page non autorisée')
        return redirect(url_for('index'))
    if request.method ==  'POST' :
        to_delete = request.form.getlist('suppression')
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        for id_message in to_delete :            
            cursor.execute("""DELETE FROM Message WHERE id =?""", (id_message,))
            print("delete ", id_message)
            conn.commit()
        conn.close()
            
    conn = sqlite3.connect('chat.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Message.id, Utilisateur.pseudo, Message.date, Message.message
        FROM Message JOIN Utilisateur ON Message.id_auteur = Utilisateur.id ORDER BY Message.date DESC;
        """)
    messages = cursor.fetchall()
    conn.close()
    return render_template('moderation.html', messages = messages)
``` 

Cette fonction utilise le template suivant :

``` HTML title="moderation.html"
{{"{%"}} extends "base.html" {{"%}"}}

{{"{%"}} block contenu {{"%}"}}
<h2>Liste des messages par ordre anté-chronologique : </h2>
{{"{%"}} if messages {{"%}"}}
<form action="{{"{{"}} url_for('moderation') {{"}}"}}" method="post">
    <input type="submit" value="envoyer" >
    {{"{%"}} for message in messages {{"%}"}}
    <div>
        
        <input type="checkbox" id="coche_{{"{{"}} message[0] {{"}}"}}" name="suppression" value="{{"{{"}} message[0] {{"}}"}}"  />
        <label for="{{"{{"}} message[0] {{"}}"}}">{{"{{"}} message[1] {{"}}"}} ({{"{{"}} message[2] {{"}}"}}) : {{"{{"}} message[3] {{"}}"}}</label>
    </div>
    {{"{%"}} endfor {{"%}"}}
    <input type="submit" value="envoyer">
</form>
{{"{%"}} endif {{"%}"}}
{{"{%"}} endblock {{"%}"}}
```

### Partie facultative : Les routes à paramètres

Il est tout à fait possible de passer des paramètres aux fonctions établissant les différentes routes. Comme il est très tard, et que je commence à fatiguer, vous pouvez voir un exemple d'utilisation pour les personnes disposant de droits d'administration, en téléchargeant l'archive ZIP suivante : [Blog.zip](Blog/Blog.zip){:target="_blank"}.




## Votre projet BDD

Vous devez construire une application Flask utilisant une base de données, sur le thème de votre choix, et dans laquelle il existe plusieurs pages :

* des pages de visualisation des données ;
* des pages d'insertion de données ;
* des pages de modification de données ;
* éventuellement un système d'inscription pour des utilisateurs (mais ce n'est pas obligé).

La grille de notation est flous, car les projets sont en général très différents les uns des autres, mais gardez en tête les points suivants :

* les différents fichiers doivent être bien organisés et leurs noms faciles à comprendre ;
* le code Python doit être a minima commenté ;
* le nom des variables doit être facile à lire ;
* les requêtes SQL doivent être correctement écrites.



