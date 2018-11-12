from sklearn import tree
from IPython.display import Image, display
import pydotplus
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data[:]
y = iris.target[:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
print("Shape of X_train is", X_train.shape)
decisionTreeClassifier = DecisionTreeClassifier()
decisionTreeClassifier.fit(X_train, y_train)
y_pred = decisionTreeClassifier.predict(X_test)
print('Misclassified ', (y_test-y_pred).sum())


dot_data = tree.export_graphviz(decisionTreeClassifier, out_file=None,
                                feature_names=iris.feature_names,
                                class_names=iris.target_names,
                                filled=True, rounded=True,
                                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)

display(Image(data=graph.create_png()))
