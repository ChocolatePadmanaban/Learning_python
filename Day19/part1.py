#Linear Regression

import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("wdbc.data.csv", header= None)
print(df.shape)
X= df.loc[:, 2:].values
y = df.loc[:,1].values
le = LabelEncoder()
y= le.fit_transform(y)

X_train, X_test , y_train,y_test= train_test_split(X,y,test_size = .2,random_state=1)
pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=4)),
                    ('lr', LogisticRegression(random_state=1, penalty='l1'))])

pipe_lr.fit(X_train, y_train)
print('Train Accuracy' , pipe_lr.score(X_train, y_train))
print("Test ACcuracy", pipe_lr.score(X_test,y_test))
y_pred = pipe_lr.predict(X_test)
print("Misclassified in test",(y_pred!=y_test).sum())
