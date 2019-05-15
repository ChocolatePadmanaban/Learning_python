def Bayes():
    dicta={.2:.2,.4:.4,.6:.2,.8:.2}
    lista=[]
    for i in dicta.keys():
        temp=88.37669683257919*dicta[i]*(i**4)*(1-i)**2
        print(temp)
        lista.append(temp)
    print(sum(lista))
    print(lista)
    dictb=dict(zip(list(dicta.keys()),lista))
    meana=0
    for i in dictb.keys():
        meana+=i*dictb[i]
    print(meana)
    


if __name__=="__main__":
    Bayes()