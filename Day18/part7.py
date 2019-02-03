from client import SimpleObject, client
import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):
        name = "Pradeep Padmanaban"
        check = client(name)
        self.assertTrue(name.upper()== check) 
  
if __name__ == '__main__': 
    unittest.main() 
