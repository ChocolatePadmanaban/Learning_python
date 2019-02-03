# Regular plots


#%matplotlib
import matplotlib.pyplot as plt
import numpy as np
X= np.linspace(-np.pi,np.pi,256)
Y1 = np.sin(X)
Y2 = np.cos(X)
#Y3 = np.sqrt(1-X*X)

#plt.plot(X,Y1) # sinh curve
#plt.plot(X, Y2)# cos curve
#plt.plot(X, Y3)#  costomised curve
plt.figure(figsize=(6,4),dpi=100)
plt.plot(X,Y1,color = "blue", linestyle= '-.',label = 'sin')
plt.plot(X,Y2,color = "maroon", linewidth= 2.5, linestyle=':',label='cos')
plt.xlim(X.min()*1.2)
print(plt.xlim.__doc__)
plt.xticks([-np.pi,-np.pi/2,-0,np.pi/2,np.pi],
            [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'],
            rotation= 30)
ax = plt.gca()
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)

ax.xaxis.set_ticks_position('bottom')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
plt.legend(loc="best")
for labels in ax.get_xticklabels()+ax.get_yticklabels():
    labels.set_fontsize(11)
    labels.set_bbox(dict(facecolor = 'grey',edgecolor=None,alpha= 0.35))
    
plt.show()