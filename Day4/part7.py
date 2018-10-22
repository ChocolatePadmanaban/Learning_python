# Generators


def func_a():
    return "a"
def gen_a():
    yield 'a'
    yield 'b'
    yield 'c'


print(func_a())
a = gen_a()
print(next(a))
print(next(a))
print(next(a))

# Generators in file:

def BeerData():
    f = open('recipeData.csv')
    for line in f:
        yield line
beer = BeerData()
print(next(beer))
print(next(beer))

lines= (line for line in open('recipeData.csv'))
print(next(lines))
cols = (l.split(',') for l in lines)
colums = next(cols)
beerdicts = (dict(zip(colums,data)) for data in cols)
print(next(beerdicts))



# Difference between Function and Genrator

lc = [n**2 for n in [1,2,3,4,5]]
ge = (n**2 for n in [1,2,3,4,5])

print(lc)
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))