# converting array to matrix for real
import numpy as np 
# Numpy – matrices
# Numpy – matrices
a = np.array([[1,2],[3,4]]) 
m = np.mat(a) # convert 2-d array to matrix 
m = np.matrix([[1, 2], [3, 4]]) 
print(a[0]) 
# result is 1-dimensional 

print(m[0]) 

print(a*a) 
# element-by-element multiplication 
#array([[ 1, 4], [ 9, 16]]) 
print(m*m)
# (algebraic) matrix multiplication 
print(a**3) 
# element-wise power 
print(m**3) 
# matrix multiplication m*m*m 
 
print( m.T) 
# transpose of the matrix  
print(m.H) 
# conjugate transpose (differs from .T for complex matrices) 
print(m.I)
# inverse matrix 
# matrix([[-2. , 1. ], [ 1.5, -0.5]])
# Array and matrix operations may be quite different!
