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
                    index= [['TN','TN','MH','MH','MH','MH'],
                    [2000,2000,2000,2000,2001,2002]],
                    columns =['event1','event2'])
print(df4)

print(pd.merge(df3,df4,left_on=['key1','key2'],right_index=True))
arr = np.arange(12).reshape((3, 4))
print(np.concatenate([arr, arr], axis=1))


s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
pd.concat([s1, s2, s3])
pd.concat([s1, s2, s3], axis=1)
s4 = pd.concat([s1 * 5, s3])
pd.concat([s1, s4], axis=1) 
pd.concat([s1, s4], axis=1, join='inner')
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])