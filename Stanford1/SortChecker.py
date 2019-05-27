from InsertSort import insertSort
from MergeSort import mergeSort
from random import randrange
def sortChecker(SortName, N):
    a=[randrange(1,N+1) for i in range(N)]
    b=a.copy()
    print("Before Sort",a)
    a.sort()
    SortName(b)
    print(b==a,b)



if __name__=="__main__":
    sortChecker(mergeSort,100)