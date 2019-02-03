#test assignment


a = 'A man, a plan, a canal; panama'
def CheckPalindrome(l):
    l= l.replace(',','').replace(';','').replace(' ','').strip().upper()
    x = (lambda y :all([l[i]==l[len(l)-i-1] for i in range(len(l))])) 
    return x(l)

def RevserseWord(l):
    l=l.strip().split(' ')
    x = (lambda y : [l[len(l)-i-1] for i in range(len(l))])
    l = ' '.join(x(l))
    return l

def RevserseChar(l):
    l = l.strip().split(' ')
    
    x = (lambda l: [l[i][::-1] for i in range(len(l))])
    l = x(l)
    for i in range(len(l)):
        if not l[i][0].isalpha():
            c1 = l[i][0]
            l[i] = l[i].replace(c1,'')+str(c1)
    return ' '.join(l)

def Cycle13(l):
    l = list(l)
    for i in range(len(l)):
        if l[i].isalpha():
            if l[i]>= 'a':
                l[i]=chr((ord(l[i]) +13-97)%26+97)
            else:
                l[i]=chr((ord(l[i]) +13-ord('A'))%26+ord('A'))
    return ''.join(l)



if __name__ == "__main__":
    print("The given string is a palindrome: ",CheckPalindrome(a))
    print('\nThe reversed string is :\n', RevserseWord(a))
    print("\nThe string with reversed words\n", RevserseChar(a))
    print("\nThe string cycled\n",Cycle13(a))
