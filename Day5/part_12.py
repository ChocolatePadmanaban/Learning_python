# Meta Classes(the classes whoes objects are also classes)

class MyInt(type):
    def __call__(cls,*args,**kwds):
        print("**************Here is My Int***************",args)
        print("Now do whatever ever you want with these objects")
        return type.__call__(cls,*args,**kwds )

class inti(metaclass= MyInt):
    def __init__(self,x,y):
        self.x=x
        self.y=y

i = inti(4,5)