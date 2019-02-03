#Regression analysis

import pandas as pd 
df = pd.read_csv('housing.data.txt',header=None, sep='\s+')

df.columns = ['CRIM', 'ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX',
    'PTRATIO','B','LSTAT','MEDV']
print(df.head())
# got the data
import matplotlib.pyplot as plt
import seaborn as sns
cols = ['RM','TAX','PTRATIO', 'LSTAT', 'MEDV']
sns.set(style='whitegrid', context='notebook')

sns.pairplot(df[cols], size=2.5)
plt.tight_layout()
plt.show()

import numpy as np 

cm = np.corrcoef(df[cols].values.T)
sns.set(font_scale=1.5)
hm = sns.heatmap(cm,
                cbar=True,
                annot=True,
                square=True,
                fmt= '.2f',
                annot_kws={'size':15},
                yticklabels= cols,
                xticklabels= cols)
plt.tight_layout()
plt.show()# prints correlation coeffient 

X = df[['RM']].values

y = df['MEDV'].values

def lin_regplot(X,y, model):
    plt.scatter(X,y,c='blue')
    plt.plot(X,model.predict(X),color='red')
    return None

from sklearn.linear_model import LinearRegression,Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

slr= LinearRegression()
slr.fit(X,y)
print('Slope: %.3f' % slr.coef_[0])
print('Intercept: %.3f'% slr.intercept_)
lin_regplot(X,y,slr)
plt.xlabel('RM')
plt.ylabel('Price')
plt.tight_layout()
plt.show()

# Till now linear regression

X = df.iloc[:,:-1].values
y = df['MEDV'].values

X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=.3 , random_state= 0)
ridge = Ridge(alpha=1)
slr = LinearRegression()

slr.fit(X_train, y_train)
y_train_pred = slr.predict(X_train)
y_test_pred = slr.predict(X_test)

print('MSE train: %.3f, test: %.3f'%(mean_squared_error(y_train, y_train_pred),
mean_squared_error(y_test,y_test_pred)))

print('R^2 train: %.3f, test: %.3f' % (r2_score(y_train, y_train_pred),
(r2_score(y_test,y_test_pred))))

plt.scatter(y_train_pred, y_train_pred-y_train,c='blue',marker='o',label = 'Taining Data')
plt.scatter(y_test_pred, y_test_pred-y_test,c='red',marker='o',label = 'Test Data')

plt.show()