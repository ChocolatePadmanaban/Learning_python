def FindOdd(ListProg):
    for i in range(len(ListProg[0])):
        if all([True if j in [k[i] for k in ListProg] else False for j in "RPS" ]):
            return None
        


if __name__=="__main__":
    T=int(input())
    Tornament=[]
    for i in range(T):
        Tornament.append([input() for j in range(int(input()))])
    print(Tornament)
