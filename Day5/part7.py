# Reding number of lines in a file an application of Else block in try catch

import sys

for arg in sys.argv[1:]:
    try:
        f=open(arg,'r')
    except IOError:
        print("Cannot open the file: ", arg)
    else:
        print(arg, "has", len(f.readlines()), 'lines')
        f.close()

# Execute python part7.py myfile.txt myfile1.txt