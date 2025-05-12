import pprint


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, node, value):
        if self.root is None:
            self.root = TreeNode(value)
        elif value <= node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def insert(self, value):
        self._insert(self.root, value)
        self.size += 1

    def __len__(self):
        return self.size

    def __contains__(self, value):
        return self.search(value) is not None

    def remove(self, value):
        pass

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
    bt = BinaryTree()
    bt.insert(1)
    bt.insert(2)
    bt.insert(4)
    bt.insert(-1)
    bt.insert(-5)

    bt.print()
    bt.insert(1.5)
    bt.print()
