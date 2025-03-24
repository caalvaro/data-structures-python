from .doubly_linked_list import DoublyLinkedList
from typing import Hashable


class DynamicHashSet:
    """
    Basic implementation of a HashSet with dynamic resizing of its capacity.

    Atributes:
    initial_capacity (int): the capacity passed as a param in the instantiation of the class.
    buckets (list[DoubleLinkedList]):
    """

    def __init__(self, capacity=10, load_factor_threshold=0.75):
        self.initial_capacity = capacity
        self.buckets = [DoublyLinkedList() for _ in range(capacity)]
        self.load_factor_threshold = load_factor_threshold
        self.capacity = capacity
        self.size = 0

    def _hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def add(self, key: Hashable) -> None:
        """
        Add a new key to the HashSet.

        Params:
        key (Hashable): A key of any hashable type to store in the HashSet.
        """
        if key in self:  # if self.__contains__(key):
            return

        index = self._hash(key)
        linked_list = self.buckets[index]
        linked_list.append(key)
        self.size += 1

        if self.size / self.capacity > self.load_factor_threshold:
            self.resize(self.capacity * 2)

    def remove(self, key: Hashable) -> None:
        """

        Args:
            key: A port value greater or equal to 1024.

        Returns:
            The new minimum port.

        Raises:
            ConnectionError: If no available port is found.
        """
        if key not in self:
            raise Exception("Key is not in the set.")

        index = self._hash(key)
        linked_list = self.buckets[index]

        linked_list.remove(item=key)
        self.size -= 1

        if self.capacity > self.initial_capacity and self.size / self.capacity < (
            1 - self.load_factor_threshold
        ):
            self.resize(self.capacity // 2)

    def resize(self, new_capacity: int) -> None:
        self.capacity = new_capacity
        old_buckets = self.buckets
        self.buckets = [DoublyLinkedList() for _ in range(new_capacity)]
        self.size = 0

        for bucket in old_buckets:
            for i in range(len(bucket)):
                if bucket[i].item is not None:
                    self.add(bucket[i].item)

        # print("\n\n------- Resize done -------\n")
        # self.print_lists()
        # print("\n\n\n")

    def __contains__(self, key: Hashable) -> bool:
        """if key in conjunto"""
        index = self._hash(key)
        linked_list = self.buckets[index]

        return linked_list.search(key).item is not None

    def __len__(self) -> int:
        return self.size

    def print_lists(self) -> None:
        print(
            "\n".join(
                str(i) + " -> " + str(linked_list)
                for i, linked_list in enumerate(self.buckets)
            )
            + "\n\n"
        )

    def __str__(self) -> str:
        elements = []  # [25, 35, 22, 59, 61, 21, 26, 54]
        for linked_list in self.buckets:
            for i in range(len(linked_list)):
                elements.append(linked_list[i])

        return "{" + ", ".join(str(element.item) for element in elements) + "}"

    def __repr__(self) -> str:
        return "; ".join(
            str(i) + " -> " + str(linked_list)
            for i, linked_list in enumerate(self.buckets)
        )


if __name__ == "__main__":
    from random import random

    hashset = DynamicHashSet(capacity=5)
    keys = []

    for i in range(5):
        random_float = round(random(), 2)
        keys.append(random_float)
        hashset.add(random_float)

    hashset.print_lists()
    print(keys)

    for key in keys:
        hashset.remove(key)
        hashset.print_lists()
