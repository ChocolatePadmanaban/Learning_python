import re
pat1 = re.compile('ba?b', re.IGNORECASE)
if pat1.search('BB'):
    print('It searched')
else:
    print('No Match')

#checking in multiline
greet = 'hello\nworld'
pat1 = re.compile('hello$',re.MULTILINE)
print(pat1.search(greet))
pat2 = re.compile('.+',re.DOTALL)
print(pat2.search(greet))

# splitting strings

p=re.compile(r'\W+')
print(p.split('This is a test, short and sweet, of split().'))
print(p.split('This is a test, short and sweet, of split().',3))

# Search and replace

p = re.compile('(blue|white|red)')
print(p.sub('colour','blue socks and red shoes'))
print(p.sub('colour','blue socks and red shoes',count=1))