from .doubly_linked_list import DoublyLinkedList


class HashSet:
    """
    HashSet is a data structure that implements a set using a hash table.
    It uses a list of linked lists to store the elements in the set.
    The hash table is implemented using a list of linked lists, where each linked list
    is a bucket that stores the elements that hash to the same index.

    """
    def __init__(self, capacity=10):
        """
        Initializes the HashSet with a given capacity.
        Args:
            buckets (list[DoublyLinkedList]): The list of buckets for the HashSet.
            capacity (int): The initial capacity of the HashSet.
            size (int): The number of elements in the HashSet.
        """
        self.buckets = [DoublyLinkedList() for _ in range(capacity)]
        self.capacity = capacity
        self.size = 0

    def hash(self, key):
        """
        Hash function that computes the index of the bucket for a given key.
        Args:
            key: The key to be hashed.
        Returns:
            Porcentage of the key in the capacity of the HashSet.
        """
        return hash(key) % self.capacity

    def add(self, key):
        """
        Adds a key to the HashSet.

        Args:
            key: The key to be added to the HashSet.
        """
        if key in self:  # if self.__contains__(key):
            return

        index = self.hash(key)
        linked_list = self.buckets[index]
        linked_list.append(key)
        self.size += 1

    def remove(self, key):
        """
        Removes a key from the HashSet.

        Args:
            key: The key to be removed from the HashSet.
        """
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
        """Returns the number of elements in the HashSet."""
        return self.size

    def print_lists(self):
        """ Prints the contents of each bucket in the HashSet."""
        return "\n".join(
            str(i) + " -> " + str(linked_list)
            for i, linked_list in enumerate(self.buckets)
        )

    def __str__(self):
        """Returns a string representation of the HashSet."""
        elements = []  # [25, 35, 22, 59, 61, 21, 26, 54]
        for linked_list in self.buckets:
            for i in range(len(linked_list)):
                elements.append(linked_list[i])

        return "{" + ", ".join(str(element.item) for element in elements) + "}"


if __name__ == "__main__":
    from random import random

    hashset = HashSet()

    for i in range(50):
        hashset.add(round(random(), 2))

    print(hashset.print_lists())
    print()
    print(hashset)
