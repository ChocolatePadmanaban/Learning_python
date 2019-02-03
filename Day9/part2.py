#debugging a program part 2

import pdb
def f1(some_arg):
    some_other = some_arg+1
    print(some_other)
    myadd(some_arg, some_other)
    return f2(some_other)

def f2(some_arg):
    some_other = some_arg+1
    some_other = 2*(some_other+12)
    myadd(some_arg, some_other)
    some_other = some_other+some_arg
    print(some_other)
    return f3(some_other)

def f3(some_arg):
    some_other = some_arg+1
    print(some_other)
    return f4(some_other)

def f4(some_arg):
    some_other = some_arg+1
    some_other = 2*some_other -17
    some_arg = 3*(some_other+12)
    some_other = myarith(some_other,some_arg)
    print (some_other)
    return some_other

def myadd(x,y):
    print("x is ", x)
    print(x+y)
def myarith(x,y):
    x = 9/x + 1.8*y
    y= 7.8*(x/9 + 2.3*y)

pdb.run("f1(1)")

# s --> single stepping pdb command
# p --> print
# n --> single stepping without going into the function

# b --> breakpoint lsit
# b (breakpoint line no) -->  will include a break point at the line no
# c --> continue till first break point

# !some_other = .9 --> to change the value of variable via debugger
# disable (breakpoint no) -->  disable the breakpoint with breakpoint no
# clear (breakpoint no )--> delete the breakpoint with breakpoint no
# l --> see where you are
# j --> jump around go back again and execute form there
