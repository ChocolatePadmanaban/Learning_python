# Handling categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd 
df = pd.DataFrame([['green','M',10.1,'class1'],
                ['red','L',13.5,'class2'],
                ['blue', 'XL', 15.3, 'class1']])
df.columns=["color",'size','price','classlabel']
size_mapping = {'XL':3, 'L':2,'M':1}
class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}

if __name__ == "__main__":
    print(df)
    df['size'] = df['size'].map(size_mapping)
    print(df)
    print(class_mapping)
    df['classlabel']= df['classlabel'].map(class_mapping)
    print(df)
    X = df[['color','size','price']].values
    color_le = LabelEncoder()
    X[:,0]= color_le.fit_transform(X[:,0])
    ohe = OneHotEncoder(categorical_features=[0])
    print(X)
    print(ohe.fit_transform(X).toarray())