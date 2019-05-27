from itertools import permutations,combinations

def timeTaken(alist):
    meters,colors=alist[0]
    secondTaken= meters
    for i in range(1,len(alist)):
        if alist[i][1]==colors:
            secondTaken+=alist[i][0]-meters
        else:
            secondTaken+=alist[i][0]+meters
        meters,colors=alist[i]
    return secondTaken



def catchSome(K,dogs):
    perm= combinations(dogs,K)
    alist=[timeTaken(i) for i in perm]
    
    return min(alist)


if __name__=="__main__":
    T=int(input())
    testCase=[]
    for _ in range(T):
        N,K=map(int, input().split())
        meters=list(map(int, input().split()))
        colors=list(map(int, input().split()))
        dogs=[(meters[i],colors[i]) for i in range(N)]
        testCase.append([K,dogs])
    for i in range(T):
        K,dogs= testCase[i]
        print("Case #"+str(i+1)+":",catchSome(K,dogs))
