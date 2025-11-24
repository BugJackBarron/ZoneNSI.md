from flask import Flask,render_template
import datetime
from math import pi
app = Flask(__name__)


@app.route('/')
def index():
    p = "Kakashi"
    n = "Hatake"
    date = datetime.datetime.now()
    heure = date.hour
    minute = date.minute
    seconde = date.second
    return render_template("index.html",prenom = p,
     nom = n, heure = heure, minute=minute, seconde=seconde)



@app.route('/contact')
def presentation():
    message = "<h1> Présentation du webmaster </h1>"
    message += "<h2> Kakashi Hatake </h2>"
    message += "<p>  Jônin du village caché de Konoha, Sixième Hokage </p>"
    message += """<a href="mailto:kakashihatake@konoha.jp">Mon mail</a> """
    return message

if __name__ == "__main__" :
    app.run(debug=True)
