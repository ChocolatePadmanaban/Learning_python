# convert list to matrix

def MatrixCreate(l,s):
    if s[0]*s[1] == len(l):
        answer = []
        for i in range(0,s[0]):
            answer1 = l[i*s[1]:(i+1)*s[1]]            
            answer.append(answer1)
        return answer
    else:
        return "Invalid Input"

print(MatrixCreate([11,-9,8,17,6,7],(3,2)))
