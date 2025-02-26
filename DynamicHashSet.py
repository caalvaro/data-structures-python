from DoublyLinkedList import DoublyLinkedList


class HashSet:
    def __init__(self, capacity=10, load_factor_threshold=0.75):
        self.initial_capacity = capacity
        self.buckets = [DoublyLinkedList() for _ in range(capacity)]
        self.load_factor_threshold = load_factor_threshold
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

        if self.size / self.capacity > self.load_factor_threshold:
            print("Load factor:", self.size / self.capacity)
            self.resize(self.capacity * 2)

    def remove(self, key):
        if key not in self:
            raise Exception("Key is not in the set.")

        index = self.hash(key)
        linked_list = self.buckets[index]

        linked_list.remove(key)
        self.size -= 1

        if self.capacity > self.initial_capacity and self.size / self.capacity < (
            1 - self.load_factor_threshold
        ):
            print("Load factor:", self.size / self.capacity)
            self.resize(self.capacity // 2)

    def resize(self, new_capacity):
        self.capacity = new_capacity
        old_buckets = self.buckets
        self.buckets = [DoublyLinkedList() for _ in range(new_capacity)]
        self.size = 0

        for bucket in old_buckets:
            for i in range(len(bucket)):
                self.add(bucket[i])

        print("\n\n------- Resize done -------\n")
        self.print_lists()
        print("\n\n\n")

    def __contains__(self, key):
        """if key in conjunto"""
        index = self.hash(key)
        linked_list = self.buckets[index]

        return linked_list.search(key) is not None

    def __len__(self):
        return self.size

    def print_lists(self):
        print(
            "\n".join(
                str(i) + " -> " + str(linked_list)
                for i, linked_list in enumerate(self.buckets)
            )
            + "\n\n"
        )

    def __str__(self):
        elements = []  # [25, 35, 22, 59, 61, 21, 26, 54]
        for linked_list in self.buckets:
            for i in range(len(linked_list)):
                elements.append(linked_list[i])

        return "{" + ", ".join(str(element.item) for element in elements) + "}"


if __name__ == "__main__":
    from random import random

    hashset = HashSet()
    keys = []

    for i in range(10):
        random_float = round(random(), 2)
        keys.append(random_float)
        hashset.add(random_float)
        hashset.print_lists()

    print(keys)

    for key in keys:
        hashset.remove(key)
        hashset.print_lists()

    hashset.print_lists()
    print()
    print(hashset)
