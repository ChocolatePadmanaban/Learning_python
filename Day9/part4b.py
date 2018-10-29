# unit testing functions

import part4
import unittest
class MathTest(unittest.TestCase):
    def testadd(self):
        self.assertTrue(part4.myadd(2,3)==5)
    def hello(self):# this function will not be executed
        return True
    def testsub(self):
        self.assertTrue(part4.mysub(3,2)==1)
    

if __name__ == "__main__":
    unittest.main()# creates objects for class with name ending in 'Test'
    # and in those classes it executes function with name starting with "test"

