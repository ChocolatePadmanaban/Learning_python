# Closure(using functions as decorators)

def entryExit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f


@entryExit
def add_():
    print(5+12)

add_()
