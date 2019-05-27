def mergeSort(alist):
    if len(alist)>1:
        mid=len(alist)//2
        Left=alist[:mid]
        Right=alist[mid:]
        mergeSort(Left)
        mergeSort(Right)
        i=j=k=0
        while i<len(Left)and j<len(Right):
            if Left[i]<Right[j]:
                alist[k]=Left[i]
                i+=1
            else:
                alist[k]=Right[j]
                j+=1
            k+=1
        while i<len(Left):
            alist[k]=Left[i]
            i+=1
            k+=1
        while j<len(Right):
            alist[k]=Right[j]
            j+=1
            k+=1
            
        



if __name__=="__main__":
    a=[9,8,7,6,5,4,3,2,1,1,1,1,1]
    print(a)
    mergeSort(a)
    print(a)