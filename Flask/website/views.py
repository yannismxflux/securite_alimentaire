
import pickle
from flask import Blueprint, render_template, request
import numpy as np
from sklearn.preprocessing import OneHotEncoder

views = Blueprint('views', __name__)

# Load the model
#model = pickle.load(open('website/finalized_model.sav', 'rb'))

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user = 'ok')

@views.route('/predict', methods=['GET', 'POST'])
def predict():
    name = request.form['name']
    siret = request.form['siret']
    adresse = request.form['adresse']
    code_postal = request.form['code_postal']
    ville = request.form['ville']
    type_activite = request.form['type_activite']
    prediction = 0
    return render_template("predict.html", user = 'ok',
                                        name=name, 
                                        siret=siret, 
                                        adresse=adresse, 
                                        code_postal=code_postal,
                                        ville=ville,
                                        type_activite=type_activite,
                                        prediction=prediction)