import os
import time
import sys
r, w = os.pipe()
pid = os.fork()



if pid:
    time.sleep(5)
    os.close(w)
    r = os.fdopen(r)
    print("Parent reading")
    mstr = r.read()
    print("Text =", mstr)
    sys.exit()
else:
    os.close(r)
    w = os.fdopen(w,'w')
    print("Child writing")
    w.write("Text written by Child")
    w.close()
    print("Child closing")
    sys.exit(0)