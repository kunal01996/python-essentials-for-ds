# Learning recursive functions in Python


def factorial(limit):
    """
    Printing factorial using recursive functions
    :param limti:
    :return:
    """

    if limit == 0:
        return 1
    else:
        return limit * factorial(limit - 1)


print(factorial(10))


# Fibonnaci series using recursive functions
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1


def recursive_fib(limit):
    if limit == 0:
        return 0
    elif limit == 1:
        return 1
    else:
        return recursive_fib(limit - 1) + recursive_fib(limit - 2)


print(recursive_fib(10))

