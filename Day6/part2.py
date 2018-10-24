model = open("model.csv")
answer =open("answers.csv")
models = [i.split(',') for i in model.readlines()]
answers = [i.split(',') for i in answer.readlines()]
model.close()
answer.close()
score = map(lambda x, y: x[1] == y[1], models, answers) 
scores = list(filter(lambda x: x==True,score))
print(len(scores))