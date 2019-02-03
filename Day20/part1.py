# Unexpands functions()
def HighestSpace(a):
    i = 10
    while i>1:
        i-=1
        if i*' ' in a:
            return i
    return i

def Un_Expand(a):
    while HighestSpace(a)> 1:
        a = a.replace(HighestSpace(a)*' ',(HighestSpace(a)//2 + (HighestSpace(a)%2))*'\t')
    else:
        return a


if __name__ =='__main__':
    print(Un_Expand('lksajfdlksahfdklj   jdsflkajs;lkfdja    lkjfda lkjsf  '))
    print(Un_Expand('lksajfdlksahfdklj   jdsflkajs;lkfdja    lkjfda lkjsf  ')==
    'lksajfdlksahfdklj\t\tjdsflkajs;lkfdja\t\tlkjfda lkjsf\t')