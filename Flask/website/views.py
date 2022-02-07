
# import pickle
from joblib import load
from flask import Blueprint, render_template, request
import numpy as np
import pandas as pd

views = Blueprint('views', __name__)

# Load the model
#model = pickle.load(open('website/finalized_model.sav', 'rb'))
model=load("website/classification.joblib")

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
    agrement=request.form['agrement']
    type_activite = request.form['type_activite']
    X=[[code_postal,agrement,"2",type_activite,code_postal[:2]]]
    X=pd.DataFrame(data=X)
    prediction=model.predict(X)
    return render_template("predict.html", user = 'ok',
                                        name=name, 
                                        siret=siret, 
                                        adresse=adresse, 
                                        code_postal=code_postal,
                                        ville=ville,
                                        type_activite=type_activite,
                                        prediction=prediction)