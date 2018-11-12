#predicting with logistic Regression

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd

iris = load_iris()
X = iris.data[:150]
y = iris.target[:150]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.3)
print("Shape of X_train is",X_train.shape)
lreg = LogisticRegression(penalty='l1',C=1)
lreg.fit(X_train,y_train)
y_pred = lreg.predict(X_test)
print('Misclassified ',(y_test-y_pred).sum())
