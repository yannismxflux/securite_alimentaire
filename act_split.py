#%%
import pandas as pd 

df = pd.read_csv('Machine Learning/ml_dataset.csv')
act=df['activite_category'].unique()
act.shape
act=pd.DataFrame(data=act)
act.to_csv('activity.csv',sep=';',index=False)
# %%
