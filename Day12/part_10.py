# DataFrames  merging


import pandas as pd
# df1 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
#                  'data1': range(7)})
# df2 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})
# print(pd.merge(df2, df1,left_on='rkey',right_on='lkey',how= 'left'))
left = pd.DataFrame({'st':['KA','KA','KL'],
                    'fg': ['pd','wh','pd'],
                    'lqty': [12,11,14]})
right = pd.DataFrame({'st':['KA','KA','KL','KL'],
                    'fg':['pd','pd','pd','cn'],
                    'rqty':[5,7,6,4]})
print(pd.merge(left,right,on=['st'],how='left'))
print(pd.merge(left,right,on=['fg','st'],how= 'right'))