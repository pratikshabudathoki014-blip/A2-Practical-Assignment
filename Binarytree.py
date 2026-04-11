from os.path import curdir
from unittest.mock import right


class Node:
    def __init__(self,value) :
        self.value= value
        self.left= None
        self.right= None
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if self.root is None:
            self.root= Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left=Node(value)
            else:
                self._insert(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)


    def search (self, value):
        return self._search (self.root, value)
    def _search(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search (current.right, value)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder (self, current):
        if current is None:
            return []

        return self._inorder (current.left) + [current.value] + self._inorder(current.right)

    def preorder(self):
        return self._preorder (self.root)
    def _preorder(self, current):
        if current is None:
            return []
        return [current.value] + self._preorder(current.left)+ self._preorder(current.right)

    def postorder(self):
        return self._postorder(self.root)
    def _postorder(self, current):
        if current is None:
            return []
        return self._postorder(current.left) + self._postorder(current.right) + [current.value]

    def delete (self, value):
        self.root =self._delete (self.root, value)

    def _delete(self, current, value):
        if current is None:
            return current
        if value < current.value:
            current.left = self._delete (current.left, value)
        elif value > current.value:
            current.right = self._delete(current.right, value)
        else:
            if current.left is None and current.right is None:
                return None

            elif current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            min_node = self._find_min(current.right)
            current.value = min_node. value
            current.right = self._delete(current.right, min_node.value)
        return current

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node



def main():
    tree= BinaryTree()
    values = [50,30,70,20,40,60,80]
    for v in values:
        tree.insert (v)

    tree.delete(20)
    tree.delete(30)
    tree.delete(50)


    print("Inorder:", tree.inorder())



if __name__ == "__main__":
    main()




















