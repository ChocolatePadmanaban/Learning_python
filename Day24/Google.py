def NoFourSplit(N):
    listN=list(str(N))
    A= []
    B= []
    for i in listN:
        if i=='4':
            A.append('2')
            B.append('2')
        else:
            A.append(i)
            B.append('0')
    return ''.join(A), str(int(''.join(B)))
def NoFourSplitList(N):
    for i in range(len(N)):
        A, B = NoFourSplit(N[i])
        print("Case #"+str(i+1)+': '+A+' '+B)


numberOfTestCases= int(input())
N=[input() for i in range(numberOfTestCases)]
NoFourSplitList(N)



