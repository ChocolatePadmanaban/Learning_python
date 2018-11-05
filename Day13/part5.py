# Data Frame

from pandas import DataFrame
import numpy as np 
frame = DataFrame(np.arange(12).reshape((4,3)),
                index=[['a','a','b','b'],[1,2,1,2]],
                columns= [['Ohio','Ohio','Colorado'],
                        ['Green','Red','Green']])
#print(frame)
frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
print(frame)

