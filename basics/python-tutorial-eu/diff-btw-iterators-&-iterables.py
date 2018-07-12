# Learning the difference iterables and iterators

# So what is the difference between an iterable and an iterator?
#
# In one perspective they are the same: You can iterate with a for loop over iterators and iterables.
# Every iterator is also an iterable, but not every iterable is an iterator. E.g. a list is iterable
# but a list is not an iterator! An iterator can be created from an iterable by using the function 'iter'.
# To make this possible the class of an object needs either a method '__iter__', which returns an iterator,
# or a '__getitem__' method with sequential indexes starting with 0.

cities = ["Berlin", "Vienna", "Zurich"]

iterable = iter(cities)

print(iterable.__next__())
print(iterable.__next__())

for i in range(len(cities)):
    try:
        print(iterable.__next__())
    except StopIteration:
        print('Exiting')
        break

