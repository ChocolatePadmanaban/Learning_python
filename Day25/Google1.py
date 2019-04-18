def NextCell(existingMartix,SafePath):
    r,c = SafePath[-1][0],SafePath[-1][1]
    for i in existingMartix:
        if (i[0]!=r)and(i[1]!=c)and(i[0]+i[1]!=r+c) and (i[0]-i[1]!=r-c):
            existingMartix.remove(i)
            SafePath.append(i)
            return existingMartix, SafePath
    return existingMartix, SafePath



def CreateMatrix(R,C):
    temp=[]
    for i in range(R):
        for j in range(C):
            temp.append([i+1,j+1])
    return temp

def FindRoute(R,C, casenumber):
    Workmatrix=CreateMatrix(R,C)
    TargetLength=len(Workmatrix)
    PrintTheFollowing=[]
    for i in Workmatrix:
        SafePath=[i]
        Workmatrix.remove(i)
        for j in range(TargetLength+2):
            Workmatrix, SafePath= NextCell(Workmatrix, SafePath)
        if len(SafePath)== TargetLength:
            PrintTheFollowing.append("Case #"+str(casenumber)+": POSSIBLE")
            for k in SafePath:
                PrintTheFollowing.append(k[0],k[1])
            return PrintTheFollowing
    PrintTheFollowing.append("Case #"+str(casenumber)+": IMPOSSIBLE")
    return PrintTheFollowing


    



T=int(input())
Testcase=[]
for i in range(T):
    R, C= input().split(' ')
    Testcase.append([int(R),int(C)])
for i in range(T):
    PrintTheFollowing=FindRoute(Testcase[i][0],Testcase[i][1],i+1)
    for j in PrintTheFollowing:
        print(j)


