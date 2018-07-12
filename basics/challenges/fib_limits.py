# Fibonnaci limits for an input


def fib_limit(ipt):
    """
    Calculating upper and lower fibonnaci limits
    :param ipt:
    :return:
    """

    a, b = 0, 1

    while True:
        a, b = b, a + b

        if a <= ipt <= b:
            return a, b


print(fib_limit(44))