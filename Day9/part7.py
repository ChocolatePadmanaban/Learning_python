# test objects using unittest

import unittest
class Student:
    pass
s1 = Student()
class StuTest(unittest.TestCase):
    def teststu(self):
        self.assertIsInstance(s1, Student)
unittest.main()