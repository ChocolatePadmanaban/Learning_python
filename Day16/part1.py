#iris dataset
#https://en.wikipedia.org/wiki/Iris_flower_data_set

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
import numpy as np
import pandas as pd


iris = load_iris()
# print(iris)
X = iris.data[50:150,2:4]
y = iris.target[50:150]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
print("Shape of X_train is",X_train.shape)
ppn = Perceptron(max_iter=20, eta0=.1)
ppn.fit(X_train,y_train)
y_pred = ppn.predict(X_test)
print('Misclassified ',(y_test-y_pred).sum())
print(y_pred)
print(y_test)
print(y_test-y_pred)