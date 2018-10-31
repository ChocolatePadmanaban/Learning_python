#declaring one dimension array in numpy

import numpy as np 
a1 = np.array([12,-9,10,8,-13])
a2 = np.array([-6,17,5,12,-9])

print(a1)
print(type(a1))
print(a1.dtype)
if type(a1) is np.ndarray:
    print("an array")

if a1.dtype== np.int64:
    print("An array of numbers")

print("array multiplication",a1*.4)
print("array division",a1/2)
print("array addition", a1+2)
print("array Subraction", a1-2)