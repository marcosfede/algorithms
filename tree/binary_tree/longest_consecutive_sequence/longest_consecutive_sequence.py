maxlen = 0


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
    DFS(root, 0, root.val)
    return maxlen


def DFS(root, cur, target):
    global maxlen
    if not root:
        return
    if root.val == target:
        cur += 1
    else:
        cur = 1
    maxlen = max(cur, maxlen)
    DFS(root.left, cur, root.val + 1)
    DFS(root.right, cur, root.val + 1)


if __name__ == '__main__':
    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    assert longest_consecutive(root) == 3
