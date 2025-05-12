from .doubly_linked_list import DoublyLinkedList


class Stack(DoublyLinkedList):
    """
    Stack is a data structure that follows the Last In First Out (LIFO) principle.
    It allows for adding and removing elements from the same end, known as the top of the stack.

    This implementation uses a doubly linked list to manage the elements, providing efficient
    operations for pushing and popping items. The stack maintains a reference to the last node,
    which represents the top of the stack, and tracks the size of the stack.

    Attributes:
        size (int): The number of elements currently in the stack.
        first_node (Node | None): The first node in the stack.
        last_node (Node | None): The last node in the stack.
    """

    def push(self, item):
        """
        Pushes an item onto the top of the stack.

        Args:
            item (Any): The value to be added to the stack.
        """
        self.append(item)

    def pop(self):
        """
        Pops the top item from the stack.
        Removes the last node from the stack and returns it.

        Returns:
            Node: The node that was removed from the stack.
        """
        last_node = self.last_node
        self.size -= 1

        if last_node == self.first_node:
            second_node = self.first_node.next_node
            self.first_node = second_node
        else:
            last_node.prev_node.next_node = last_node.next_node

        if last_node == self.last_node:
            penult_node = self.last_node.prev_node
            self.last_node = penult_node
        else:
            last_node.next_node.prev_node = last_node.prev_node

        return last_node
