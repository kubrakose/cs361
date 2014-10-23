__author__ = 'fsebile'

def fib(n):
    print '2'
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)