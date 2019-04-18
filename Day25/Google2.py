def RhymeRemover(Tescase, indexoftest):
    if len(Tescase)!=0:
        wordsCompination=[Tescase[indexoftest][i:] for i in range(Tescase[indexoftest])]
        Tescase.remove(wordsCompination[0])
        for i in wordsCompination:
            for j in Tescase:
                if i in j:
                    Tescase.remove(j)
                    return True
        Tescase.insert(indexoftest,wordsCompination[0])
        return False
        
def RhymeFinder(TestCase,RhymeCount=0):
    while 


T=int(input())
TestCases=[]
for i in range(T):
    N=int(input())
    Temp=[]
    for j in range(N):
        Temp.append(input())
    TestCases.append(Temp)


