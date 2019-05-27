def quickSort(alist,first,last):
    if first<last:
        splitvalue=partition(alist,first,last)
        quickSort(alist,first,splitvalue-1)
        quickSort(alist,splitvalue+1,last)

def partition(alist,first,last):
    pivotvalue=alist[first]
    leftmark=first+1
    rightmark=last
    done=False
    while not done:
        while leftmark<=rightmark and alist[leftmark]<=pivotvalue:
            leftmark+=1
        while rightmark>=leftmark and alist[rightmark]>=pivotvalue:
            rightmark-=1
        if leftmark>rightmark:
            done=True
        else:
            alist[leftmark],alist[rightmark]=alist[rightmark],alist[leftmark]
    alist[first],alist[rightmark]=alist[rightmark],alist[first]
    return rightmark

if __name__=="__main__":
    a=[1,1,9,8,7,6,5,4,3,2,1,1,1,1]
    print(a)
    quickSort(a,0,len(a)-1)
    print(a)