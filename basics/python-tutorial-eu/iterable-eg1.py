def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


for i in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
    print(i, "iterable: ", iterable(i))

