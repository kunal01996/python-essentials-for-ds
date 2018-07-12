# function to calculate factorial

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

# function to calculate combination

def combination(n, r):
    """
    Combination
    :param n:
    :param r:
    :return:
    """
    return factorial(n)//(factorial(n -r)*factorial(r))


# Write a function which implements the Pascal's triangle


def pascals_triangle():
    """
    Printing pascals triangle
    :return:
    """

    for i in range(0, 5):
        for k in range(5, i, -1):
            print(end="  ")
        for j in range(0, i+1):
            print(combination(i, j), end="  ")
        print()


pascals_triangle()

