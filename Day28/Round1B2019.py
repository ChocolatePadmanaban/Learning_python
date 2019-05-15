from itertools import combinations

def Possiblities(Q,person):
    r,c, d =person.split()
    r,c=int(r),int(c)
    if d=='N':
        return set([(i,j) for i in range(Q+1) for j in range(c+1,Q+1)])
    if d=='S':
        return set([(i,j) for i in range(Q+1) for j in range(c)])
    if d=='W':
        return set([(i,j) for i in range(r) for j in range(Q+1)])
    if d=='E':
        return set([(i,j) for i in range(r+1,Q+1) for j in range(Q+1)])
def cartLochigh(Q,personList,r):
    comb=list(combinations(personList,r))
    for subPersonList in comb:
        cartlocations=Possiblities(Q,subPersonList[0])
        if len(subPersonList)>1:
            for i in range(1,len(subPersonList)):
                cartlocations= cartlocations & Possiblities(Q,subPersonList[i])
        minX,minY=Q+1,Q+1
        for i in cartlocations:
            minX=min(minX,i[0])
        for i in cartlocations:
            if i[0]==minX:
                minY=min(minY,i[1])
        if (minX!=Q+1)and(minY!=Q+1):
            return minX,minY
    return cartLochigh(Q,personList,r-1)

def printAnswer(persondict):
    for i in persondict.keys():
        x,y= cartLochigh(persondict[i][0],persondict[i][1],len(persondict[i][1]))
        print("Case #"+str(i+1)+':',x,y)


if __name__=='__main__':
    persondict={}
    for i in range(int(input())):
        person, Q = map(int, input().split())
        personList=[input() for j in range(person)]
        persondict[i]=[Q,personList]
    printAnswer(persondict)