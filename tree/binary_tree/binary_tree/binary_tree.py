from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def search_dfs(self, target):
        """ search the entire tree looking for a value" in dfs order"""
        stack = [self.root]
        while stack:
            curr = stack.pop()
            if curr.val == target:
                return curr
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return None

    def search_bfs(self, target):
        """ search the entire tree looking for a value" in bfs order"""
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            if curr.val == target:
                return curr
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        return None
