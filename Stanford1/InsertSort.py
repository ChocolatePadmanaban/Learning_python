def insertSort(Arrlist):
    for i in range(1,len(Arrlist)):
        j=i-1
        temp=Arrlist[i]
        while j>=0 and Arrlist[j]>=temp:
            Arrlist[j+1]=Arrlist[j]
            j-=1
        Arrlist[j+1]=temp


if __name__=="__main__":
    a=[1,1,1,1,1,19,8,7,6,5,4,1,1,1,3,2,1,1,1,1,1,1]
    print(a)
    insertSort(a)
    print(a)