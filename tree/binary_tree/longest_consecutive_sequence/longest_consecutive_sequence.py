class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def longest_consecutive(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    return DFS(root, None, 0)


def DFS(root, parent, length):
    if not root:
        return length

    if parent and root.val == parent.val + 1:
        length += 1
    else:
        length = 1

    left_length = DFS(root.left, root, length)
    right_length = DFS(root.right, root, length)

    return max(length, left_length, right_length)


if __name__ == '__main__':
    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    assert longest_consecutive(root) == 3
