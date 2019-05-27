
def FindNext(R,C,Sr,Sc,W,thegrid):
    if W=='N':
        agrid=[i[0] for i in thegrid if (i[0]<Sr)and(i[1]==Sc)]
        if agrid==[]:
            return Sr-1,Sc 
        else:
            bgrid=[i for i in range(1,max(agrid)+1) if i not in agrid]
            return max(bgrid),Sc
    elif W=='S':
        agrid=[i[0] for i in thegrid if (i[0]>Sr)and(i[1]==Sc)]
        if agrid==[]:
            return Sr+1,Sc 
        else:
            bgrid=[i for i in range(min(agrid),R+1) if i not in agrid]
            return min(bgrid),Sc
    elif W=='E':
        agrid=[i[1] for i in thegrid if (i[0]==Sr)and(i[1]>Sc)]
        if agrid==[]:
            return Sr,Sc+1 
        else:
            bgrid=[i for i in range(min(agrid),C+1) if i not in agrid]
            return Sr,min(bgrid)
    elif W=='W':
        agrid=[i[1] for i in thegrid if (i[0]==Sr)and(i[1]<Sc)]
        if agrid==[]:
            return Sr,Sc-1 
        else:
            bgrid=[i for i in range(1,max(agrid)) if i not in agrid]
            return Sr,max(bgrid)

def wiggleWalk(R,C,Sr,Sc,ThePath):
    thegrid=[]
    thegrid.append((Sr,Sc))
    for W in ThePath:
        Sr,Sc=FindNext(R,C,Sr,Sc,W,thegrid)
        
        thegrid.append((Sr,Sc))
    #sys.stdout.flush()
    return Sr,Sc



if __name__=="__main__":
    T=int(input())
    Testcase=[]
    for _ in  range(T):
        N,R,C,Sr,Sc=map(int,input().split())
        ThePath=input()
        Testcase.append([R,C,Sr,Sc,ThePath])
    for k in range(T):
        R,C,Sr,Sc,ThePath=Testcase[k]
        Testcase[k]=wiggleWalk(R,C,Sr,Sc,ThePath)
        print('Case #'+str(k+1)+': '+str(Testcase[k][0])+' '+str(Testcase[k][1]))

