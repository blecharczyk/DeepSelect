class Resources:
    def __init__(self, dict):
        self.dict = dict.copy()


    def __len__(self):
        return len(self.dict)


    def __getitem__(self, key):
        return self.dict[key]


    def __setitem__(self, key, value):
        if value < 0:
            raise ValueError(f"Expected non-negative amount of resource, got {key}")
        self.dict[key] = value


    def zeroed(self):
        d = self.dict.copy()
        for i in d:
            d[i] = 0
        return Resources(d)


    def __add__(self, other):
        for key_o in other.dict:
            if key_o in self.dict:
                self.dict[key_o] = self.dict[key_o] + other.dict[key_o]
            else:
                self.dict[key_o] = other.dict[key_o]
        return self


    def __sub__(self, other):
        for a in other.dict:
            assert a in self.dict
            assert self.dict[a] >= other.dict[a]
        for a in other.dict:
            self.dict[a] = self.dict[a] - other.dict[a]
        return self


    def __lt__(self, other):
        if (self == other):
            return False
        for a in self.dict:
            if a in other.dict:
                if self.dict[a] > other.dict[a]:
                    return False
            elif self.dict[a] != 0:
                return False
        return True


    def __le__(self, other):
        return (self == other) or (self < other)


    def __gt__(self, other):
        if (self == other):
            return False
        for a in self.dict:
            if a in other.dict:
                if self.dict[a] < other.dict[a]:
                    return False
            elif self.dict[a] != 0:
                return True
        return True


    def __ge__(self, other):
        return (self == other) or (self > other)


    def __eq__(self, other):
        if len(self.dict) != len(other.dict):
            return False
        for a in self.dict:
            if not (a in other.dict):
                return False
        for a in self.dict:
            if self.dict[a] != other.dict[a]:
                return False
        return True


    def __str__(self):
        s = "["
        for i in self.dict:
            s = s + str(i) + ":" + str(self.dict[i]) + ", "
        s = s[:-2]
        s = s + "]"
        return s


    def __repr__(self):
        s = "["
        for i in self.dict:
            s = s +  str(i) + ":" + str(self.dict[i]) + ", "
        s = s[:-2]
        s = s + "]"
        return s













