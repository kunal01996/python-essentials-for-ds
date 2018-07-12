# Learning functions in python


def fahrenheit(C):
    """
    Converting celsius to fahrenheit
    :param C:
    :return:
    """
    return (C * 9 / 5) + 32


vals = map(fahrenheit, (22.6, 25.8, 27.3, 29.8))
print(set(vals))

# Optional parameters


def wish(name="everyone"):
    """
    Wish greeting
    :param name:
    :return None:
    """
    print("Good evening, {}".format(name))


wish("Peter")
wish()


# Using Docstring
print(wish.__doc__)

# Keyword Parameters


def subsum(a, b, c=0, d=10):
    """
    Having some testing with keyword parameters
    :param a:
    :param b:
    :param c:
    :param d:
    :return None:
    """
    print(f"a : {a}, b : {b}, c : {c}, d: {d}")


subsum(1, 34, d=10)


# Returning values in function


def no_return(x, y):
    c = x + y


print(no_return(2, 3))


# Returning multiple values from a function
def fib_intervall(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    (old, new, lub) = (0, 1, 0)
    while True:
        if new < x:
            lub = new
            (old, new) = (new, old + new)
        else:
            return (lub, new)


while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))


# Local and global variables in python

# To make a local variable defined inside of a function use the keyword global
def f():
    """
    Using the global keyword
    :return:
    """
    global s
    s = "cat"

f()
print(s)


# Arbitrary number of parameters
def arithmetic_mean(first, *values):
    """
    Calling for arbitrary values
    :param first:
    :param values:
    :return:
    """
    return (first + sum(values)) / (1 + len(values))


print(arithmetic_mean(1, 2, 3, 4, 5, 6))


# Arbitrary number of arguments

def fn(**kwargs):
    """
    Using kwargs
    :param kwargs:
    :return:
    """
    print(kwargs)


fn(de="German",en="English",fr="French")


def fnc(a, b, c, d):
    print(a, b, c, d)


d = {'a':'append', 'b':'block','c':'extract','d':'yes'}
fnc(**d)
