#manupulating error statement with python on linux

import os
import sys
divisor = int(input(" "))
dividend = int(input(" "))

fd = os.open("allers.txt",os.O_CREAT|os.O_WRONLY)
os.dup2(fd,2)
if dividend == 0:
    sys.stderr.write("cant divide by zero")

os.close(fd)