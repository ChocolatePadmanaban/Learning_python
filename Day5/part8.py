# Defining your own exception and impportance of raise

class MyExcept(Exception):
    def __init__(self):
        return
    def __str__(self):
        print("My Except Occured")
def myfunc():
    raise MyExcept

try:
    myfunc()
except:
    print("Caught an exception")
    raise
finally:
    print("Printed Finnally")

print("Print")
