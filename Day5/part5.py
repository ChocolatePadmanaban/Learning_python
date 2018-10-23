# Else statement in try catch block

import sys

try:
    f=open("myfile.txt")
    val= int(f.read().strip())
except FileNotFoundError:
    print("No such File")
except ValueError:
    print("Not a number")
except:
    print(sys.exc_info()[0])
    raise
else:
    res = 6+val
    print("res is", res)
    f.close()