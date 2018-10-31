# multi dimensional array
import numpy as np 
a34= np.array([[12,10,-21,7],
                [-17,18,19,16],
                [13,-7,-18,10]])

print(a34)
print(a34.size)
print(a34.shape)
print("Second row is", a34[1])
print("First column is", a34[:,0])
print("Second row third element is",a34[1,2])
print("Slice of the matrix", a34[1,1:3])
a34[1,2]= 7
print("changed array",a34)


x = np.arange(0,10,1) #arguments start, stop , step
print(x)

print(np.linspace(0,10,25)) # linspace numpy
print(np.logspace(0,10,10,base=np.e)) #logspace numpy
