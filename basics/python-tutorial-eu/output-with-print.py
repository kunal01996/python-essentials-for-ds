# Output with print()

# "print" is - as we have already mentioned - a function in version 3.x.
# Like any other function print expects its arguments to be surrounded by parentheses.
# So parenthesis are an easy remedy for this error.

# print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Printing the stars

for i in range(1, 10):
    for k in range(10, i, -1):
        print(end=" ")
    for j in range(1, i):
        print("*", end=" ")
    print()

for i in range(1, 9):
    for j in range(1, i):
        print(end=" ")
    for k in range(9, i, -1):
        print(" ", end="*")
    print()


# Writing to the error file
fh = open("data.txt", 'w')
print("42 is the answer, and i am writing it to!", file=fh)