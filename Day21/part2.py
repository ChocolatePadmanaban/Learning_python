#Get Variables of a class

class Student():
    __Grade = 'S'
    def __init__(self,name= 'Pradeep', rollno= 110112062, sec= 'ICE'):
        self.Name = name
        self.Rollno = rollno
        self.Sec= sec
    def getGrade(self):
        return self.__Grade
def GetVaribles(Class_1):
    a = Class_1()
    c1=  set(['__class__', '__delattr__', '__dict__', '__dir__','__doc__',
     '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
      '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
       '__ne__',
       '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
        '__sizeof__', '__str__', '__subclasshook__', '__weakref__'])
    b1 = set(dir(a))- c1
    print(b1)
    gets = []
    for i in  b1:
        if '_Student__' in i:
            gets.append(i.replace('_Student__',''))
    print(gets)
    d1 = {}
    for i in gets:
        d1[i]=a.__getattribute__('get'+i)()
    print(d1)


if __name__ == "__main__":
    a = Student()
    GetVaribles(Student)