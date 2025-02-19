from DoublyLinkedList import DoublyLinkedList


class HashSet:
    def __init__(self, capacity=10):
        self.buckets = [DoublyLinkedList() for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def add(self, key):
        if key in self:  # if self.__contains__(key):
            return

        index = self.hash(key)
        linked_list = self.buckets[index]
        linked_list.append(key)
        self.size += 1

    def remove(self, key):
        if key not in self:
            raise Exception("Key is not in the set.")

        index = self.hash(key)
        linked_list = self.buckets[index]

        linked_list.remove(key)
        self.size -= 1

    def __contains__(self, key):
        """if key in conjunto"""
        index = self.hash(key)
        linked_list = self.buckets[index]

        return linked_list.search(key) is not None

    def __len__(self):
        return self.size

    def print_lists(self):
        return "\n".join(
            str(i) + " -> " + str(linked_list)
            for i, linked_list in enumerate(self.buckets)
        )

    def __str__(self):
        elements = []  # [25, 35, 22, 59, 61, 21, 26, 54]
        for linked_list in self.buckets:
            for i in range(len(linked_list)):
                elements.append(linked_list[i])

        return "{" + ", ".join(str(element.item) for element in elements) + "}"


if __name__ == "__main__":
    hashset = HashSet()

    hashset.add("25")
    hashset.add("35")
    hashset.add("21")
    hashset.add("22")
    hashset.add("26")
    hashset.add("54")
    hashset.add("59")
    hashset.add("61")
    hashset.add("72")
    print(hashset.print_lists())
    print()
    print(hashset)
