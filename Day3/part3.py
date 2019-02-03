#defing Classes

class Student:
    '''student class '''
    total = 0
    def __init__(self, n,a):
        '''for privacy add __ before variable names'''
        self.__name = n
        '''exceptoin is  added with intention'''
        try:
            if a<0:
                raise Exception(a,n)
            else:
                self.__age = a
        except Exception as inst:
            print('Negative age', inst.args)
            self.__age= 0
        self.__class__.total += 1
        self.__roll = self.__class__.total
        #print("Hello")
        '''we cannnat access without getters'''

    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def inc_age(self,n):
        self.__age += n
    def get_roll(self):
        return self.__roll
    def __repr__(self):
        return "An object of class student"
    def __gt__(self,other):
        return self.__age > other.get_age()

