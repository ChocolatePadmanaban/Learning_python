# data vs Class Attributes

class counter:
    overall_total = 0
        # class attribute
    def __init__ (self):
        self.mytotal = 0
        # data attribute
    def increment(self):
        counter.overall_total +=1
        self.mytotal +=1

a = counter()
b = counter()

a.increment()
b.increment()
b.increment()

print("A's total ", a.mytotal)
print("Over all total",a.__class__.overall_total)
print("B's total ", b.mytotal)
print("Over all total",b.__class__.overall_total)
