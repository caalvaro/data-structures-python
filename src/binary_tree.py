from abc import abstractmethod, ABC
import pprint
from typing import Any, TypeVar, Generic, Optional


class Comparable(ABC):
    @abstractmethod
    def __lt__(self, a: Any) -> bool:
        pass


T = TypeVar("T", bound=Comparable)


class TreeNode(Generic[T]):
    def __init__(self, value: T, parent: Optional["TreeNode[T]"]) -> None:
        self.value: T = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None
        self.parent: Optional[TreeNode[T]] = parent

    def has_no_child(self) -> bool:
        return self.left is None and self.right is None

    def has_one_child(self) -> bool:
        return (self.left is None) ^ (self.right is None)

    def has_two_childs(self) -> bool:
        return self.left is not None and self.right is not None

    def get_child(self) -> Optional["TreeNode[T]"]:
        if self.left is not None:
            return self.left
        else:
            return self.right

    def get_successor(self) -> Optional["TreeNode[T]"]:
        if self.right is None:
            return

        aux_node = self.right

        while aux_node.left is not None:
            aux_node = aux_node.left

        return aux_node

    def replace(self, new_node: Optional["TreeNode[T]"]) -> None:
        if self.parent is not None:
            if self.parent.left == self:
                self.parent.left = new_node
            else:
                self.parent.right = new_node

        if new_node and self.left != new_node:
            new_node.left = self.left
        if new_node and self.right != new_node:
            new_node.right = self.right


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[TreeNode[T]] = None
        self.size: int = 0

    def _insert(self, node: TreeNode[T], value: T) -> None:
        if value <= node.value:
            if node.left is None:
                node.left = TreeNode(value, node)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value, node)
            else:
                self._insert(node.right, value)

    def insert(self, value: T):
        if self.root is None:
            self.root = TreeNode(value, None)
            return

        self._insert(self.root, value)
        self.size += 1

    def __len__(self) -> int:
        return self.size

    def __contains__(self, value) -> bool:
        return self.search(value) is not None

    def remove(self, value: T) -> None:
        node_to_remove = self.search(value)

        if node_to_remove is None:
            raise Exception("Value doesn't exist in the tree.")

        self.size -= 1

        if node_to_remove.has_no_child():
            if node_to_remove == self.root:
                self.root = None
            else:
                node_to_remove.replace(None)
        elif node_to_remove.has_one_child():
            if node_to_remove == self.root:
                self.root = node_to_remove.get_child()
            node_to_remove.replace(node_to_remove.get_child())
        else:
            successor = node_to_remove.get_successor()

            if successor is not None:
                successor.replace(None)

            if node_to_remove == self.root:
                self.root = successor

            node_to_remove.replace(successor)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)

    def search(self, value):
        return self._search(self.root, value)

    def _inorder(self, node, values):
        if node is None:
            return values

        values = self._inorder(node.left, values)
        values.append(node.value)
        values = self._inorder(node.right, values)

        return values

    def inorder(self):
        return self._inorder(self.root, [])

    def _print(self, node):
        if node is None:
            return None

        return {
            "value": node.value,
            "left": self._print(node.left),
            "right": self._print(node.right),
        }

    def print(self):
        pprint.pprint(self._print(self.root))


if __name__ == "__main__":
    # To-Do
    # Refactor functions and types
    # implement self balancing tree
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(4)
    bt.insert(-1)
    bt.insert(-5)

    bt.print()
    bt.insert(1.5)
    bt.print()
