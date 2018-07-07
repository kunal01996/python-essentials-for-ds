# Formatting in python

from math import sqrt

print("Art: %5d, Price is %8.2f" %(432, 345.69))
print("Art: {a:<5d}, Price is {b:<8.2f}".format(a=432, b=3456.7967))


def print_sqrts(start, end):
    """
    Printing pretty formatted strings
    :param start:
    :param end:
    :return None:
    """
    for i in range(start, end+1):
        print("Square root of {0} is {1:<5.2}".format(i, sqrt(i)))

    return None


print_sqrts(start=1, end=10)
print(print_sqrts.__doc__)

# This option signals the use of a comma for a thousands separator.
print("{0:,}".format(456789012))

# a, b, *_ = (1, 2, 3, 8, 4, 5, 6)
# print(_)

# String methods used for formatting

# 1. center()
s = "Python"
print(s.center(10, "*"))

# 2. ljust()
print(s.ljust(10, "#"))

# 3. rjust()
print(s.rjust(10, "^"))

# 4. zfill() is same as rjust()
print(s.zfill(10))

# Formatted String literals

price = 12.234
print(f"The price is {price*2:5.6f}")
