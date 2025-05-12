from .node import Node


class SingleLinkedList:
    """
    A singly linked list implementation.

    A singly linked list is a linear data structure where each element (node)
    points to the next, allowing for dynamic memory usage and efficient insertion
    and removal operations. This implementation maintains references to both the
    first and last nodes, and tracks the list size.

    Attributes:
        size (int): The number of elements currently in the list.
        first_node (Node | None): The first node in the list.
        last_node (Node | None): The last node in the list.

    Methods:
        append(item): Adds an item to the end of the list.
        insert(elem, pos): Inserts an item at the specified position.
        remove(index=None, item=None): Removes a node by index or by item value.
        search(item): Finds a node and its predecessor by item value.
        __getitem__(index): Returns the node at the specified index.
        __str__(): Returns a string representation of the list.
        getNodeAndPrevious(index): Returns a node and its previous node by index.

    """

    def __init__(self) -> None:
        """
        Initializes an empty singly linked list.
        Sets the size to 0 and both first and last nodes to None.

        Attributes:
            size (int): The number of elements in the list.
            first_node (Node | None): The first node in the list.
            last_node (Node | None): The last node in the list.
        """
        self.size = 0
        self.first_node = Node(None)
        self.last_node = Node(None)

    def __str__(self) -> str:
        """
        Returns a string representation of the singly linked list.
        The string format is "| item1 | item2 | ... | itemN |" where each item
        is the value of a node in the list.
        """
        if self.size == 0:
            return "| |"

        list_string = "|"

        curr_node = self.first_node
        while curr_node.item is not None:
            list_string += " " + str(curr_node.item) + " |"

            if curr_node.item is not None:
                curr_node = curr_node.next_node

        return list_string

    def append(self, item):
        """
        Appends an item to the end of the singly linked list.
        Args:
            item (Any): The value to append to the list.
        If the list is empty, the new node becomes both the first and last node.
        If the list is not empty, the new node is added after the last node,
        and the last node reference is updated to the new node.
        """
        new_node = Node(item)

        if self.size == 0:
            self.size += 1
            self.first_node = new_node
            self.last_node = new_node
            return

        self.size += 1

        self.last_node.next_node = new_node
        self.last_node = new_node

    def __getitem__(self, index):
        """
        Gets the node at the specified index in the singly linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node: The node at the specified index.
        """
        counter = 0
        curr_node = self.first_node

        while counter < index:
            counter += 1
            curr_node = curr_node.next_node

        return curr_node

    def getNodeAndPrevious(self, index):
        """
        Gets the node and its previous node at the specified index in the singly linked list.

        Args:
            index (int): The index of the node to retrieve.

        Returns:
            Node at the specified index and its previous node.

        """
        counter = 0
        curr_node = self.first_node
        prev_node = None

        while counter < index:
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.next_node

        return curr_node, prev_node

    def search(self, item):
        """
        Searches for an item in the singly linked list.

        Args:
            item (Any): The value to search for in the list.

        Returns:
            Node containing the item and its predecessor.
        """
        curr_node = self.first_node
        prev_node = None

        while curr_node.item != item:
            # prev_node, curr_node
            curr_node = curr_node.next_node

        return curr_node, prev_node

    def remove(self, index=None, item=None):
        """
        Removes a node from the singly linked list by index or item value.

        Args:
            index (int): The index of the node to remove. Defaults to None.
            item (Any): The value of the node to remove. Defaults to None.
        """
        self.size -= 1

        if index is not None:
            curr_node, prev_node = self.getNodeAndPrevious(index)
        elif item is not None:
            curr_node, prev_node = self.search(item)

        if curr_node == self.first_node:
            self.first_node = curr_node.next_node
            return

        if prev_node is not None:
            prev_node.next_node = curr_node.next_node

    def insert(self, elem, pos):
        """
        Inserts an item at the specified position in the singly linked list.

        Args:
            elem (Any): The value to insert into the list.
            pos (int): The position at which to insert the new node.

        """
        if pos < 0 or pos > self.size + 1:
            raise Exception("Position not valid.")

        if pos == self.size + 1:
            self.append(elem)
            return

        new_node = Node(elem)
        self.size += 1

        if pos == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return

        aux_node = self.first_node
        counter = 1

        while aux_node.next_node is not None and counter < pos - 1:
            aux_node = aux_node.next_node
            counter += 1

        new_node.next_node = aux_node.next_node
        aux_node.next_node = new_node


if __name__ == "__main__":
    single_linked_list = SingleLinkedList()

    single_linked_list.append(100)
    single_linked_list.append(200)
    single_linked_list.append(300)
    single_linked_list.append(400)
    single_linked_list.append(500)

    print(single_linked_list)

    single_linked_list.insert(99, 0)

    print(single_linked_list)

    single_linked_list.insert(250, 3)

    print(single_linked_list)

    single_linked_list.insert(550, 8)

    print(single_linked_list)

    try:
        single_linked_list.insert(550, 50)
    except:
        print("Position not valid.")
