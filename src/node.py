from typing import Any


class Node:
    def __init__(self, item: Any):
        if item is not None:
            self.prev_node = Node(None)
            self.next_node = Node(None)

        self.item = item

    def __str__(self) -> str:
        return str(self.item)
