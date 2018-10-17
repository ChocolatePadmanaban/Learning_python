# Classes

class Student:
    '''student class '''
    
    def __init__(self, n,a):
        '''for privacy add __ before variable names'''
        self.name = n
        self.age= a
        
    def get_age(self):
        return self.age
    

class child_student(Student):
    '''A subclass extending Student Class'''

    def __init__(self,n,a,s):
        '''initializing'''
        Student.__init__(self,n,a)
        self.section_num=s
    def get_age(self):
        print("Age: "+str(self.age))

c = child_student("Dinesh", 12, 2)
c.get_age()