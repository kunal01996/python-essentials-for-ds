# Learning for-loop in python

edibles = ["ham", "spam", "eggs", "nuts"]

for food in edibles:
    if food == "spam":
        print("No more spam")
        break
else:
    print("I am glad i finished my food without any spam this time!")
print('I am stuffed!')

# Pythagorean triplets

from math import sqrt
n = int(input("Max num: "))

for a in range(1, n+1):
    for b in range(a, n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if c_square == c**2:
            print(a, b, c, end="\n")
