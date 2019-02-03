#Priciple component analysis in wine data

import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from numpy import array
from sklearn.decomposition import PCA



df_wine = pd.read_csv('wine.csv',header=None)

df_wine.columns = ['Class label','Alcohol','Malic acid',
                   'Ash','Alcalinity of ash','Magnesium',
                   'Total phenols','Flavanoids','Nonflavanoid phenols',
                   'Proanthocyanins','Color intensity','Hue',
                   'OD280/OD315 of diluted wines','Proline']

print(df_wine.head())
print('=======================================')

Y = df_wine.iloc[:,0].values
X = df_wine.iloc[:,1:].values

x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.3)
sc = StandardScaler()
x_train_std = sc.fit_transform(x_train)     # Standardized value
x_test_std = sc.transform(x_test)

pca = PCA(n_components=5)
print('Standardized data: ',x_train_std)
x_train_pca = pca.fit_transform(x_train_std)
x_test_pca = pca.transform(x_test_std)
print('Principal data: \n',x_train_pca)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(x_train_pca,y_train)

print('MisClassification in training', lr.score(x_train_pca, y_train))
print('MisClassification in Test', lr.score(x_test_pca, y_test))
