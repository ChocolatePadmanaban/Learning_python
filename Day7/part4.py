#matrix operations:
# 1.convert list to matrix
# 2.MatrixTranspose

def MatrixCreate(l,s):
    if s[0]*s[1] == len(l):
        answer = []
        for i in range(0,s[0]):
            answer1 = l[i*s[1]:(i+1)*s[1]]            
            answer.append(answer1)
        return answer
    else:
        return "Invalid Input"

def MatrixTranspose(M):
    m= len(M)
    n = len(M[0])
    answer = []
    for i in range(n):
        answer1 = []
        for j in range(m):
            answer1.append(M[j][i])
        answer.append(answer1)
    return answer


print(MatrixCreate([11,-9,8,17,6,7],(3,2)))
print(MatrixTranspose([[1,2,3],[4,5,6]]))

