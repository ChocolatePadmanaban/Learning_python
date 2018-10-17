# Classes

class Student:
    '''student class '''
    def __init__(self, n,a):
        '''for privacy add __ before variable names'''
        self.__name = n
        self.__age= a
        print("Hello")
        '''we cannnat access without getters'''

    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def inc_age(self,n):
        self.__age += n
    


