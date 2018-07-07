# Learning loops in python

n, sum = 1, 0

while n <= 100:
    sum += n
    n += 1

print('The sum is : {:d}'.format(sum))

#  Normally, the keyboard serves as the standard input. The standard output is usually the
# terminal or console where the script had been started, which prints the output.
# A script is supposed to send its error messages to the standard error.
# Python has these three channels as well:
#
#     standard input
#     standard output
#     standard error

# They are contained in the module sys. Their names are:
#
#     sys.stdin
#     sys.stdout
#     sys.stderror

import sys

text = ""

while 1:
    c = sys.stdin.read(1)
    text = text + c
    if c == "\n":
        break

print(text)


# Using the while...else statements

import random

num_from_user = int(input('Please enter a number between 1 to 20: '))
flag = True

while flag:
    if num_from_user == random.randint(1, 21):
        flag = False
    elif num_from_user == 0:
        print("Sorry that you're giving up!")
        break
    else:
        num_from_user = int(input('Please enter a number between 1 to 20, or to quit press 0 and return: '))
else:
    print('Congratulations, you finished the game!')


