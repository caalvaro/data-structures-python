from doubly_linked_lists import DoublyLinkedList


class Stack(DoublyLinkedList):
    def push(self, item):
        self.append(item)

    def pop(self):
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
