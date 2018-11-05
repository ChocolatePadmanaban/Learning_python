#unstack in Series
import pandas as pd
import numpy as np
s1= pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(data2.unstack())
print(data2.unstack().stack())
print(data2.unstack().stack(dropna=False))

#dataFrame duplicate

import pandas as pd
data = pd.DataFrame({'k1':['one']*3+['two']*4,
                    'k2': [1,3,2,3,3,4,4]})

print(data.duplicated('k2'))
print(data.drop_duplicates('k1'))

#pandas bins
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats.codes)
print(pd.value_counts(cats))
#To change open close, pass right=False

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))
data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))
