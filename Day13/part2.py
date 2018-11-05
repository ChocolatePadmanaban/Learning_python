# replicating part one

import pandas as pd 
df_wine = pd.read_csv('file.csv',header= None)

df_wine.columns = ['one','two','three','four','five']
df_wine = df_wine.set_index('five')

print(df_wine)