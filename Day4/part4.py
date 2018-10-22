# Editing Builtin Functions in Iterators

class BoundedRepeater:
    def __init__(self, v, uplim):
        self.value = v
        self.limit = uplim
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>= self.limit:
            raise StopIteration
        self.count += 1
        return self.value
br1 = BoundedRepeater('hello',4)

while True:
    try:
        print(next(br1))
    except:
        print('Done')
        break