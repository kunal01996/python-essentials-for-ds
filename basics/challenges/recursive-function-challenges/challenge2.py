# Write a recursive Python function that returns the sum of the first n integers.
# (Hint: The function will be similar to the factorial function!)


def arithmetic_sum(limit):
    """
    An arithmetic sum using recursion
    :param limit:
    :return:
    """
    if limit == 1:
        return 1
    else:
        return limit + arithmetic_sum(limit-1)


print(arithmetic_sum(10))

# Iterative version of the recursive function

sum = 0

for i in range(1, 11):
    sum += i

print(sum)