#importing classes form part3 
from copy import deepcopy
from part3 import Student
stu1 = Student("Pradeep", 22)
stu2 = Student("Ezhil", 32)
stu3 = deepcopy(stu1)
print(stu1.get_name() + "'s age is", stu1.get_age())
print(stu2.get_name() + "'s age is", stu2.get_age())
stu1.inc_age(3)
print(stu1.get_name() + "'s age is", stu1.get_age())
print(stu2.get_name() + "'s age is", stu2.get_age())
print(stu3.get_name() + "'s age is", stu3.get_age())