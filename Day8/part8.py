#difference between multiprocessing and multithreading
# multithreading has same data here and multiprocessing has copied data

import _thread
import time
x =0
def inc_x(inc):
    global x
    x = x+inc
    print(x)
def print_x(val):
    global x
    print(x +val)

_thread.start_new_thread(inc_x,(8,))
_thread.start_new_thread(print_x,(5,))
while True:
    pass