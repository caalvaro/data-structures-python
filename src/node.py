from typing import Any


class Node:
    def __init__(self, item: Any) -> None:
        self.item = item
        self.prev_node = None
        self.next_node = None

    def __str__(self) -> str:
        return str(self.item)
