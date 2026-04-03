from os.path import curdir


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
            return self._search (current.left, value)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self):
        return self._inorder(self.root)
    def _inorder (self, current):
        if current is None:
            return []

        return self._inorder (current.left) + [current.value] + self._inorder(current.right)

    def preorder(self):
        return self._postorder (self.root)

    def _postorder(self, current):
        if current is None:
            return []
        return self._postorder(current.left) + self._postorder(current.right) + [current.value]

    def delete (self, value):
        self.root =self._delete (self.root, value)

    def _delete(self, current, value):
        if current is None:
            return current






