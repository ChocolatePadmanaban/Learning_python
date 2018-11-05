# importing data into pandas from internet or csv files

import pandas as pd 
df_wine = pd.read_csv(r'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data')

df_wine.columns = ['Alcohol ','Malic acid ','Ash','Alcalinity of ash','Magnesium '
,'Total phenols','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins',
'Color intensity','Hue','OD280/OD315 of diluted wines','Proline']

print(df_wine.head())
data = df_wine.iloc[:,1:].values
print(data)