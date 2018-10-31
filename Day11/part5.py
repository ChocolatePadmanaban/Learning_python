# array filters

import numpy as np 
arr = np.arange(100,200)
select = [5,25,50,75,-5]
print(arr[select])
arr = np.arange(10,20)
div_by_3 = arr%3==0
print(div_by_3)
print(arr[div_by_3])
print(arr.sum())
print(arr.mean())
print(arr.std())
print(arr.max())
print(arr.min())
print(div_by_3.all())
print(div_by_3.any())
print(div_by_3.sum())
print(div_by_3.nonzero())