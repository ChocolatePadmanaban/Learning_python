#

import re

pat1 = re.compile('^(\+91|\+44)?[0-9]{10}$')
cell = input("Enter your cell number ")
if pat1.search(cell):
    print("It matched")
else:
    print('It did not match')

country = re.compile('(in|jp|uk)$')
read_country  = input("Enter a Country Code ")
if country.search(read_country):
    print("It matched")
else:
    print('It did not match')

p = re.compile('\d+')
A = p.findall('129879879879879878798 drummers drumming , 11 pipers piping, 10 lords a-leaping')
print(A)