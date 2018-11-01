# DataFrames 


import pandas as pd
df1 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
print(pd.merge(df2, df1,left_on='rkey',right_on='lkey',how= 'left'))