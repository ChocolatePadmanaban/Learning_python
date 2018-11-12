#Standard Scalar (standardisation with inbuilt functions)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data[:]
y = iris.target[:]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.transform(X_test)
print("Shape of X_train is",X_train_std.shape)
lreg = LogisticRegression(penalty='l1',C=1)
lreg.fit(X_train_std,y_train)
y_pred = lreg.predict(X_test_std)
print('Misclassified ',(y_test-y_pred).sum())
