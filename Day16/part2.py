#predicting in wine dataset
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import numpy as np
import pandas as pd

df_wine = pd.read_csv('wine_data.csv', header=None)
y = df_wine.iloc[:,0].values
X = df_wine.iloc[:,1:].values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
print("Shape of X_train is",X_train.shape)
ppn = Perceptron(max_iter=30, eta0=.1)
ppn.fit(X_train,y_train)
y_pred = ppn.predict(X_test)
print('Misclassified ',(y_test-y_pred).sum())
