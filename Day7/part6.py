# Get 100 inputs at a time from file
import os
fname = input("Enter your First  Name \n")
lname = input("Enter your last name \n")
print("Your First name is ", fname)
print("Your Last name is ", lname)

# in Terminal type python part6.py < names.txt


files = os.system("ls")
print(files)