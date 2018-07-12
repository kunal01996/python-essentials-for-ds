# Think of a recursive version of the function f(n) = 3 * n, i.e. the multiples of 3


# Recursive version
def fn_3(limit):
    if limit == 1:
        return 3
    else:
        return 3 + fn_3(limit - 1)


print(fn_3(10))


# Iterable version
sum = 3
for i in range(10, 1, -1):
    sum += 3

print(sum)