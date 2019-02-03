#Exception Handling
import sys

while True:
    try:
        x = int(input("Please Enter a number:"))
        break
    except ValueError:
        print("Ooops! that was not valid number")

try:
    f=open('myfile.txt'); s=f.readline()
    i = int(s.strip())
    f.close()
except FileNotFoundError:
    print('No such file')
except ValueError:
    print("Not a number")
except:
    print("Unexpected error: ",sys.exc_info()[0])
    raise


def divide():
    x = int(input("Enter divisor"))
    y = int(input('Enter the divisor'))
    return y/x

try:
    print(divide())
except:
    print(sys.exc_info()[0])