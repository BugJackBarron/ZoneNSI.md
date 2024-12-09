from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'PAS_TOP_COMME_CLE_SECRETE'

@app.route('/')
def index() :
    return "Hello World !"

if __name__ == "__main__" :
    app.run(port=5555, debug=True)