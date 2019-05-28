def mergeSort(alist):
    if len(alist)>1:
        midv=len(alist)//2
        left=alist[:midv]
        right=alist[midv:]

        mergeSort(left)
        mergeSort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                alist[k]=left[i]
                i+=1
            else:
                alist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            alist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            alist[k]=right[j]
            j+=1
            k+=1
        



if __name__=="__main__":
    a=[9,8,7,6,5,4,3,2,1,1,1,1,1]
    print(a)
    mergeSort(a)
    print(a)