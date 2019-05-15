def Swap(Arr,Pivot):
    if len(Arr)!=1:
        print(Arr, Pivot)
        if len(Arr)==Pivot+1:
            return Swap(Arr,0)
        elif Arr[Pivot]>=Arr[Pivot+1]:
            Arr[Pivot],Arr[Pivot+1]=Arr[Pivot+1],Arr[Pivot]
            return Swap(Arr,Pivot+1)
        elif Arr[Pivot]<Arr[Pivot+1] and Pivot!=0 :
            return Swap(Arr,Pivot+1)
    return Arr,Pivot
    

def Quick(Arr,Pivot=0):
    Arr, Pivot= Swap(Arr, Pivot)
    print(Pivot)
    if len(Arr)!= 1:
        if len(Arr)==Pivot+1:
            Quick(Arr[:Pivot],0)
            print(Arr,"Quick")
        elif Pivot !=0:
            Quick(Arr[:Pivot],0)
            Quick(Arr[Pivot+1:],0)



if __name__=="__main__":
    A=[9,8,7,6,5,5,5,4,3,2,1,5,5]
    Quick(A)
    print(A)

