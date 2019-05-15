def insertionSort(arr): 
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

  
if __name__=="__main__":
    a=[1,1,8,9,7,6,5,4,3,2,1,1,1,1]
    print(a)
    insertionSort(a)
    print(a)