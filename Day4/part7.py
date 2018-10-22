# Generators


def func_a():
    return "a"
def gen_a():
    yield 'a'
    yield 'b'
    yield 'c'


print(func_a())
print(next(gen_a()))
print(next(gen_a()))
print(next(gen_a()))
print(next(gen_a()))