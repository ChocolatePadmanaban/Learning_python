# milti dimenstional element finding(find the location of first occurance)


A= [[1,2],[2,[5,6]],3]
def Extract(a, e):
    for i in a:
        b = [a.index(i)]
        if i == e:
            print(i)
            break
        elif type(i) == list and Extract(i,e) != None:
            c = Extract(i,e)
            b = b + Extract(i,e)
        else:
            break
    return b

print(Extract(A, 1))