def CheckNext(a1,GalaxyMatrix,startpoint,path,pathset):
    for i in a1:
        for j in i:
            if all([len(path)==len(pathset),GalaxyMatrix[j[0]-1][j[1]-1]==True,startpoint[0]!=j[0],startpoint[1]!=j[1],startpoint[0]+startpoint[1]!=j[0]+j[1],startpoint[0]-startpoint[1]!=j[0]-j[1]]):
                GalaxyMatrix[j[0]-1][j[1]-1] = False 
                path.append(j)
                pathset.add(j)
                CheckNext(a1,GalaxyMatrix,j,path,pathset)
    
def CheckPossible(a):
    a1=[[(i+1,j+1)  for j in range(a[1])] for i in range(a[0])]
    GalaxyMatrix=[[True for j in range(a[1])] for i in range(a[0])]
    startpoint=(1,1)
    path=[]
    pathset=set(path)
    CheckNext(a1,GalaxyMatrix,startpoint,path,pathset)
    if any([any(i) for i in GalaxyMatrix]):
        return ['IMPOSSIBLE']
    else:
        return ['POSSIBLE']+path

def PrintAnswer(a):
    for i in range(len(a)):
        temp=CheckPossible(a[i])
        if temp[0]=="IMPOSSIBLE":
            print('Case #'+str(i+1)+': IMPOSSIBLE')
        else:
            print('Case #'+str(i+1)+': POSSIBLE')
            for j in range(1,len(temp) ):
                print(temp[j][0],temp[j][1])

if __name__ == "__main__":
    a=[[int(j) for j in input().split()] for i in range(int(input()))]
    PrintAnswer(a)

