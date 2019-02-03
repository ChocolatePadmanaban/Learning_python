# soting in numpy

import numpy as np 
x = np.array([4.5,2.3,4.5,1.2,3.4])
print(np.sort(x))
print(x.argsort())

# array operations inverse

a = np.array([[1,2],[5,12]])
print("a is",a)
print("Inverse of a\n",np.linalg.inv(a))

# https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.linalg.inv.html

print("Identity matrix\n", np.eye(3))