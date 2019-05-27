from itertools import *
import sys
def SkillHour(S):
    maxHour=max(S)
    alist = [maxHour-i for i in S]
    return sum(alist)

def training(N,P,S):
    comb= combinations(S,P)
    alist= [SkillHour(i) for i in comb]
    sys.stdout.flush()
    return min(alist)



if __name__=="__main__":
    T=int(input())
    alist=[]
    for i in range(T):
        N,P=map(int,input().split())
        S=map(int,input().split())
        alist.append([N,P,S])
    for i in range(T):
        print("Case #"+str(i+1)+":",training(alist[i][0],alist[i][1],alist[i][2]))

