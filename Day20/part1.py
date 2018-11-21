# Unexpands functions


def HighestSpace(a):
    space, i = 2,2
    while i< 10:
        i-=1
        if i*' ' in a:
            return i

def Un_Expand(a):
    while HighestSpace(a)>= 1:
        a = a.replace(HighestSpace(a)*' ',(HighestSpace(a)//2 + (HighestSpace(a)%2))*'\t')
    else:
        return a


if __name__ =='__main__':
    print(Un_Expand('lksajfdlksahfdklj   jdsflkajs;lkfdja    lkjfda lkjsf  '))
    print(Un_Expand('lksajfdlksahfdklj   jdsflkajs;lkfdja    lkjfda lkjsf  ')==
    'lksajfdlksahfdklj\t\tjdsflkajs;lkfdja\t\tlkjfda lkjsf\t')