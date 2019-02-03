#indian stocks

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

min_index = pd.read_csv('NIFTY-I.csv',header=None)
min_index.columns = ['date','time','open','high',
                    'low','close','volume','IO']

min_index['period'] = min_index['date'].map(str)+min_index['time']

min_index= min_index.drop(axis=1,columns = ['date','time'])

min_index['period']= pd.to_datetime(min_index['period'],format='%Y%m%d%H:%M')

min_index= min_index.set_index('period')
print(min_index.head())