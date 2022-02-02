
import pickle
from flask import Blueprint, render_template, request
import numpy as np
from sklearn.preprocessing import OneHotEncoder

views = Blueprint('views', __name__)

# Load the model
#model = pickle.load(open('website/finalized_model.sav', 'rb'))

@views.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_file = open('website/static/utilisateurs.txt', 'r')
        for line in user_file.readlines():
            login_info = line.split()
            if email == login_info[0] and password == login_info[1]:
                return render_template("home.html", user = 'ok')
        message = "Erreur de login"
        return render_template("home.html", message = message)

@views.route('/predict', methods=['GET', 'POST'])
def predict():
    name = request.form['name']
    siret = request.form['siret']
    adresse = request.form['adresse']
    code_postal = request.form['code_postal']
    ville = request.form['ville']
    type_activite = request.form['type_activite']
    prediction = 1
    return render_template("predict.html", user = 'ok',
                                        name=name, 
                                        siret=siret, 
                                        adresse=adresse, 
                                        code_postal=code_postal,
                                        ville=ville,
                                        type_activite=type_activite,
                                        prediction=prediction)