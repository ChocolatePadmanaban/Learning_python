#implementing Singleton Object (only one instance of a class is present at anytime. eg president of a country)

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance= super(Singleton,cls).__new__(cls)
        return cls.instance


s1= Singleton()
s2 = Singleton()

print(s1==s2)
# same
class Someclass():
    def __init__(self):
        self.a = 0

s3=Someclass()
s4= Someclass()
print(s3==s4)
#different