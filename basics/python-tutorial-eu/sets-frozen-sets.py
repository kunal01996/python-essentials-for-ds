# Learning Sets and Frozen sets in python

# Sets

# The data type "set", which is a collection type, has been part of Python since version 2.4.
# A set contains an unordered collection of unique and immutable objects.
# The set data type is, as the name implies, a Python implementation of the sets
# as they are known from mathematics. This explains, why sets unlike lists
# or tuples can't have multiple occurrences of the same element.

first_set = set([(1, 2, 3)])
print(first_set)

cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))

print(cities)

# Frozen sets
# Though sets can contain only immutable objects as there elements
cities.add("Samburg")
print(cities)

cities = frozenset(["Incheon", "Frankfurt", "Orlando", "New Jersey"])
# cities.add("James")
print(type(cities))

# SET operations

# ADD Operation
colors = {'red', 'green'}
colors.add('blue')
print(colors)

# Cleaning the SET
colors.clear()
print(colors)

# Making a shallow copy
more_cities = {"Winterthur", "Schaffhausen", "St. Gallen"}
backup_cities = more_cities.copy()
more_cities.clear()
print(more_cities)
print(backup_cities)

# Difference
X = {"a", "b", "c", "d"}
Y = {"c", "d", "e"}
Z = {"a", "m", "n"}

print(X - Y - Z) # alternative X.difference(Y).difference(Z)

X = {"a", "b", "c", "d"}
X.difference_update(Y)
print(X)

# Removing an element from a set
X.discard("b")
print(X)

# Using remove, but remove will generate an error in case the element does not exist
# X.remove("b")

# UNION
x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
z = x | y # Alternatively use .union(set object) to do UNION
print(z)

# INTERSECTION
z = x & y # Alternativey use .intersection(set object) to do INTERSECTION
print(z)

# Checking if the sets are DISJOINT
print(x.isdisjoint(y))

# Checking SUBSET
print(x.issubset(x.union(y)))

# Checking SUPERSET
print(x.issuperset({"a"}))

# Removing an arbitrary element from the SET
print(x.pop())

# Looping through the SET
for e in x.intersection(y):
    print(e)
