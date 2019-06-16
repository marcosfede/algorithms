class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self, root):
        self.root = root

    def search(self, target):
        curr = self.root
        while curr is not None:
            if curr.val == target:
                return curr
            elif target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
        return None

    def insert(self, node):
        """ insert a new node assuming there are no repeated values"""
        curr = self.root
        while True:
            if node.val < curr.val:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left
            elif node.val > curr.val:
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right
