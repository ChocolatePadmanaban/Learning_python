#https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
def FindRhyme(alienWords,word):
    indexi=alienWords.index(word)
    alienWords.remove(word)
    for j in alienWords:
        if word[-1:] == j[-1:]:
            rhymingWords=[word,j]
            alienWords.remove(j)
            return rhymingWords

    alienWords.insert(indexi,word)
    return []

def CountRhyme(alienWords):
    N=len(alienWords)
    rhymingWords=[]
    for i in range(N):
        try:
            rhymingWords+=FindRhyme(alienWords,alienWords[i])
        except:
            break
    print(set(rhymingWords))
    return len(set(rhymingWords))

def SolveRhyme(InputDictonary):
    for i in range(len(InputDictonary)):
        print("Case #"+str(i+1)+": "+str(CountRhyme(InputDictonary[i])))



if __name__ == "__main__":
    InputDictonary=[]
    for i in range(int(input())):
        N=int(input())
        temp=[]
        for j in range(N):
            temp.append(input())
        InputDictonary.append(temp)
    SolveRhyme(InputDictonary)