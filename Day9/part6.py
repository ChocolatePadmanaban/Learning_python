# testing in doctest part 2
import doctest
class Myclass:
    pass

def myfunc(obj):
    """
    >>> myfunc(Myclass()) #doctest: +ELLIPSIS
    <__main__.Myclass object at 0x...>
    """

    return obj


if __name__ == '__main__':
    doctest.testmod(verbose=True)