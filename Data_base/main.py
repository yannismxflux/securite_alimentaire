from operator import index
import pandas as pd
import os
import psycopg2
import creat_connect_sql_db as sql



def reader():
    file = pd.read_csv('export_alimconfiance.csv', sep=';',encoding = "utf-8",dtype={'Code_postal':str}, parse_dates=['Date_inspection'])
    for i in file.columns:
        file[i] = file[i].replace(';','', regex=True)
    new_file=file[file['SIRET'].str.len()==14] 
    new_file.to_csv('Clean_Alimconfonfiance.csv',sep=';')
    etablissement_file=new_file[["SIRET","APP_Libelle_etablissement","Adresse_2_UA","Code_postal","Libelle_commune", "geores","ods_type_activite","Agrement"]]
    etablissement_file=etablissement_file.drop_duplicates(subset="SIRET", keep='first')
    etablissement_file.to_csv("CSV_ETABLISSEMENT.csv", sep=';',na_rep="NA",header=False,index=False)
    inspection_file=new_file[["Numero_inspection", "Synthese_eval_sanit","APP_Libelle_activite_etablissement","Date_inspection","SIRET"]]
    inspection_file.to_csv("CSV_INSPECTION.csv", header=False,sep=';',index=False)
    print("2 CSV CREATED.......")
    return(file)



if __name__ == "__main__":
    file = reader()
    sql.creat_db()
    sql.insert_values()
