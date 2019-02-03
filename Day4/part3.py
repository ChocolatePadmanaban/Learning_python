#iterators


#Iterating alist
a = iter(['some','list'])
print(next(a))
print(next(a))


#Iterating a set
b = iter(set([1,2,3,45,5,6,3,3,3,3,3,3,3,3,3,3,3222]))
print(next(b))
print(next(b))

#Itrrating a string
c = iter('pradeep is awesome')
print(next(c))
print(next(c))

# Iterating with while loop without condition
# def print_some(Iterable):
#     iterator =iter(Iterable)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration as e:
#             print(e)
#         else:
#             print(item)


