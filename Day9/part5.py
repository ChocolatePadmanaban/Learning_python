# doc Testing
import doctest
def my_function(a,b):
    """
    >>> my_function(3,2)
    6
    >>> my_function('a',2)
    'aa'
    """
    return a*b

    #python -m doctest -v part5.py

    # or
if __name__ =="__main__":
    doctest.testmod(verbose=True)


