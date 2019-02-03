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
    def testnotadd(self):
        return self.assertNotAlmostEqual(part4.myadd(3,2),6)
    

if __name__ == "__main__":
    #unittest.main()# creates objects for class with name ending in 'Test'
    # and in those classes it executes function with name starting with "test"
    suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #gives full details with
    print(dir(unittest.TestCase))


