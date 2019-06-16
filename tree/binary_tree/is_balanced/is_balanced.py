class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def is_balanced_rec(root, depth):

    if root is None:
        return True, depth

    left_balanced, left_depth = is_balanced_rec(root.left, depth + 1)
    right_balanced, right_depth = is_balanced_rec(root.right, depth + 1)

    subtree_depth = max(left_depth, right_depth)
    if not left_balanced or not right_balanced:
        return False, subtree_depth
    return abs(left_depth - right_depth) <= 1, subtree_depth


def is_balanced(root):
    balanced, depth = is_balanced_rec(root, 1)
    return balanced


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    assert is_balanced(root) is True

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.left.left = Node(6)
    assert is_balanced(root) is False
