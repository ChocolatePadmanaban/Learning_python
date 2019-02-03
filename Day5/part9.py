# Finally block in try catch

def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by Zero")
    else:
        print("result is ",result)
    finally:
        print("Exected Finally clause")
print(divide(1,0))
print("Hello")