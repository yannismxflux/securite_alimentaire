import pandas as pd
import os
import psycopg2
import creat_connect_sql_db as sql



def reader():
    file = pd.read_csv('export_alimconfiance.csv', sep=';', parse_dates=['Date_inspection'])
    file.drop_duplicates(subset="SIRET", keep='first', inplace=True)


    for i in file.columns:
        file[i] = file[i].replace(',','', regex=True)
    file.to_csv("CSV_ETABLISSEMENT.csv", na_rep='NA', header=False, columns = ["SIRET","APP_Libelle_etablissement","Adresse_2_UA","Code_postal","Libelle_commune", "APP_Libelle_activite_etablissement", "geores"])
    file.to_csv("CSV_INSPECTION.csv", na_rep='NA', header=False, columns = ["Numero_inspection", "Synthese_eval_sanit", "Date_inspection","SIRET"])
    print("2 CSV CREATED.......")
    return(file)



if __name__ == "__main__":
    file = reader()
    sql.creat_db()
    sql.insert_values()
