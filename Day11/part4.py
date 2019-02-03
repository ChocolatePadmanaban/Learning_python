#mesh grid

import numpy as np

x, y = np.mgrid[1:6,10:14]
print(x)
print(y)
print(x*y)
print(np.mgrid.__doc__)

print(np.random.rand(5,5))
print(np.random.rand.__doc__)

print(np.random.randn(9))
print(np.random.randn.__doc__)