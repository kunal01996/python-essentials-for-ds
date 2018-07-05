# Learning Sequential data types

# Python provides for six sequence (or sequential) data types:
# 1. strings
# 2. byte sequences
# 3. byte arrays
# 4. lists
# 5. tuples
# 6. range objects

# Learning Lists in python

# The main properties of Python lists:
# 1. They are ordered
# 2. The contain arbitrary objects
# 3. Elements of a list can be accessed by an index
# 4. They are arbitrarily nestable, i.e. they can contain other lists as sublists
# 5. Variable size
# 6. They are mutable, i.e. the elements of a list can be changed

empty_list = []
integer_list = [1, 2, 3]
string_list = ['parrot', 'hen', 'peacock']
mixed_list = ['Kunal', 21, 'Student']
nested_list = [12, [34, [45, 56]], 'Some more coming']

print(empty_list)
print(integer_list)
print(string_list)
print(mixed_list)
print(nested_list)

# A tuple is an immutable list, i.e. a tuple cannot be changed in any way once it has been created.
# Where is the benefit of tuples?
# 1. Tuples are faster than lists.
# 2. If you know that some data doesn't have to be changed, you should use tuples instead of lists,
#       because this protects your data against accidental changes.
# 3. The main advantage of tuples consists in the fact that tuples can be used as keys in dictionaries,
#       while lists can't.

first_tuple = (1, 'This is some value', 2)
print(first_tuple)

# Slicing in sequesntial data types

my_string = "Python is great"
print(my_string[0:])
print(my_string[0:-5])
print(my_string[::-1])
print(mixed_list[::-1])
print(first_tuple[::-1])
print(my_string[:-9])
print(my_string[::3])

another_string = "TPoyrtohnotno  ciosu rtshees  lianr gTeosrto nCtiot yb yi nB oCdaennasdeao"

print(another_string[::2])

s = "Toronto is the largest City in Canada"
t = "Python courses in Toronto by Bodenseo"
s = "".join(["".join(x) for x in zip(s, t)])
print(s)

# Finding out the length of sequence
print(len(mixed_list))
print(len(s))

master_list = []
master_list += mixed_list + integer_list
print(master_list)

# Checking if an element already exists in a sequence

print(2 not in master_list)

# Repeating elements of a sequence using the * operator
print(3 * master_list)

multiple_list = [[]]*3
print(multiple_list)

x = ["a", "b", "c"]
y = [x] * 4
y[0][0] = "p"
print(y)
