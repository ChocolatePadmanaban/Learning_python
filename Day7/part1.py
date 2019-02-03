# problem statement: check the values of answers and modle in 
#their respective csv file and print the score for which the answers match
# with special case of negative marking -1 for wrong answer


model = open("model.csv")
answer =open("answers.csv")
models = [i.split(',') for i in model.readlines()]
answers = [i.split(',') for i in answer.readlines()]
model.close()
answer.close()
scores = []
for i in range(len(models)):
    if models[i][1] == answers[i][1]:
        scores.append(1)
    elif models[i][1] == 'x\n':
        scores.append(0)
    else :
        scores.append(-1)
scores = sum(scores)
print(scores)