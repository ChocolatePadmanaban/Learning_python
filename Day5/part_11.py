# Monostate Singleton(Single ton with different memory spaces)

class Borg:
    __shared_state ={"1":"2"}
    def __init__(self):
        self.x=1
        self.__dict___= self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x=4
print("Borg object b:", b)
print("Borg Object B2:", b1)
#different Memory addressed
print("Object state 'b':",b.__dict___)
print("object state 'b1':",b1.__dict___)
#but same state