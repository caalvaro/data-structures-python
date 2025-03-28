from typing import Any
from .node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.first_node = Node(None)
        self.last_node = Node(None)

    def __str__(self) -> str:
        if self.size == 0:
            return "| |"

        list_string = "|"

        curr_node = self.first_node
        while curr_node.item is not None:
            list_string += " " + str(curr_node.item) + " |"

            curr_node = curr_node.next_node

        return list_string

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, index: int) -> Node:
        counter = 0

        curr_node: Node | None = self.first_node

        while counter < index and curr_node.item is not None:
            counter += 1
            curr_node = curr_node.next_node

        return curr_node

    def __len__(self):
        return self.size

    def append(self, item: Any) -> None:
        if item is None:
            raise Exception("Item can not be None.")

        new_node = Node(item)

        if self.size == 0:
            self.size += 1
            self.first_node = new_node
            self.last_node = new_node
            return

        self.size += 1

        new_node.prev_node = self.last_node
        self.last_node.next_node = new_node
        self.last_node = new_node

    def search(self, item):
        curr_node = self.first_node

        while curr_node.item and curr_node.item != item:
            curr_node = curr_node.next_node

        return curr_node

    def remove(self, index=None, item=None):
        self.size -= 1

        if index is not None:
            curr_node = self[index]
        elif item is not None:
            curr_node = self.search(item)

        if curr_node == self.first_node:
            second_node = self.first_node.next_node
            self.first_node = second_node
        else:
            curr_node.prev_node.next_node = curr_node.next_node

        if curr_node == self.last_node:
            penult_node = self.last_node.prev_node
            self.last_node = penult_node
        else:
            curr_node.next_node.prev_node = curr_node.prev_node

    def insert(self, elem, pos):
        if pos < 0 or pos > self.size:
            raise Exception("Position not valid.")

        if pos == self.size:
            self.append(elem)
            return

        new_node = Node(elem)
        self.size += 1

        curr_node = self[pos]

        if pos == 0:
            self.first_node = new_node
        else:
            prev_node = curr_node.prev_node
            prev_node.next_node = new_node
            new_node.prev_node = prev_node

        curr_node.prev_node = new_node
        new_node.next_node = curr_node


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.append(100)
    doubly_linked_list.append(200)
    doubly_linked_list.append(300)
    doubly_linked_list.append(400)
    doubly_linked_list.append(500)

    print(doubly_linked_list)
    print("Tamanho:", len(doubly_linked_list))

    doubly_linked_list.insert(99, 0)

    print(doubly_linked_list)
    print("Tamanho:", len(doubly_linked_list))

    doubly_linked_list.insert(250, 3)

    print(doubly_linked_list)
    print("Tamanho:", len(doubly_linked_list))

    doubly_linked_list.insert(550, 7)

    print(doubly_linked_list)
    print("Tamanho:", len(doubly_linked_list))

    doubly_linked_list.insert(550, 50)
