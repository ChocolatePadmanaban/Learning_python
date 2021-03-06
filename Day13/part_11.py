import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

tips = pd.read_csv('tips.csv')
#print(tips.head())
tips['tip_pct'] = tips['tip']/tips['total_bill']

grouped = tips.groupby(['sex'])
gsum = grouped.sum()['size']
print(gsum)
gsum.plot(kind= 'bar')
grouped_pct = grouped['tip_pct']

print(grouped_pct.agg('mean'))

print(grouped_pct.agg('mean'))
print(grouped_pct.agg(['mean', 'std', lambda arr: arr.max()-arr.min()]))
print(grouped_pct.agg([('foo','mean'),('bar',np.std),
                        ('p2p', lambda arr:arr.max()- arr.min())]))


party_counts = pd.crosstab([tips.day,tips.sex],tips.size)
print(party_counts)
myplot= party_counts.plot(kind='pie',subplots= 'True')
plt.show()
