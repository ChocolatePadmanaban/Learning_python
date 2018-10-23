# Decorators(Adding additional capablities to a function)

class myDecorators:
    def __init__(self,f):
        print("A logging in about to strat")
        f()
    def __call__(self):
        print("Done")

@myDecorators
def myfunct():
    print("The Function is called")
myfunct()