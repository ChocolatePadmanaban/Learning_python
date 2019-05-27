def insertionSort(arr): 
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp

  
if __name__=="__main__":
    a=[1,1,8,9,7,6,5,4,3,2,1,1,1,1]
    print(a)
    insertionSort(a)
    print(a)