from flask import Flask, render_template, request, session, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

app.secret_key = 'PAS_TOP_COMME_CLE_SECRETE'

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

@app.route('/connexion')
def connexion() :
    return render_template('connexion.html')

@app.route('/check_login', methods=['GET', 'POST'])
def check_login() :
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = request.form['password']

        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, pseudo, id_autorisation FROM Utilisateur WHERE pseudo = ? AND password = ?", (pseudo, password))
        user = cursor.fetchone()
        conn.close()        
        if user:
            flash('Connexion réussie!', 'success')
            session['user_id'] = user[0]
            session['pseudo'] = user[1]            
            session['autorisation'] = user[2]
            return redirect(url_for('index'))
        else:
            print('Echec')
            flash('Pseudo ou mot de passe incorrect', 'danger')

    return render_template('connexion.html')

@app.route('/disconnect')
def disconnect() :
    session.pop('pseudo', None)
    session.pop('user_id', None)
    session.pop('autorisation', None)
    return redirect(url_for('index'))

@app.route('/inscription')
def inscription() :
    if 'pseudo' in session :
        flash("Vous êtes déjà inscrit·e !")
        return redirect(url_for('index'))
    return render_template('inscription.html')

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
            flash("le mot de passe doit être au moins de longueur 10")
            return render_template('inscription.html')            
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute(""" INSERT INTO Utilisateur(pseudo, password, email, id_autorisation) VALUES (?, ?, ?, 1) ;""", (pseudo, password,email,))
        conn.commit()
        conn.close()
        flash("Vous êtes inscrit·e. Veuillez vous connecter !")
        return redirect(url_for("connexion"))
        
        
    return render_template('inscription.html')

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

@app.route('/utilisateurs', methods=['GET', 'POST'])
@app.route('/utilisateurs/<numero>', methods=['GET', 'POST'])
def utilisateur(numero = None) :
    if 'autorisation' not in session or session['autorisation']!= 0:
        flash('Page non autorisée')
        return redirect(url_for('index'))
    if request.method == 'POST' :
        id = request.form['id']
        pseudo = request.form['pseudo']
        email = request.form['email']
        password = request.form['password']
        print(password)
        id_autorisation = request.form['droits']
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("""
                       UPDATE Utilisateur
                       SET pseudo= ?,
                       email = ?,
                       password = ?,
                       id_autorisation = ?
                       WHERE id= ?""", (pseudo, email, password, id_autorisation, id))
        conn.commit()
        conn.close()
        return redirect(url_for('utilisateur'))
                       
        
    elif numero is not None :
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Utilisateur WHERE id = ?", (numero,))
        user = cursor.fetchone()
        conn.close()
        return render_template('utilisateur.html',user =user)
    else :
        conn = sqlite3.connect('chat.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT id, pseudo, email, id_autorisation FROM Utilisateur""")
        liste = cursor.fetchall()
        conn.close()
        return render_template('utilisateurs.html', liste= liste)
    
    

if __name__ == "__main__" :
    app.run(port=5555, debug=True)