# find a .c file and replace it with cpp

from glob import glob
from os import rename

def DoRename_1():
    g = glob('/home/cisco/Documents/Learning_python/Day21/*.c', recursive=False)
    for files in g:
        p= files.replace('.c','.cpp')
        rename(files, p)

if __name__ =="__main__":
    DoRename_1()
