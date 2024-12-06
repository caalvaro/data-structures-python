class Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next_node = None

    def __str__(self) -> str:
        return str(self.item)


class SingleLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.first_node = None
        self.last_node = None

    def __str__(self) -> str:
        if self.size == 0:
            return "| |"

        list_string = "|"

        curr_node = self.first_node
        while curr_node is not None:
            list_string += " " + str(curr_node.item) + " |"

            curr_node = curr_node.next_node

        return list_string

    def append(self, item):
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
        counter = 0
        curr_node = self.first_node

        while counter < index:
            counter += 1
            curr_node = curr_node.next_node

        return curr_node

    def getNodeAndPrevious(self, index):
        counter = 0
        curr_node = self.first_node
        prev_node = None

        while counter < index:
            counter += 1
            prev_node = curr_node
            curr_node = curr_node.next_node

        return curr_node, prev_node

    def search(self, item):
        curr_node = self.first_node
        prev_node = None

        while curr_node.item != item:
            prev_node, curr_node
            curr_node = curr_node.next_node

        return curr_node, prev_node

    def remove(self, index=None, item=None):
        self.size -= 1

        if index is not None:
            curr_node, prev_node = self.getNodeAndPrevious(index)
        elif item is not None:
            curr_node, prev_node = self.search(item)

        if curr_node == self.first_node:
            self.first_node = curr_node.next_node
            return

        prev_node.next_node = curr_node.next_node


if __name__ == "__main__":
    single_linked_list = SingleLinkedList()

    single_linked_list.append(100)
    single_linked_list.append(200)
    single_linked_list.append(300)
    single_linked_list.append(400)
    single_linked_list.append(500)

    print(single_linked_list)
    print(single_linked_list[2])

    single_linked_list.remove(2)
    print(single_linked_list)
