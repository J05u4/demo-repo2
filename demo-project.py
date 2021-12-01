import numpy as np

def fct1(a):
    r = a+7+2
    return min(r, 12)

print(fct1(3))

class base(object):
    def __init__(self, name):
        self.name = name

    def some_method(self, arg):
        self.arg = arg
        print("this should return some ", self.arg)
