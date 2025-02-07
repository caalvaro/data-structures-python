class HashSet:
    def __init__(self, size=10):
        self.items = [0] * 10
        self.size = size

    def hash(self, item):
        return item % self.size

    def add(self, item):
        index = self.hash(item)
        self.items[index] = item

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    hashset = HashSet()

    hashset.add(25)
    print(hashset, "\n")
    hashset.add(35)
    print(hashset, "\n")
    hashset.add(21)
    print(hashset, "\n")
    hashset.add(22)
    print(hashset, "\n")
    hashset.add(26)
    print(hashset, "\n")
    hashset.add(54)
    print(hashset, "\n")
    hashset.add(59)
    print(hashset, "\n")
    hashset.add(61)
    print(hashset, "\n")
    hashset.add(72)
    print(hashset)
