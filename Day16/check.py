dic = {'a':{'b':{'c':{'d':'e'}}}}
keys1=[]
values1 = []
condition = True
while condition:
    keys1.extend(list(dic.keys()))
    val = list(dic.values())
    for i in val:
        val = i
    if type(val) is dict:
        dic = val
    else:
        condition = False
        values1.append(val)
def fibo(n):
    a,b = 0,1
    li = []
    li.append(a)
    li.xtend(b)

if __name__ == "__main__":
    print(keys1,values1)