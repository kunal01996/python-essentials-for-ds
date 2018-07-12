# Creating a fibonacci series


def fib(limit):
    """
    A fibonnaci series
    :param limit:
    :return:
    """

    counter = 0
    a, b = 0, 1
    output_list = []

    while counter != limit:
        output_list.append(a)
        a, b = b, a + b
        counter += 1

    return output_list


print(fib(20))
