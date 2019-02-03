# sub plots

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6, 4))
fig.add_subplot(231).hist(np.random.randn(100),bins= 20,color='k',alpha=.3)
fig.add_subplot(233).scatter(np.arange(30),
                    np.arange(30)+3*np.random.randn(30))
fig.add_subplot(235).plot(np.sin(np.linspace(-np.pi,np.pi,256)))
plt.show()