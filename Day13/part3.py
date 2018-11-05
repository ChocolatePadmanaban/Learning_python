# datafRAMES AUTO MERGING

import pandas as pd 
import numpy as np 
# df1 = pd.DataFrame({'key':['a','a','b','c','c','b','c'],
#                     'value':range(7)})
# df2 = pd.DataFrame({'val': [12,7,9]}, index= ['a','b','d'])
# print(pd.merge(df1,df2,left_on='key',right_index=True))
#--------------------------------------------------------------------------------#
df3 = pd.DataFrame({'key1':['MH','MH','MH','TN','TN'],
                    'key2': [2000,2001,2002,2001,2000],
                    'data': [3,2,5,6,9]})
print(df3)

df4 = pd.DataFrame(np.arange(12).reshape((6,2)),
                    index= [['TN','KL','KA','AP','TL','MH'],
                    [2000,2000,2000,2000,2001,2002]],
                    columns =['event1','event2'])
print(df4)

sdf = df4.stack()
print(sdf.unstack(0))#to take transpose in pandas 