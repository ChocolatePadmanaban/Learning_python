#working with dataframe

import numpy as np 
import pandas as pd 

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns = list('abcd'),
                    index= ['tn','ka','kl'])
s1 = df1.loc['ka']
print(df1)
print(s1)
# print(df1+s1)

f = lambda x: x.max()-x.min()
print("executing via row vice\n",df1.apply(f))
print("executing via column vice\n",df1.apply(f,axis=1))