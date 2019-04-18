def UniquePath(P):
    UniqueP=[]
    for i in list(P):
        if i=='S':
            UniqueP.append('E')
        else:
            UniqueP.append('S')
    return ''.join(UniqueP)

def UniquePathList(LydiaPath):
    for i in range(len(LydiaPath)):
        A = UniquePath(LydiaPath[i][1])
        print("Case #"+str(i+1)+': '+A)

numberOfTestCase=int(input())
LydiaPath=[]
for i in range(numberOfTestCase):
    size=int(input())
    path=input()
    LydiaPath.append([size,path])
UniquePathList(LydiaPath)
