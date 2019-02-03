# milti dimenstional list straighting


A= [[1,2],[2,[5,6]],3]
def Extract(a):
    b = []
    for i in a:
        if type(i) == list:
            b = b+ Extract(i)
        else:
            b.append(i)
    return b

print(Extract(A))