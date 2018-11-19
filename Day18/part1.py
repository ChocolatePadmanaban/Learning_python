# pearsonr corealation coefficient


from scipy.stats import pearsonr
print(pearsonr([1,2,3],[1,2,3.1]))
print(pearsonr.__doc__)

# Data analytic methods: Principle component Analysis manually
from numpy import array, mean, cov
from numpy.linalg import eig

A = array([[1,2],[3,4],[5,6]])

M = mean(A.T, axis=1)

C= A-M

V = cov(C.T)

values, vectors = eig(V)


P = vectors.T.dot(C.T)
print(P.T)

# Principle component analysis with buit in functions
from sklearn.decomposition import PCA
A = array([[1,2],[3,4],[5,6]])
print(A)

pca = PCA(2)

pca.fit(A)

print(pca.components_)
print(pca.explained_variance_)

B= pca.transform(A)
print(B)