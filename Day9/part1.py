# Debugging pakage pdb


import pdb
def some_div(some_int):
    print("Start int", some_int)
    ret_int = 10/some_int
    print("End some int", some_int)
    return ret_int


#different ways of calling debugger
pdb.run("some_div(2)")#will not say what the function returns
print(pdb.runeval("some_div(2)")) # will show what the function returns

print(pdb.runcall(some_div,2 ))# will run same as runeval but should pass as function, parameter list
# pdb commands c

if __name__ == "__main__":
    try:
        some_div(0)
    except:
        import sys
        tb = sys.exc_info()[2]#exception info

        pdb.post_mortem(tb)# returns exception info in pdp prompt



