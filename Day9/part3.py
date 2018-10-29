# illegal practices in debugging()
# # do not denug inside for  loop:
import pdb

def Hi():
    print("Hi")
    for i in range(7):
        print("Roses are red")
        print("Violets are blue")
        print("There is no one like you")

pdb.run('Hi()')
