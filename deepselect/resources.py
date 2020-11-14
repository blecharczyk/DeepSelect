import numpy as np


class Resources:
    def __init__(self, names, amounts):
        assert (len(names) == len(amounts))

        self.names = names
        self.amounts = np.array(amounts, dtype=np.int32)

    def __len__(self):
        return len(self.amounts)

    def __getitem__(self, key):
        position = key if isinstance(key, int) else self.names.index(key)
        return self.amounts[position]

    def __setitem__(self, key, value):
        if value < 0:
            raise ValueError(f"Expected non-negative amount of resource, got {key}")

        position = key if isinstance(key, int) else self.names.index(key)
        self.amounts[position] = value

    def zeroed(self):
        zeroed_amounts = np.zeros_like(self.amounts)
        return Resources(self.names, zeroed_amounts)

    def __add__(self, other):
        return Resources(self.names, self.amounts + other.amounts)

    def __sub__(self, other):
        assert self >= other
        return Resources(self.names, self.amounts - other.amounts)

    def __lt__(self, other):
        return self <= other and self != other

    def __le__(self, other):
        return (self.amounts <= other.amounts).all()

    def __gt__(self, other):
        return self >= other and self != other

    def __ge__(self, other):
        return (self.amounts >= other.amounts).all()

    def __eq__(self, other):
        return np.array_equal(self.amounts, other.amounts)

    def __str__(self):
        return "Resources[" + ", ".join(
            [self.names[i] + ": " + str(self.amounts[i]) for i in range(len(self.amounts))]) + "]"

    def __repr__(self):
        return f"Resources({self.names}, {self.amounts.tolist()})"
