#clean data by replaceing with mean
import pandas as pd
from sklearn.preprocessing import Imputer

if __name__ =="__main__":
    df = pd.read_csv('data.csv', header=None)
    imr = Imputer(missing_values='NaN',strategy='mean',axis=0)
    imr = imr.fit(df)
    imputed_data = imr.transform(df.values)
    print(imputed_data)