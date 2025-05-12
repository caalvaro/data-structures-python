class Node:
    """
    Represents a node in a singly linked list.

    Each node stores a single data item and a reference to the next node
    in the list. This class is used as the fundamental building block for
    singly linked list structures.

    Attributes:
        item (Any): The value stored in the node.
        next_node (Node | None): Reference to the next node in the list.

    """
    def __init__(self, item=None) -> None:
        """Initializes a node with an optional item.

        Args:
            item (Any, optional): The value to store in the node. Defaults to None.
        """
        self.item = item
        self.next_node = None

    def __str__(self) -> str:
        """ Returns a string representation of the node's item."""
        return str(self.item)


def print_linked_list(head: Node) -> None:
    """
    Prints the contents of a singly linked list.

    Args:
        head (Node): The head node of the linked list.
    """
    if head.next_node.item is None:
        print("| |")
        return

    list_string = "|"

    curr_node = head.next_node
    while curr_node.item is not None:
        list_string += " " + str(curr_node.item) + " |"

        curr_node = curr_node.next_node

    print(list_string)


def append(head: Node, item):
    """
    Appends a new item to the end of the singly linked list.

    Args:
        head (Node): The head node of the linked list.
        item (Any): The value to append to the list.

    """
    new_node = Node(item)

    if head.next_node.item is None:
        head.next_node = new_node
        return

    aux_node = head.next_node
    while aux_node.next_node.item is not None:
        aux_node = aux_node.next_node

    aux_node.next_node = new_node


def search(head: Node, item):
    """
    Searches for an item in the singly linked list.
    Args:
        head (Node): The head node of the linked list.
        item (Any): The value to search for in the list.

    Returns:
        Node: The node containing the item if found, otherwise None.
    """
    aux_node = head

    while aux_node.item != item and aux_node.next_node.item is not None:
        aux_node = aux_node.next_node

    return aux_node


def get_node(head: Node, index):
    """
    Gets the node at a specific index in the singly linked list.
    Args:
        head (Node): The head node of the linked list.
        index (int): The index of the node to retrieve.

    Returns:
        Node: The node at the specified index.
    """
    aux_node = head
    counter = 0

    while counter < index:
        aux_node = aux_node.next_node
        counter += 1

    return aux_node


def remove(head: Node, index=None, item=None):
    """
    Removes a node from the singly linked list by index or item.
    Args:
        head (Node): The head node of the linked list.
        index (int): The index of the node to remove. Defaults to None.
        item (Any): The value of the node to remove. Defaults to None.

    """
    if index is not None:
        prev_node = get_node(head, index - 1)
        curr_node = prev_node.next_node
    elif item is not None:
        aux_node = head

        while aux_node.next_node.item is not None and aux_node.next_node.item != item:
            aux_node = aux_node.next_node

        prev_node = aux_node
        curr_node = prev_node.next_node

    if curr_node == head.next_node:
        head.next_node = curr_node.next_node
        return

    prev_node.next_node = curr_node.next_node


def insert(head, elem, pos):
    """
    Inserts a new node with the given element at the specified position in the singly linked list.

    Args:
        head (Node): The head node of the linked list.
        elem (Any): The value to insert into the list.
        pos (int): The position at which to insert the new node.
    """
    new_node = Node(elem)

    prev_node = get_node(head, pos - 1)
    curr_node = prev_node.next_node

    prev_node.next_node = new_node
    new_node.next_node = curr_node


if __name__ == "__main__":
    head = Node(None)

    append(head, 100)
    append(head, 200)
    append(head, 300)
    append(head, 400)
    append(head, 500)
    append(head, 600)
    append(head, 700)
    append(head, 800)
    append(head, 900)

    print_linked_list(head)

    remove(head, item=100)
    print_linked_list(head)

    remove(head, index=1)
    print_linked_list(head)

    remove(head, index=3)
    print_linked_list(head)

    remove(head, item=700)
    print_linked_list(head)

    remove(head, index=5)
    print_linked_list(head)

    remove(head, item=800)
    print_linked_list(head)

    insert(head, 50, 1)
    print_linked_list(head)

    insert(head, 60, 2)
    print_linked_list(head)

    insert(head, 70, 5)
    print_linked_list(head)

    insert(head, 80, 7)
    print_linked_list(head)

    # remove(head, item=100)
    # print_linked_list(head)

    # remove(head, index=1)
    # print_linked_list(head)

    # insert(99, 0)

    # print(single_linked_list)

    # insert(250, 3)

    # print(single_linked_list)

    # insert(550, 8)

    # print(single_linked_list)

    # insert(550, 50)
