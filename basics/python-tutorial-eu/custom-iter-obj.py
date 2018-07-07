# Creating custom iter Obj


class Reverse:
    """
    A class to reverse an iterable e.g List, Tuple, String
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]


lst = [44, 34, 54]
reverse_list = Reverse(lst)

for el in reverse_list:
    print(el)

