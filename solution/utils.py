"""
Autores: Tatan Rufino, para la Universidad de Sevilla
"""
def iterate(f, start=None):
    """ Yields start, f(start), f(f(start)), ... """
    next = start
    while True:
        yield next
        next =  f(next)

def first(iterable):
    """ Takes the first of iterable """
    for value in iterable:
        return value

NaN = float('nan')
class InfinityObj: pass
Infinity = InfinityObj()
