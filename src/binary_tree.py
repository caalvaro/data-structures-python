from abc import abstractmethod, ABC
import pprint
from typing import Any, TypeVar, Generic, Optional, List

# ABC means Abstract Base Class, and it is used to define abstract methods that must be implemented by subclasses.
class Comparable(ABC):
    '''Comparable is an abstract class that defines a contract for comparison.'''
    @abstractmethod
    # __le__ means: Less than or equal to
    def __le__(self, a: Any) -> bool:
        pass

    @abstractmethod
    # __gt__ means: Greater than
    def __gt__(self, a: Any) -> bool:
        pass

    # This method is not abstract, but it can be overridden by subclasses.
    def append(self, a: Any) -> None:
        raise NotImplementedError("This method should be implemented by subclasses.")

T = TypeVar("T", bound=Comparable)


class TreeNode(Generic[T]):
    '''ThreeNode is a generic class that represents a node in a binary tree.
    It contains a value, references to its left and right children, and a reference to its parent.
    The type of the value is defined by the type variable T, which must be a subclass of Comparable.
    '''

    def __init__(self, value: T, parent: Optional["TreeNode[T]"]) -> None:
        '''Initialize a TreeNode with a value and an optional parent.
        Args:
            value (T): The value of the node, which must be a subclass of Comparable.
            left (Optional[TreeNode[T]]): The left child of this node, or None if it has no left child.
            right (Optional[TreeNode[T]]): The right child of this node, or None if it has no right child.
            parent (Optional[TreeNode[T]]): The parent node of this node, or None if it is the root.

        Return: None
        '''
        self.value: T = value
        self.left: Optional[TreeNode[T]] = None
        self.right: Optional[TreeNode[T]] = None
        self.parent: Optional[TreeNode[T]] = parent

    def has_no_child(self) -> bool:
        '''Check if the node has no child.

        Returns:
            bool: True if the node has no children, False otherwise.
        '''
        return self.left is None and self.right is None

    def has_one_child(self) -> bool:
        '''Check if the node has one child.

        Returns:
            bool: True if the node has no children, False otherwise.
        '''
        return (self.left is None) ^ (self.right is None)

    def has_two_childs(self) -> bool:
        '''Check if the node has two children.
        Returns:
            bool: True if the node has two children, False otherwise.
        '''
        return self.left is not None and self.right is not None

    def get_child(self) -> Optional["TreeNode[T]"]:
        '''Get the child of the node.
        If the node has two children, it returns the left child.
        If the node has one child, it returns that child.
        If the node has no children, it returns None.'

        Returns:
            Optional[TreeNode[T]]: The child of the node, or None if it has no children.
        '''
        if self.left is not None:
            return self.left
        else:
            return self.right

    def get_successor(self) -> Optional["TreeNode[T]"]:
        '''Get the successor of the node.
        The successor is the smallest node in the right subtree.
        If the node has no right child, it returns None.
        Returns:
            Optional[TreeNode[T]]: The successor of the node, or None if it has no right child.
        '''
        if self.right is None:
            return

        aux_node = self.right

        while aux_node.left is not None:
            aux_node = aux_node.left

        return aux_node

    def replace(self, new_node: Optional["TreeNode[T]"]) -> None:
        '''Replace the current node with a new node.
        If the new node is None, it removes the current node from the tree.
        If the new node is not None, it replaces the current node with the new node.
        Args:
            new_node (Optional[TreeNode[T]]): The new node to replace the current node.
        Returns:  None '''
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
    '''BinaryTree is a generic class that represents a binary tree.
    It contains a root node and a size attribute to keep track of the number of nodes in the tree.
    The type of the values in the tree is defined by the type variable T, which must be a subclass of Comparable.'''

    def __init__(self) -> None:
        '''Initialize a BinaryTree with no root and size 0.
        Returns: None'''
        self.root: Optional[TreeNode[T]] = None
        self.size: int = 0

    def _insert(self, node: TreeNode[T], value: T) -> None:
        '''Insert a value into the binary tree.
        This method is called recursively to find the correct position for the new value.
        Args:
            node (TreeNode[T]): The current node to compare the value with.
            value (T): The value to be inserted into the tree.
        Returns: None '''
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
        '''Insert a value into the binary tree.
        If the tree is empty, it creates a new root node.
        If the tree is not empty, it calls the _insert method to find the correct position for the new value.
        Args:
            value (T): The value to be inserted into the tree.'''
        if self.root is None:
            self.root = TreeNode(value, None)
            return

        self._insert(self.root, value)
        self.size += 1

    def __len__(self) -> int:
        '''Return the size of the binary tree.
        Returns:
            int: The number of nodes in the binary tree.
        '''
        return self.size

    def __contains__(self, value) -> bool:
        '''Check if a value is in the binary tree.
        Args:
            value (T): The value to be checked for existence in the tree.
        Returns:
            bool: True if the value exists in the tree, False otherwise.
        '''
        return self.search(value) is not None

    def remove(self, value: T) -> None:
        '''Remove a value from the binary tree.
        This method searches for the node with the given value and removes it from the tree.
        If the node has no children, it simply removes it.
        If the node has one child, it replaces the node with its child.
        If the node has two children, it finds the successor (the smallest node in the right subtree) and replaces the node with the successor.
        Args:
            value (T): The value to be removed from the tree.
        Returns: None'''
        node_to_remove: Optional[TreeNode[T]] = self.search(value)

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

    def _search(self, node: Optional[TreeNode[T]], value: T):
        '''Search for a value in the binary tree.
        This method is called recursively to find the node with the given value.
        Args:
            node (Optional[TreeNode[T]]): The current node to compare the value with.
            value (T): The value to be searched in the tree.
        Returns:
            Optional[TreeNode[T]]: The node with the given value, or None if the value is not found.
        '''
        if node is None or node.value == value:
            return node
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)

    def search(self, value: T):
        '''Search for a value in the binary tree.
        This method calls the _search method to find the node with the given value.
        Args:
            value (T): The value to be searched in the tree.
        Returns:
            Optional[TreeNode[T]]: The node with the given value, or None if the value is not found.
        '''
        return self._search(self.root, value)

    # list (List) é mutável e aceita .append(), mas é invariante e pode causar erros de tipagem em genéricos.
    def _inorder(self, node: Optional[TreeNode[T]], values: List[T]):
        '''Perform an inorder traversal of the binary tree.
        This method is called recursively to visit the left subtree, then the current node, and finally the right subtree.
        Args:
            node (Optional[TreeNode[T]]): The current node to visit.
            values (List[T]): A list to store the values in inorder.
        Returns:
            List[T]: A list of values in inorder traversal.'''
        if node is None:
            return values

        values = self._inorder(node.left, values)
        values.append(node.value)
        values = self._inorder(node.right, values)

        return values

    def inorder(self):
        '''Get the values of the binary tree in inorder traversal.
        Returns:
            List[T]: A list of values in inorder traversal.
        '''
        return self._inorder(self.root, [])

    def _print(self, node: Optional[TreeNode[T]]):
        '''Print the binary tree in a structured format.
        This method is called recursively to print the current node and its left and right children.
        Args:
            node (Optional[TreeNode[T]]): The current node to print.
        Returns:
            dict: A dictionary representation of the binary tree, with the current node's value and its left and right children.
        '''
        if node is None:
            return None

        return {
            "value": node.value,
            "left": self._print(node.left),
            "right": self._print(node.right),
        }

    def print(self):
        '''Print the binary tree in a structured format.
        This method calls the _print method to get the dictionary representation of the binary tree and prints it.
        Returns: None'''
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
