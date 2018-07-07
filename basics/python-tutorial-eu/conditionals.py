# Learning conditionals in python

age = int(input("Please enter your age: "))

print()

if age < 1:
    print('This could be hardly true!')
elif age == 1:
    print('About 14 human years!')
elif age == 2:
    print('About 22 years human years!')
elif age > 2:
    human = 22 + (age - 2)*5
    print('Human years: ', human)

###

input('Press return>')


# The ternary if

num = int(input('please enter a number'))
max = num if num > 20 else 5

print(max)
