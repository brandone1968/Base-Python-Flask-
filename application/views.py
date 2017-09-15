#from flask import Flask, render_template, url_for, request
from flask import Flask, render_template, request, make_response, abort, flash, url_for
from flask.helpers import flash
from unicodedata import category
from flask.templating import render_template
app = Flask(__name__)
from .models import Utenti
from .forms import *



# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

# @app.route('/')
# @app.route('/index/')
# def index():
#     nuovo_utente = Utenti()
#     #nuovo_utente.add_data("Zio Paperone", "De Paperoni", 70)
#      
#     list_records = nuovo_utente.list_all_utenti()
#     return render_template("index.html", list_records=list_records)

@app.route('/')
@app.route('/index/')
@app.route('/index/<int:page>')
def index(page=1):
    nuovo_utente = Utenti()
    list_records = nuovo_utente.list_all_utenti(page,app.config['LISTINGS_PER_PAGE'])
    return render_template("index.html", list_records=list_records)

@app.route('/add_record', methods=['GET', 'POST'])
def add_record():
    form = Form_New_Message(request.form)
    
    if request.method == 'POST':
        if form.validate():
            nuovo_utente = Utenti()
            nome = form.nome.data
            cognome = form.cognome.data
            eta = form.eta.data
            nuovo_utente.add_data(nome, cognome, eta)
            flash("Utente salvato", category="success")
            
    return render_template("add_record.html", form=form)





