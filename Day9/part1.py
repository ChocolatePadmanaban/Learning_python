# Debugging pakage pdb


import pdb
def some_div(some_int):
    print("Start int", some_int)
    ret_int = 10/some_int
    print("End some int", some_int)
    return ret_int

pdb.run("some_div(2)")#will not say what the function returns
print(pdb.runeval("some_div(2)"))# will show what the function returns


