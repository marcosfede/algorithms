from collections import deque


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def is_subtree(big, small):
    queue = deque([big])
    while queue:
        node = queue.popleft()
        if node.val == small.val:
            same = is_same_tree(node, small)
            if same:
                return True
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p and q and p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return False


if __name__ == '__main__':
    big = Node(3)
    big.left = Node(4)
    big.right = Node(5)
    big.left.left = Node(1)
    big.left.right = Node(2)
    small = Node(4)
    small.left = Node(1)
    small.right = Node(2)
    assert is_subtree(big, small) is True

    big = Node(3)
    big.left = Node(4)
    big.right = Node(5)
    big.left.left = Node(1)
    big.left.right = Node(2)
    big.left.left.left = Node(0)
    small = Node(3)
    small.left = Node(4)
    small.left.left = Node(1)
    small.left.right = Node(2)
    assert is_subtree(big, small) is False
