from typing import Any
from .node import Node


class DoublyLinkedList:
    """
    Doublely linked list implementation.

    A doubly linked list is a data structure consisting of a sequence of nodes,
    where each node contains an item and two references: one to the next node and
    one to the previous node. This allows bidirectional traversal of the list.

    Attributes:
        size (int): The number of elements in the list.
        first_node (Node): The first node in the list.
        last_node (Node): The last node in the list.

    """
    def __init__(self) -> None:
        """
        Initializes an empty doubly linked list.

        Attributes:
            size (int): The number of elements in the list.
            first_node (Node): The first node in the list.
            last_node (Node): The last node in the list.
        """
        self.size = 0
        self.first_node = Node(None)
        self.last_node = Node(None)

    def __str__(self) -> str:
        """
        __str__(): Returns a string representation of the list.

        Returns: list_string (str): A string representation of the list.
        If the list is empty, it returns "| |".
        If the list is not empty, it returns a string with the items in the list,
        separated by "|", e.g., "| item1 | item2 | item3 |".
        """
        if self.size == 0:
            return "| |"

        list_string = "|"

        curr_node = self.first_node
        while curr_node.item is not None:
            list_string += " " + str(curr_node.item) + " |"

            curr_node = curr_node.next_node

        return list_string

    def __repr__(self):
        """
        __repr__(): Returns a string representation for debugging.
        This method is called when the object is printed or when it is
        converted to a string.
        Returns: str: A string representation of the list.
        """
        return self.__str__()

    def __getitem__(self, index: int) -> Node:
        """
        __getitem__(index): Returns the node at the specified index.

        Args:
            index (int): The index of the node to be retrieved.

        Returns: curr_node (Node): The node at the specified index.
        """
        counter = 0

        curr_node: Node | None = self.first_node

        while counter < index and curr_node.item is not None:
            counter += 1
            curr_node = curr_node.next_node

        return curr_node

    def __len__(self):
        """
        __len__(): Returns the number of elements in the list.
        """
        return self.size

    def append(self, item: Any) -> None:
        """"
        Append an item to the end of the list.
        Args:
            item (Any): The item to be appended.
            Raises: Exception: If the item is None.

        Returns: new_node (Node): The newly created node containing the item.
        """
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
        """
        search(item): Returns the node containing the item.

        Args: item (Any): The value to be searched for.

        Returns: curr_node (Node): The node containing the item.
        """
        curr_node = self.first_node

        while curr_node.item and curr_node.item != item:
            curr_node = curr_node.next_node

        return curr_node

    def remove(self, index=None, item=None):
        """
        remove(index=None, item=None): Removes an item by index or by value.

        Args:
            index (int): The index of the item to be removed.
            item (Any): The value of the item to be removed.
            Raises: Exception: If both index and item are None.

        """
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
        """"
        insert(elem, pos): Inserts an item at a specific position.
        Args:
            elem (Any): The item to be inserted.
            pos (int): The position at which the item should be inserted.
            Raises: Exception: If the position is invalid.

        Returns: curr_node (Node): The node at the specified position.
        new_node (Node): The newly created node containing the item.
        """
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
