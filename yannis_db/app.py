#%%
import pandas as pd

df = pd.read_csv('../Data_base/export_alimconfiance.csv', sep=';',encoding = "utf-8",
        dtype={'Code_postal':str}, parse_dates=['Date_inspection'])
df.head()
# %%
new_file=df[df['SIRET'].str.len()==14]
# %%
new_file.head()
# %%
etablissement_file=new_file[["SIRET","APP_Libelle_etablissement","Adresse_2_UA","Code_postal","Libelle_commune", "geores","ods_type_activite"]]
etablissement_file.head()
etablissement_file.shape
# %%
etablissement_file=etablissement_file.drop_duplicates(subset="SIRET", keep='first')
etablissement_file.shape
# %%
inspection_file=new_file[["Numero_inspection", "Synthese_eval_sanit","APP_Libelle_activite_etablissement","Date_inspection","SIRET"]]
# %%
inspection_file.describe()
# %%
inspection_file.Synthese_eval_sanit.value_counts()
# %%
