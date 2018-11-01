#Sorting and Ranking
import pandas as pd 
import numpy as np

obj = pd.Series(range(4),index=['d','a','b','c'])
print(obj.sort_index())

frame = pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],
        columns = ['d','a','b','c'])

print(frame.sort_index())
print(frame.sort_index(by='b'))