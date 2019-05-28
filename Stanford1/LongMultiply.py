def OneAdd(a,b):
    addlen=min(len(a),len(b))
    a,b=a[::-1],b[::-1]
    temp=0
    c=''
    for i in range(addlen):
        d=str(int(a[i])+int(b[i])+temp)
        c=d[-1:]+c
        temp=0
        if int(d)>9:
            temp=int(d[:-1])
    if len(a)>len(b):
        temp= temp+int(a[:addlen-1:-1])
        
    elif len(a)<len(b):
        temp= temp+int(b[:addlen-1:-1])
    
    c=str(temp)+c
    return c



def OneMultiply(a,b):
    a=a[::-1]
    temp=0
    c=[]
    for i in a:
        d=str(int(i)*int(b)+temp)
        c.append(d[-1:])
        if int(d)>9:
            temp=int(d[:-1])
    c.append(str(temp)[::-1])
    a=a[::-1]
    return ''.join(c[::-1])

def longMultiply(a,b):
    c =[OneMultiply(a,i)  for i in b]
    c=c[::-1]
    c=[c[i]+('0'*i) for i in range(len(c))]
   
    d=c[0]
   
    for i in range(1,len(c)):
        
        d = OneAdd(d,c[i])
        

    print(d)


if __name__=="__main__":
    print(OneMultiply("84","2"))
    longMultiply('899999487587657865765765765765765765786578657865786587657657','26787698768976897698769876987687687698768976897890')

